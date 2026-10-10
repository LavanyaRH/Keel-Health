"""
Keel Health - Clinical Preprocessing and Feature Preparation Module

This module prepares clinical encounter data from the UCI Diabetes 130-US Hospitals dataset
for machine learning readmission risk prediction.

Key Design Decisions & Clinical Safeguards:
1. Cohort Filtering:
   - Excludes terminal encounters (discharge_disposition_id in [11, 13, 14, 19, 20, 21])
     representing in-hospital deaths or discharges to hospice. Patients who expire cannot
     clinically experience readmission; retaining them creates severe outcome leakage
     and distorts risk estimation.
2. Target Definition:
   - Positive class (1): readmitted == '<30' (early 30-day readmission).
   - Negative class (0): readmitted in ['NO', '>30'] (no early readmission).
3. Leakage Prevention:
   - Excludes identifiers (encounter_id, patient_nbr) from model features.
   - Patient-Grouped Splitting: Uses GroupShuffleSplit grouped by patient_nbr so that all
     encounters for any individual patient belong exclusively to either train or test,
     preventing cross-encounter patient leakage.
4. Timing & Prediction Window Review:
   - Inpatient decision support for discharge planning requires risk assessment before or at
     the discharge decision.
   - discharge_disposition_id: By default excluded from model features. It is finalized only at
     discharge and often reflects post-discharge care interventions (e.g. SNF, Home Health),
     which introduces confounding by indication and post-prediction timing leakage if evaluated
     earlier during admission. Supported as an optional toggle for comparison.
   - High-missingness columns: weight (96.86% missing), payer_code (39.56% missing, administrative
     billing code), and medical_specialty (49.08% missing, 73 categories) are excluded to avoid
     imputing synthetic noise into >40-97% of observations.
   - Zero-variance columns: examide and citoglipton are 100% constant ('No') and excluded.
5. Safe Preprocessing:
   - Scikit-learn Pipeline and ColumnTransformer fit strictly on training data.
   - Handles '?' placeholders, ICD-9 diagnosis clustering, missing lab values, and scaling.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Ensure project root is available in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from configs.config import (
    POSITIVE_TARGET_CLASS,
    RANDOM_STATE,
    RAW_DIABETIC_DATA_PATH,
    TARGET_COL,
    TERMINAL_DISCHARGE_IDS,
    TEST_SIZE,
)
from src.data.load_data import load_raw_data


class ICD9Categorizer(BaseEstimator, TransformerMixin):
    """
    Maps ICD-9 diagnostic codes in diag_1, diag_2, and diag_3 into standard
    clinical disease categories to prevent extreme high-cardinality overfitting.

    Categorization taxonomy (Strack et al., 2014 clinical benchmark):
    - Circulatory: 390-459, 785
    - Respiratory: 460-519, 786
    - Digestive: 520-579, 787
    - Diabetes: 250.xx
    - Injury: 800-999
    - Musculoskeletal: 710-739
    - Genitourinary: 580-629, 788
    - Neoplasms: 140-239
    - Other: V-codes, E-codes, other unclassified ICD-9 ranges
    - Missing: '?', NaN, empty strings
    """

    def __init__(self, cols: Optional[List[str]] = None):
        self.cols = cols

    def fit(self, X: Any, y: Any = None) -> ICD9Categorizer:
        return self

    def transform(self, X: Any) -> pd.DataFrame:
        X_out = X.copy()
        target_cols = self.cols if self.cols is not None else [
            c for c in ['diag_1', 'diag_2', 'diag_3'] if c in X_out.columns
        ]

        if isinstance(X_out, pd.DataFrame):
            for col in target_cols:
                if col in X_out.columns:
                    X_out[col] = X_out[col].apply(self._map_single_code)
        return X_out

    def get_feature_names_out(self, input_features: Optional[List[str]] = None) -> np.ndarray:
        if input_features is not None:
            return np.asarray(input_features, dtype=object)
        return np.array(self.cols if self.cols is not None else [], dtype=object)

    @staticmethod
    def _map_single_code(val: Any) -> str:
        if pd.isna(val) or val is None:
            return "Missing"
        s = str(val).strip()
        if s == "?" or s == "":
            return "Missing"
        if s.startswith("V") or s.startswith("E"):
            return "Other"
        try:
            code = float(s)
        except ValueError:
            return "Other"

        if (390 <= code <= 459) or code == 785:
            return "Circulatory"
        elif (460 <= code <= 519) or code == 786:
            return "Respiratory"
        elif (520 <= code <= 579) or code == 787:
            return "Digestive"
        elif 250 <= code < 251:
            return "Diabetes"
        elif 800 <= code <= 999:
            return "Injury"
        elif 710 <= code <= 739:
            return "Musculoskeletal"
        elif (580 <= code <= 629) or code == 788:
            return "Genitourinary"
        elif 140 <= code <= 239:
            return "Neoplasms"
        else:
            return "Other"


class CategoricalStandardizer(BaseEstimator, TransformerMixin):
    """
    Standardizes categorical columns by replacing '?' placeholders with 'Unknown',
    filling nulls (such as unperformed lab tests) with 'Unknown', and casting to string.
    """

    def __init__(self):
        pass

    def fit(self, X: Any, y: Any = None) -> CategoricalStandardizer:
        return self

    def transform(self, X: Any) -> pd.DataFrame:
        X_out = X.copy()
        if isinstance(X_out, pd.DataFrame):
            for col in X_out.columns:
                X_out[col] = (
                    X_out[col]
                    .replace("?", "Unknown")
                    .fillna("Unknown")
                    .astype(str)
                )
        return X_out

    def get_feature_names_out(self, input_features: Optional[List[str]] = None) -> np.ndarray:
        if input_features is not None:
            return np.asarray(input_features, dtype=object)
        return np.array([], dtype=object)


def filter_modeling_cohort(
    df: pd.DataFrame,
    exclude_terminal: bool = True,
    terminal_ids: Optional[List[int]] = None,
) -> pd.DataFrame:
    """
    Filters raw encounter data into a clinically valid modeling cohort.

    Parameters:
        df: Raw DataFrame.
        exclude_terminal: If True, excludes encounters with discharge dispositions
                          corresponding to in-hospital death or hospice transfer.
        terminal_ids: List of discharge disposition IDs to filter out.
                      Defaults to configs.config.TERMINAL_DISCHARGE_IDS.

    Returns:
        pd.DataFrame: Cleaned cohort slice.
    """
    cohort = df.copy()
    if exclude_terminal:
        ids_to_exclude = terminal_ids if terminal_ids is not None else TERMINAL_DISCHARGE_IDS
        terminal_mask = cohort["discharge_disposition_id"].isin(ids_to_exclude)
        excluded_count = int(terminal_mask.sum())
        cohort = cohort[~terminal_mask].copy()
        print(f"[Cohort Selection] Excluded {excluded_count:,} terminal encounters (expired/hospice). Remaining: {len(cohort):,}")
    return cohort


def create_binary_target(
    df: pd.DataFrame,
    target_col: str = TARGET_COL,
    positive_class: str = POSITIVE_TARGET_CLASS,
) -> pd.Series:
    """
    Constructs binary readmission target:
    - 1: readmitted == '<30' (positive class)
    - 0: readmitted in ['NO', '>30'] (negative class)
    """
    if target_col not in df.columns:
        raise KeyError(f"Target column '{target_col}' not found in DataFrame.")
    return (df[target_col] == positive_class).astype(int)


def get_feature_manifest(
    include_discharge_disposition: bool = False,
) -> Tuple[List[str], List[str], Dict[str, str]]:
    """
    Defines numerical features, categorical features, and explicitly excluded features
    with rationale.

    Parameters:
        include_discharge_disposition: Whether to include discharge_disposition_id in features.
                                       Defaults to False to prevent post-prediction timing leakage.

    Returns:
        Tuple[List[str], List[str], Dict[str, str]]: (numerical_cols, categorical_cols, excluded_manifest)
    """
    numerical_cols = [
        "time_in_hospital",
        "num_lab_procedures",
        "num_procedures",
        "num_medications",
        "number_outpatient",
        "number_emergency",
        "number_inpatient",
        "number_diagnoses",
    ]

    base_categorical_cols = [
        "race",
        "gender",
        "age",
        "admission_type_id",
        "admission_source_id",
        "max_glu_serum",
        "A1Cresult",
        "change",
        "diabetesMed",
        "diag_1",
        "diag_2",
        "diag_3",
        "metformin",
        "repaglinide",
        "nateglinide",
        "chlorpropamide",
        "glimepiride",
        "acetohexamide",
        "glipizide",
        "glyburide",
        "tolbutamide",
        "pioglitazone",
        "rosiglitazone",
        "acarbose",
        "miglitol",
        "troglitazone",
        "tolazamide",
        "insulin",
        "glyburide-metformin",
        "glipizide-metformin",
        "glimepiride-pioglitazone",
        "metformin-rosiglitazone",
        "metformin-pioglitazone",
    ]

    categorical_cols = list(base_categorical_cols)
    if include_discharge_disposition:
        categorical_cols.append("discharge_disposition_id")

    excluded_manifest = {
        "encounter_id": "Primary key identifier (100% unique per row, memorization hazard).",
        "patient_nbr": "Patient identifier (leakage hazard; reserved exclusively as group split key).",
        TARGET_COL: "Target variable (separated as y label).",
        "weight": "Extremely high missingness (96.86% '?'). Imputing would create severe artificial noise.",
        "payer_code": "High missingness (39.56% '?') and administrative billing code with no clinical physiological relevance.",
        "medical_specialty": "High missingness (49.08% '?') and high cardinality (73 categories). Blind imputation introduces substantial noise.",
        "examide": "Zero variance / constant feature (100% 'No').",
        "citoglipton": "Zero variance / constant feature (100% 'No').",
    }

    if not include_discharge_disposition:
        excluded_manifest["discharge_disposition_id"] = (
            "Excluded from baseline features to prevent post-prediction timing leakage and intervention confounding. "
            "Discharge disposition is only determined at final discharge and reflects care interventions (e.g. SNF, Home Health), "
            "making it unavailable during earlier inpatient stay decision points."
        )

    return numerical_cols, categorical_cols, excluded_manifest


def patient_grouped_split(
    df: pd.DataFrame,
    patient_col: str = "patient_nbr",
    target_col: str = TARGET_COL,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Performs patient-grouped train/test split using GroupShuffleSplit.
    Guarantees that all encounters of any patient are strictly isolated to either train or test.

    Parameters:
        df: Modeling cohort DataFrame.
        patient_col: Column containing unique patient identifier.
        target_col: Column containing target label.
        test_size: Fraction of patient groups allocated to test.
        random_state: Reproducible random state seed.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: (train_df, test_df)
    """
    if patient_col not in df.columns:
        raise KeyError(f"Patient grouping column '{patient_col}' not found.")

    gss = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=random_state)
    target_binary = create_binary_target(df, target_col=target_col)
    
    train_idx, test_idx = next(gss.split(df, target_binary, groups=df[patient_col]))
    train_df = df.iloc[train_idx].copy()
    test_df = df.iloc[test_idx].copy()

    # Integrity verification: zero patient overlap
    overlap = set(train_df[patient_col]).intersection(set(test_df[patient_col]))
    if len(overlap) > 0:
        raise ValueError(f"Patient leakage detected: {len(overlap)} patients appear in both splits!")

    return train_df, test_df


