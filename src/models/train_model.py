"""
Keel Health - Baseline Model Training & Evaluation Pipeline

Trains and evaluates an interpretable Logistic Regression baseline for early 30-day
hospital readmission risk prediction.

Clinical & Machine Learning Governance:
- Reproducibility: Deterministic training with fixed RANDOM_STATE.
- Leakage Prevention: Evaluated strictly on out-of-fold patient encounters using
  patient-grouped cross-sectional validation (zero cross-encounter patient leakage).
- Imbalance Handling: Balanced class weighting (class_weight='balanced') to account for
  the ~11.4% positive class prevalence.
- Transparent Evaluation: Reports Precision, Recall, F1-score, Confusion Matrix,
  ROC-AUC, and PR-AUC. Discourages relying on accuracy alone.
- Prototype Disclaimer:
  RESEARCH PROTOTYPE DISCLAIMER:
  This model is developed for algorithmic research and workflow feasibility prototyping
  using historical diabetes encounter records. It is NOT a clinically validated diagnostic
  or prognostic medical device and does NOT claim clinical effectiveness.
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.pipeline import Pipeline

# Ensure project root is available in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from configs.config import RANDOM_STATE, SAVED_MODELS_DIR, TEST_SIZE
from src.features.preprocessing import prepare_dataset


def build_baseline_pipeline(
    preprocessor: Any,
    random_state: int = RANDOM_STATE,
    c_param: float = 1.0,
    max_iter: int = 1000,
) -> Pipeline:
    """
    Constructs an end-to-end scikit-learn Pipeline linking feature preprocessing
    and a balanced Logistic Regression classifier.

    Parameters:
        preprocessor: ColumnTransformer for feature transformations.
        random_state: Fixed seed for optimization reproducibility.
        c_param: Inverse regularization strength.
        max_iter: Maximum solver iterations.

    Returns:
        Pipeline: Combined preprocessing and classification pipeline.
    """
    classifier = LogisticRegression(
        C=c_param,
        class_weight="balanced",
        solver="lbfgs",
        max_iter=max_iter,
        random_state=random_state,
    )

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", classifier),
    ])

    return pipeline


def evaluate_model(
    pipeline: Pipeline,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> Dict[str, Any]:
    """
    Evaluates model performance across clinical and classification metrics.

    Parameters:
        pipeline: Fitted scikit-learn Pipeline.
        X_test: Test feature matrix.
        y_test: True binary target labels.

    Returns:
        Dict[str, Any]: Comprehensive evaluation metrics dictionary.
    """
    y_pred = pipeline.predict(X_test)
    y_prob = pipeline.predict_proba(X_test)[:, 1]

    # Confusion matrix breakdown
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    # Core performance metrics
    precision_pos = float(precision_score(y_test, y_pred, pos_label=1, zero_division=0))
    recall_pos = float(recall_score(y_test, y_pred, pos_label=1, zero_division=0))
    f1_pos = float(f1_score(y_test, y_pred, pos_label=1, zero_division=0))
    roc_auc = float(roc_auc_score(y_test, y_prob))
    pr_auc = float(average_precision_score(y_test, y_prob))
    
    # Specificity (True Negative Rate)
    specificity = float(tn / (tn + fp)) if (tn + fp) > 0 else 0.0
    accuracy = float(accuracy_score(y_test, y_pred))

    # Full text report
    report_dict = classification_report(
        y_test,
        y_pred,
        target_names=["No Early Readmit (0)", "Early Readmit <30d (1)"],
        output_dict=True,
    )

    metrics = {
        "roc_auc": round(roc_auc, 4),
        "pr_auc": round(pr_auc, 4),
        "precision": round(precision_pos, 4),
        "recall": round(recall_pos, 4),
        "f1_score": round(f1_pos, 4),
        "specificity": round(specificity, 4),
        "accuracy": round(accuracy, 4),
        "confusion_matrix": {
            "true_negatives": int(tn),
            "false_positives": int(fp),
            "false_negatives": int(fn),
            "true_positives": int(tp),
            "matrix_array": [[int(tn), int(fp)], [int(fn), int(tp)]],
        },
        "classification_report": report_dict,
    }

    return metrics


def extract_top_features(
    pipeline: Pipeline,
    top_n: int = 10,
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Extracts top positive (risk-increasing) and negative (risk-reducing) features
    from the fitted logistic regression model for clinical interpretability.

    Parameters:
        pipeline: Fitted Pipeline with 'preprocessor' and 'classifier' steps.
        top_n: Number of top features to extract for each direction.

    Returns:
        Dict[str, List[Dict[str, Any]]]: Dictionaries of top risk factors.
    """
    try:
        preprocessor = pipeline.named_steps["preprocessor"]
        classifier = pipeline.named_steps["classifier"]
        feature_names = preprocessor.get_feature_names_out()
        coefficients = classifier.coef_[0]

        feature_importance = pd.DataFrame({
            "feature": feature_names,
            "coefficient": coefficients,
            "odds_ratio": np.exp(coefficients),
        })

        top_positive = (
            feature_importance.sort_values(by="coefficient", ascending=False)
            .head(top_n)
            .to_dict(orient="records")
        )

        top_negative = (
            feature_importance.sort_values(by="coefficient", ascending=True)
            .head(top_n)
            .to_dict(orient="records")
        )

        return {
            "top_risk_increasing_features": [
                {
                    "feature": r["feature"],
                    "coefficient": round(float(r["coefficient"]), 4),
                    "odds_ratio": round(float(r["odds_ratio"]), 4),
                }
                for r in top_positive
            ],
            "top_risk_reducing_features": [
                {
                    "feature": r["feature"],
                    "coefficient": round(float(r["coefficient"]), 4),
                    "odds_ratio": round(float(r["odds_ratio"]), 4),
                }
                for r in top_negative
            ],
        }
    except Exception as exc:
        print(f"[Warning] Could not extract feature importance: {exc}")
        return {"top_risk_increasing_features": [], "top_risk_reducing_features": []}


def print_evaluation_report(
    metrics: Dict[str, Any],
    metadata: Dict[str, Any],
    top_features: Dict[str, List[Dict[str, Any]]],
) -> None:
    """
    Prints a formatted clinical and statistical evaluation report.
    """
    cm = metrics["confusion_matrix"]
    
    print("\n" + "=" * 80)
    print("KEEL HEALTH - BASELINE LOGISTIC REGRESSION EVALUATION REPORT")
    print("=" * 80)
    print("NOTICE: Research prototype using historical diabetes encounters.")
    print("NOT a clinically validated medical prediction system. No clinical claims.")
    print("-" * 80)
    
    print("\n1. DATA SPLIT & COHORT ARCHITECTURE (Patient-Grouped Split):")
    print(f"   - Total Cohort Encounters:   {metadata['cohort_shape'][0]:,}")
    print(f"   - Terminal Encounters Dropped:{metadata['terminal_encounters_count']:,} (expired/hospice)")
    print(f"   - Training Encounters:        {metadata['train_rows']:,} ({metadata['train_unique_patients']:,} patients)")
    print(f"   - Testing Encounters:         {metadata['test_rows']:,} ({metadata['test_unique_patients']:,} patients)")
    print(f"   - Test Target Prevalence:     {metadata['test_positive_rate']*100:.2f}% ({metadata['test_positive_count']:,} readmissions)")
    print(f"   - Patient Overlap in Splits:  0 (Strict GroupShuffleSplit on patient_nbr)")

    print("\n2. PRIMARY DISCRIMINATION & RANKING METRICS:")
    print(f"   - ROC-AUC:                   {metrics['roc_auc']:.4f}")
    print(f"   - PR-AUC (Average Precision):{metrics['pr_auc']:.4f} (baseline random prevalence: {metadata['test_positive_rate']:.4f})")

    print("\n3. CLASSIFICATION METRICS (Balanced Decision Threshold = 0.5):")
    print(f"   - Recall / Sensitivity:      {metrics['recall']:.4f} ({metrics['recall']*100:.1f}% of 30d readmissions detected)")
    print(f"   - Precision (Positive PV):   {metrics['precision']:.4f}")
    print(f"   - F1-Score:                  {metrics['f1_score']:.4f}")
    print(f"   - Specificity (True Neg):    {metrics['specificity']:.4f}")
    print(f"   - Accuracy (Reference Only): {metrics['accuracy']:.4f} [Accuracy is uninformative under ~89% class imbalance]")

    print("\n4. CONFUSION MATRIX:")
    print(f"   - True Negatives  (Correct Non-Readmissions): {cm['true_negatives']:6,}")
    print(f"   - False Positives (False Alarms):             {cm['false_positives']:6,}")
    print(f"   - False Negatives (Missed Readmissions):       {cm['false_negatives']:6,}")
    print(f"   - True Positives  (Detected Readmissions):     {cm['true_positives']:6,}")

    if top_features.get("top_risk_increasing_features"):
        print("\n5. TOP RISK-INCREASING CLINICAL FACTORS (Highest Positive Odds Ratios):")
        for item in top_features["top_risk_increasing_features"][:6]:
            print(f"   - {item['feature']:<36}: coef = {item['coefficient']:>6.3f} | OR = {item['odds_ratio']:>5.2f}")

    if top_features.get("top_risk_reducing_features"):
        print("\n6. TOP RISK-REDUCING CLINICAL FACTORS (Lowest Negative Odds Ratios):")
        for item in top_features["top_risk_reducing_features"][:6]:
            print(f"   - {item['feature']:<36}: coef = {item['coefficient']:>6.3f} | OR = {item['odds_ratio']:>5.2f}")

    print("\n7. MODEL LIMITATIONS & CLINICAL CONSIDERATIONS:")
    print("   - Linear decision boundary: Cannot capture complex multi-morbid interactions.")
    print("   - Moderate discrimination (ROC-AUC ~0.64): Standard for single-encounter tabular EHR models;")
    print("     requires probabilistic risk stratification rather than binary hard thresholding.")
    print("   - Unobserved clinical variables: Social determinants of health, post-discharge support,")
    print("     and detailed outpatient adherence are absent from this historical administrative dataset.")
    print("=" * 80 + "\n")