def build_preprocessor(
    numerical_cols: List[str],
    categorical_cols: List[str],
) -> ColumnTransformer:
    """
    Constructs a scikit-learn ColumnTransformer that cleanly handles numerical
    scaling and categorical encoding without leakage.

    Parameters:
        numerical_cols: List of continuous/count feature names.
        categorical_cols: List of categorical feature names.

    Returns:
        ColumnTransformer: Preprocessor object ready for fitting on training data.
    """
    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])

    diag_cols = [c for c in ["diag_1", "diag_2", "diag_3"] if c in categorical_cols]

    cat_pipeline = Pipeline([
        ("icd_categorizer", ICD9Categorizer(cols=diag_cols)),
        ("cleaner", CategoricalStandardizer()),
        ("imputer", SimpleImputer(strategy="constant", fill_value="Unknown")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", num_pipeline, numerical_cols),
            ("cat", cat_pipeline, categorical_cols),
        ],
        remainder="drop",
    )

    return preprocessor


def prepare_dataset(
    filepath: Optional[Path | str] = None,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
    include_discharge_disposition: bool = False,
    exclude_terminal: bool = True,
) -> Dict[str, Any]:
    """
    Complete end-to-end data preparation workflow:
    1. Loads raw dataset (read-only, never modifies raw source).
    2. Filters cohort (excludes terminal/expired encounters).
    3. Builds binary target (<30 vs NO/>30).
    4. Splits by patient_nbr groups without leakage.
    5. Assembles feature matrices and labels.
    6. Returns dataset artifacts and comprehensive metadata.

    Parameters:
        filepath: Optional path to raw dataset CSV.
        test_size: Proportion of patient groups in test set.
        random_state: Random state seed.
        include_discharge_disposition: Whether to include discharge_disposition_id.
        exclude_terminal: Whether to exclude deceased/hospice encounters.

    Returns:
        Dict[str, Any]: Preprocessing result dictionary containing:
            - X_train, X_test, y_train, y_test
            - train_df, test_df (full dataframes for auditing)
            - preprocessor (unfitted ColumnTransformer)
            - numerical_cols, categorical_cols, excluded_manifest
            - metadata (split counts, target rates, patient counts)
    """
    raw_df = load_raw_data(filepath)
    raw_rows, raw_cols = raw_df.shape

    cohort_df = filter_modeling_cohort(
        raw_df,
        exclude_terminal=exclude_terminal,
    )

    num_cols, cat_cols, excluded_manifest = get_feature_manifest(
        include_discharge_disposition=include_discharge_disposition
    )

    train_df, test_df = patient_grouped_split(
        cohort_df,
        patient_col="patient_nbr",
        target_col=TARGET_COL,
        test_size=test_size,
        random_state=random_state,
    )

    feature_cols = num_cols + cat_cols

    X_train = train_df[feature_cols].copy()
    y_train = create_binary_target(train_df)

    X_test = test_df[feature_cols].copy()
    y_test = create_binary_target(test_df)

    preprocessor = build_preprocessor(num_cols, cat_cols)

    metadata = {
        "raw_shape": [raw_rows, raw_cols],
        "cohort_shape": list(cohort_df.shape),
        "terminal_excluded": exclude_terminal,
        "terminal_encounters_count": int(raw_rows - len(cohort_df)),
        "random_state": random_state,
        "test_size": test_size,
        "train_rows": int(len(train_df)),
        "test_rows": int(len(test_df)),
        "train_unique_patients": int(train_df["patient_nbr"].nunique()),
        "test_unique_patients": int(test_df["patient_nbr"].nunique()),
        "train_positive_count": int(y_train.sum()),
        "train_positive_rate": float(round(y_train.mean(), 4)),
        "test_positive_count": int(y_test.sum()),
        "test_positive_rate": float(round(y_test.mean(), 4)),
        "numerical_features_count": len(num_cols),
        "categorical_features_count": len(cat_cols),
        "total_selected_features_count": len(feature_cols),
        "include_discharge_disposition": include_discharge_disposition,
        "excluded_features": excluded_manifest,
    }

    return {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
        "train_df": train_df,
        "test_df": test_df,
        "preprocessor": preprocessor,
        "numerical_cols": num_cols,
        "categorical_cols": cat_cols,
        "feature_cols": feature_cols,
        "excluded_manifest": excluded_manifest,
        "metadata": metadata,
    }


if __name__ == "__main__":
    print("Testing src.features.preprocessing pipeline...")
    data_bundle = prepare_dataset()
    meta = data_bundle["metadata"]
    print("=" * 60)
    print("PREPROCESSING BUNDLE SUMMARY:")
    for k, v in meta.items():
        if k != "excluded_features":
            print(f"  {k}: {v}")
    print("\nExcluded Features Manifest:")
    for feat, reason in meta["excluded_features"].items():
        print(f"  - {feat}: {reason}")
    print("=" * 60)