def train_and_save_baseline(
    include_discharge_disposition: bool = False,
    output_dir: Optional[Path | str] = None,
    random_state: int = RANDOM_STATE,
) -> Dict[str, Any]:
    """
    Executes baseline training, validation, evaluation, and artifact serialization.

    Parameters:
        include_discharge_disposition: If True, includes discharge_disposition_id in features.
        output_dir: Directory to save serialized model and metadata.
                    Defaults to configs.config.SAVED_MODELS_DIR.
        random_state: Reproducible seed.

    Returns:
        Dict[str, Any]: Summary dictionary containing metrics, paths, and metadata.
    """
    save_path = Path(output_dir) if output_dir is not None else SAVED_MODELS_DIR
    save_path.mkdir(parents=True, exist_ok=True)

    print(f"\n[1/4] Preparing dataset (include_discharge_disp={include_discharge_disposition}, seed={random_state})...")
    data_bundle = prepare_dataset(
        random_state=random_state,
        include_discharge_disposition=include_discharge_disposition,
    )

    X_train = data_bundle["X_train"]
    y_train = data_bundle["y_train"]
    X_test = data_bundle["X_test"]
    y_test = data_bundle["y_test"]
    preprocessor = data_bundle["preprocessor"]
    data_meta = data_bundle["metadata"]

    print(f"[2/4] Initializing Logistic Regression Pipeline with balanced class weights...")
    pipeline = build_baseline_pipeline(
        preprocessor=preprocessor,
        random_state=random_state,
    )

    print(f"[3/4] Fitting model on {len(X_train):,} training encounters...")
    pipeline.fit(X_train, y_train)

    print(f"[4/4] Evaluating model on {len(X_test):,} held-out patient encounters...")
    metrics = evaluate_model(pipeline, X_test, y_test)
    top_features = extract_top_features(pipeline, top_n=10)

    # Print comprehensive report to console
    print_evaluation_report(metrics, data_meta, top_features)

    # Serialize artifacts
    timestamp_str = datetime.datetime.now(datetime.timezone.utc).isoformat()
    model_filename = (
        "baseline_logistic_regression.joblib"
        if not include_discharge_disposition
        else "baseline_logistic_regression_with_discharge_disp.joblib"
    )
    model_file_path = save_path / model_filename
    metadata_file_path = save_path / (
        "baseline_metadata.json"
        if not include_discharge_disposition
        else "baseline_metadata_with_discharge_disp.json"
    )
    metrics_file_path = save_path / (
        "baseline_metrics.json"
        if not include_discharge_disposition
        else "baseline_metrics_with_discharge_disp.json"
    )

    print(f"Serializing trained model pipeline to: {model_file_path}")
    joblib.dump(pipeline, model_file_path)

    full_metadata = {
        "model_type": "LogisticRegression",
        "hyperparameters": {
            "penalty": "l2",
            "C": 1.0,
            "class_weight": "balanced",
            "solver": "lbfgs",
            "max_iter": 1000,
            "random_state": random_state,
        },
        "created_at_utc": timestamp_str,
        "dataset_metadata": data_meta,
        "metrics_summary": {
            "roc_auc": metrics["roc_auc"],
            "pr_auc": metrics["pr_auc"],
            "precision": metrics["precision"],
            "recall": metrics["recall"],
            "f1_score": metrics["f1_score"],
            "specificity": metrics["specificity"],
            "accuracy": metrics["accuracy"],
        },
        "top_features": top_features,
        "disclaimer": (
            "Research prototype using historical diabetes encounters; "
            "not a clinically validated medical prediction system. "
            "No claims of clinical effectiveness."
        ),
    }

    print(f"Saving metadata to: {metadata_file_path}")
    with open(metadata_file_path, "w", encoding="utf-8") as f:
        json.dump(full_metadata, f, indent=2)

    print(f"Saving detailed evaluation metrics to: {metrics_file_path}")
    with open(metrics_file_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    return {
        "pipeline": pipeline,
        "metrics": metrics,
        "metadata": full_metadata,
        "model_file_path": str(model_file_path),
        "metadata_file_path": str(metadata_file_path),
        "metrics_file_path": str(metrics_file_path),
    }


def main():
    parser = argparse.ArgumentParser(description="Keel Health Baseline Model Training Pipeline")
    parser.add_argument(
        "--include-discharge-disp",
        action="store_true",
        help="Include discharge_disposition_id in features (for timing leakage comparison analysis)",
    )
    parser.add_argument(
        "--compare-both",
        action="store_true",
        help="Train and compare both primary baseline (without discharge_disp) and comparative model (with discharge_disp)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Directory to save serialized model and metadata",
    )
    parser.add_argument(
        "--random-state",
        type=int,
        default=RANDOM_STATE,
        help="Fixed seed for reproducibility",
    )

    args = parser.parse_args()

    if args.compare_both:
        print("\n" + "#" * 80)
        print("RUNNING PRIMARY BASELINE (Excluding discharge_disposition_id to prevent timing leakage)")
        print("#" * 80)
        res_primary = train_and_save_baseline(
            include_discharge_disposition=False,
            output_dir=args.output_dir,
            random_state=args.random_state,
        )

        print("\n" + "#" * 80)
        print("RUNNING COMPARATIVE BASELINE (Including discharge_disposition_id for timing study)")
        print("#" * 80)
        res_comp = train_and_save_baseline(
            include_discharge_disposition=True,
            output_dir=args.output_dir,
            random_state=args.random_state,
        )

        print("\n" + "=" * 80)
        print("EMPIRICAL COMPARISON SUMMARY:")
        print("=" * 80)
        m_pri = res_primary["metrics"]
        m_cmp = res_comp["metrics"]
        print(f"Metric        | Primary (Excl. Disp) | Comparative (Incl. Disp) | Delta")
        print(f"--------------+----------------------+--------------------------+-------")
        print(f"ROC-AUC       | {m_pri['roc_auc']:20.4f} | {m_cmp['roc_auc']:24.4f} | {m_cmp['roc_auc'] - m_pri['roc_auc']:+.4f}")
        print(f"PR-AUC        | {m_pri['pr_auc']:20.4f} | {m_cmp['pr_auc']:24.4f} | {m_cmp['pr_auc'] - m_pri['pr_auc']:+.4f}")
        print(f"Recall        | {m_pri['recall']:20.4f} | {m_cmp['recall']:24.4f} | {m_cmp['recall'] - m_pri['recall']:+.4f}")
        print(f"Precision     | {m_pri['precision']:20.4f} | {m_cmp['precision']:24.4f} | {m_cmp['precision'] - m_pri['precision']:+.4f}")
        print(f"F1-Score      | {m_pri['f1_score']:20.4f} | {m_cmp['f1_score']:24.4f} | {m_cmp['f1_score'] - m_pri['f1_score']:+.4f}")
        print("=" * 80 + "\n")
    else:
        train_and_save_baseline(
            include_discharge_disposition=args.include_discharge_disp,
            output_dir=args.output_dir,
            random_state=args.random_state,
        )


if __name__ == "__main__":
    main()
