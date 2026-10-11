"""
Keel Health - Random Forest Model Training, Evaluation & Comparison Pipeline

Trains and evaluates an ensemble Random Forest classifier for early 30-day
hospital readmission risk prediction on the UCI Diabetes dataset, adhering
strictly to the existing clinical governance and preprocessing architecture.

Governance & Architectural Safeguards:
1. Strict Leakage Prevention: Evaluated on the exact same patient-grouped held-out test
   split as the Logistic Regression baseline (GroupShuffleSplit on patient_nbr, zero overlap).
2. Data Integrity: Preprocessor ColumnTransformer is fitted strictly on training data only.
   Test features are transformed out-of-fold.
3. Imbalance Handling: Leverages balanced class weighting (class_weight='balanced')
   to account for the ~11.4% positive class prevalence.
4. Non-Destructive Operation: Operates in full isolation from the baseline model,
   preserving existing saved artifacts, metrics, and Streamlit dashboard code.
5. Rigorous Comparison: Automatically loads the existing baseline metrics and produces
   a side-by-side statistical and clinical comparison artifact.
6. Research Prototype Disclaimer:
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
from sklearn.ensemble import RandomForestClassifier
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


def build_random_forest_pipeline(
    preprocessor: Any,
    n_estimators: int = 200,
    max_depth: Optional[int] = 15,
    min_samples_split: int = 20,
    min_samples_leaf: int = 10,
    max_features: str = "sqrt",
    class_weight: str = "balanced",
    random_state: int = RANDOM_STATE,
    n_jobs: int = -1,
) -> Pipeline:
    """
    Constructs an end-to-end scikit-learn Pipeline linking feature preprocessing
    and a balanced Random Forest classifier.

    Parameters:
        preprocessor: ColumnTransformer for feature transformations.
        n_estimators: Number of trees in the forest.
        max_depth: Maximum tree depth to constrain overfitting.
        min_samples_split: Minimum samples required to split an internal node.
        min_samples_leaf: Minimum samples required to be at a leaf node.
        max_features: Number of features to consider when looking for the best split.
        class_weight: Class weighting strategy for imbalanced target distribution.
        random_state: Fixed random seed for deterministic tree generation.
        n_jobs: Number of parallel CPU workers (-1 uses all available cores).

    Returns:
        Pipeline: Combined preprocessing and Random Forest classification pipeline.
    """
    classifier = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        max_features=max_features,
        class_weight=class_weight,
        random_state=random_state,
        n_jobs=n_jobs,
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
    decision_threshold: float = 0.5,
) -> Dict[str, Any]:
    """
    Evaluates model performance across clinical and statistical classification metrics.

    Parameters:
        pipeline: Fitted scikit-learn Pipeline.
        X_test: Test feature matrix.
        y_test: True binary target labels.
        decision_threshold: Cutoff on predicted positive-class probability.

    Returns:
        Dict[str, Any]: Comprehensive evaluation metrics dictionary.
    """
    y_prob = pipeline.predict_proba(X_test)[:, 1]
    y_pred = (y_prob >= decision_threshold).astype(int)

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

    # Classification report dictionary
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
        "decision_threshold": decision_threshold,
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
    top_n: int = 20,
) -> List[Dict[str, Any]]:
    """
    Extracts top features by Gini feature importance (Mean Decrease in Impurity)
    from the fitted Random Forest classifier.

    Parameters:
        pipeline: Fitted Pipeline with 'preprocessor' and 'classifier' steps.
        top_n: Number of top features to extract.

    Returns:
        List[Dict[str, Any]]: Sorted list of top feature importances.
    """
    try:
        preprocessor = pipeline.named_steps["preprocessor"]
        classifier = pipeline.named_steps["classifier"]
        feature_names = preprocessor.get_feature_names_out()
        importances = classifier.feature_importances_

        feature_df = pd.DataFrame({
            "feature": feature_names,
            "importance": importances,
        }).sort_values(by="importance", ascending=False)

        top_records = feature_df.head(top_n).to_dict(orient="records")
        return [
            {
                "feature": str(r["feature"]),
                "importance": round(float(r["importance"]), 5),
            }
            for r in top_records
        ]
    except Exception as exc:
        print(f"[Warning] Could not extract Random Forest feature importances: {exc}")
        return []


def load_baseline_artifacts(
    saved_models_dir: Path,
    include_discharge_disposition: bool = False,
) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """
    Loads the existing serialized baseline metrics and metadata from disk without
    retraining or modifying the original baseline artifacts.
    """
    metrics_filename = (
        "baseline_metrics.json"
        if not include_discharge_disposition
        else "baseline_metrics_with_discharge_disp.json"
    )
    metadata_filename = (
        "baseline_metadata.json"
        if not include_discharge_disposition
        else "baseline_metadata_with_discharge_disp.json"
    )

    metrics_path = saved_models_dir / metrics_filename
    metadata_path = saved_models_dir / metadata_filename

    baseline_metrics = None
    baseline_metadata = None

    if metrics_path.exists():
        try:
            with open(metrics_path, "r", encoding="utf-8") as f:
                baseline_metrics = json.load(f)
        except Exception as exc:
            print(f"[Warning] Could not load baseline metrics: {exc}")

    if metadata_path.exists():
        try:
            with open(metadata_path, "r", encoding="utf-8") as f:
                baseline_metadata = json.load(f)
        except Exception as exc:
            print(f"[Warning] Could not load baseline metadata: {exc}")

    return baseline_metrics, baseline_metadata


def build_comparison_summary(
    baseline_metrics: Dict[str, Any],
    rf_metrics: Dict[str, Any],
    data_meta: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Generates a structured side-by-side comparison between the baseline
    Logistic Regression model and the newly trained Random Forest model.
    """
    metric_keys = [
        ("roc_auc", "ROC-AUC (Discrimination)", True),
        ("pr_auc", "PR-AUC (Average Precision)", True),
        ("recall", "Recall / Sensitivity", True),
        ("precision", "Precision (PPV)", True),
        ("f1_score", "F1-Score (Harmonic Mean)", True),
        ("specificity", "Specificity (TNR)", True),
        ("accuracy", "Accuracy (Secondary Reference)", True),
    ]

    table: Dict[str, Any] = {}
    for key, label, higher_is_better in metric_keys:
        lr_val = float(baseline_metrics.get(key, 0.0))
        rf_val = float(rf_metrics.get(key, 0.0))
        diff = round(rf_val - lr_val, 4)
        pct_change = round((diff / lr_val) * 100, 2) if lr_val > 0 else 0.0

        if diff > 0:
            winner = "Random Forest" if higher_is_better else "Logistic Regression"
        elif diff < 0:
            winner = "Logistic Regression" if higher_is_better else "Random Forest"
        else:
            winner = "Tie"

        table[key] = {
            "label": label,
            "logistic_regression": lr_val,
            "random_forest": rf_val,
            "delta_rf_minus_lr": diff,
            "percent_change": pct_change,
            "higher_performing": winner,
        }

    # Confusion matrix comparison
    lr_cm = baseline_metrics.get("confusion_matrix", {})
    rf_cm = rf_metrics.get("confusion_matrix", {})

    cm_comparison = {
        "true_positives": {
            "logistic_regression": lr_cm.get("true_positives", 0),
            "random_forest": rf_cm.get("true_positives", 0),
            "delta": rf_cm.get("true_positives", 0) - lr_cm.get("true_positives", 0),
        },
        "false_negatives": {
            "logistic_regression": lr_cm.get("false_negatives", 0),
            "random_forest": rf_cm.get("false_negatives", 0),
            "delta": rf_cm.get("false_negatives", 0) - lr_cm.get("false_negatives", 0),
        },
        "true_negatives": {
            "logistic_regression": lr_cm.get("true_negatives", 0),
            "random_forest": rf_cm.get("true_negatives", 0),
            "delta": rf_cm.get("true_negatives", 0) - lr_cm.get("true_negatives", 0),
        },
        "false_positives": {
            "logistic_regression": lr_cm.get("false_positives", 0),
            "random_forest": rf_cm.get("false_positives", 0),
            "delta": rf_cm.get("false_positives", 0) - lr_cm.get("false_positives", 0),
        },
    }

    # Clinical trade-off analysis
    auc_diff = table["roc_auc"]["delta_rf_minus_lr"]
    rec_diff = table["recall"]["delta_rf_minus_lr"]
    prec_diff = table["precision"]["delta_rf_minus_lr"]

    synthesis = {
        "primary_ranking_winner": table["roc_auc"]["higher_performing"],
        "clinical_sensitivity_winner": table["recall"]["higher_performing"],
        "precision_winner": table["precision"]["higher_performing"],
        "interpretability_tradeoff": (
            "Logistic Regression provides direct, exact odds ratios (exp(beta_i)) and additive log-odds "
            "contributions, enabling patient-specific linear attribution in transitional care planning. "
            "Random Forest provides non-linear feature interaction modeling and tree ensemble Gini importances, "
            "but requires surrogate explanation methods (e.g. TreeSHAP) for local patient attribution."
        ),
        "clinical_summary": (
            f"Random Forest {'improved' if auc_diff >= 0 else 'decreased'} discrimination by {abs(auc_diff):.4f} ROC-AUC points "
            f"({table['roc_auc']['percent_change']:+.2f}%). "
            f"Recall was {'higher' if rec_diff >= 0 else 'lower'} by {abs(rec_diff):.4f} "
            f"({rf_cm.get('true_positives', 0):,} vs {lr_cm.get('true_positives', 0):,} true positive readmissions detected). "
            f"Precision was {'higher' if prec_diff >= 0 else 'lower'} by {abs(prec_diff):.4f}."
        ),
    }

    return {
        "comparison_timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "evaluation_protocol": {
            "dataset": "UCI Diabetes 130-US Hospitals (1999-2008)",
            "split_type": "GroupShuffleSplit (grouped by patient_nbr, zero cross-patient leakage)",
            "test_size": data_meta.get("test_size", TEST_SIZE),
            "test_encounters": data_meta.get("test_rows", 19802),
            "test_unique_patients": data_meta.get("test_unique_patients", 13998),
            "test_positive_prevalence": data_meta.get("test_positive_rate", 0.1119),
            "decision_threshold": 0.5,
        },
        "metrics_comparison": table,
        "confusion_matrix_comparison": cm_comparison,
        "synthesis": synthesis,
    }


def print_comparison_report(
    rf_metrics: Dict[str, Any],
    baseline_metrics: Dict[str, Any],
    rf_meta: Dict[str, Any],
    comparison: Dict[str, Any],
    top_features: List[Dict[str, Any]],
) -> None:
    """
    Prints a formatted, side-by-side clinical and statistical comparison report to stdout.
    """
    cm_rf = rf_metrics["confusion_matrix"]
    cm_lr = baseline_metrics.get("confusion_matrix", {})

    print("\n" + "=" * 88)
    print("KEEL HEALTH - MODEL EVALUATION & COMPARISON REPORT")
    print("Baseline Logistic Regression  vs.  Random Forest Classifier")
    print("=" * 88)
    print("NOTICE: Research prototype using historical diabetes encounters.")
    print("NOT a clinically validated medical prediction system. No clinical claims.")
    print("-" * 88)

    print("\n1. DATA SPLIT & COHORT ARCHITECTURE (Exact Same Patient-Grouped Held-Out Test Set):")
    ds_meta = rf_meta["dataset_metadata"]
    print(f"   - Total Cohort Encounters:   {ds_meta['cohort_shape'][0]:,}")
    print(f"   - Training Encounters:        {ds_meta['train_rows']:,} ({ds_meta['train_unique_patients']:,} unique patients)")
    print(f"   - Testing Encounters:         {ds_meta['test_rows']:,} ({ds_meta['test_unique_patients']:,} unique patients)")
    print(f"   - Test Readmission Rate:      {ds_meta['test_positive_rate']*100:.2f}% ({ds_meta['test_positive_count']:,} cases)")
    print(f"   - Patient Overlap:            0 (Strict GroupShuffleSplit on patient_nbr)")

    print("\n2. HEAD-TO-HEAD METRIC COMPARISON (Decision Threshold = 0.50):")
    print(f"   {'Metric':<32} {'Logistic Regression':>20} {'Random Forest':>16} {'Delta (RF - LR)':>16}")
    print("   " + "-" * 84)

    for m_key, m_info in comparison["metrics_comparison"].items():
        label = m_info["label"]
        lr_v = m_info["logistic_regression"]
        rf_v = m_info["random_forest"]
        delta = m_info["delta_rf_minus_lr"]
        pct = m_info["percent_change"]
        sign = "+" if delta > 0 else ""
        print(f"   {label:<32} {lr_v:>20.4f} {rf_v:>16.4f} {sign}{delta:>10.4f} ({sign}{pct:.1f}%)")

    print("\n3. CONFUSION MATRIX COMPARISON:")
    print(f"   {'Outcome Category':<32} {'Logistic Regression':>20} {'Random Forest':>16} {'Delta (RF - LR)':>16}")
    print("   " + "-" * 84)
    tp_lr, tp_rf = cm_lr.get("true_positives", 0), cm_rf["true_positives"]
    fn_lr, fn_rf = cm_lr.get("false_negatives", 0), cm_rf["false_negatives"]
    tn_lr, tn_rf = cm_lr.get("true_negatives", 0), cm_rf["true_negatives"]
    fp_lr, fp_rf = cm_lr.get("false_positives", 0), cm_rf["false_positives"]

    print(f"   {'True Positives (Detected)':<32} {tp_lr:>20,} {tp_rf:>16,} {tp_rf - tp_lr:>+16,}")
    print(f"   {'False Negatives (Missed)':<32} {fn_lr:>20,} {fn_rf:>16,} {fn_rf - fn_lr:>+16,}")
    print(f"   {'True Negatives (Correct Non)':<32} {tn_lr:>20,} {tn_rf:>16,} {tn_rf - tn_lr:>+16,}")
    print(f"   {'False Positives (False Alarms)':<32} {fp_lr:>20,} {fp_rf:>16,} {fp_rf - fp_lr:>+16,}")

    if top_features:
        print("\n4. TOP 10 RANDOM FOREST CLINICAL FEATURES (Mean Decrease in Impurity / Gini):")
        for idx, feat in enumerate(top_features[:10], 1):
            print(f"   {idx:>2}. {feat['feature']:<40}: {feat['importance']:.5f} ({feat['importance']*100:.2f}%)")

    print("\n5. CLINICAL & STATISTICAL SYNTHESIS:")
    synth = comparison["synthesis"]
    print(f"   - Discrimination:   {synth['clinical_summary']}")
    print(f"   - Interpretability: {synth['interpretability_tradeoff']}")
    print("=" * 88 + "\n")


def train_and_save_random_forest(
    n_estimators: int = 200,
    max_depth: Optional[int] = 15,
    min_samples_split: int = 20,
    min_samples_leaf: int = 10,
    max_features: str = "sqrt",
    class_weight: str = "balanced",
    random_state: int = RANDOM_STATE,
    n_jobs: int = -1,
    include_discharge_disposition: bool = False,
    output_dir: Optional[Path | str] = None,
) -> Dict[str, Any]:
    """
    Executes Random Forest model training, out-of-fold evaluation on the identical
    held-out patient test set, generates comparative metrics against the baseline,
    and serializes all new artifacts distinctly.

    Parameters:
        n_estimators: Number of trees.
        max_depth: Maximum tree depth.
        min_samples_split: Minimum samples to split an internal node.
        min_samples_leaf: Minimum samples required at leaf.
        max_features: Feature subset size per split.
        class_weight: Class weight strategy ('balanced').
        random_state: Reproducible seed.
        n_jobs: CPU parallel workers.
        include_discharge_disposition: Whether to include discharge_disposition_id.
        output_dir: Directory where artifacts are saved.

    Returns:
        Dict[str, Any]: Summary dictionary of training and comparison results.
    """
    save_path = Path(output_dir) if output_dir is not None else SAVED_MODELS_DIR
    save_path.mkdir(parents=True, exist_ok=True)

    # 1. Load data with identical protocol
    print(f"\n[1/5] Preparing dataset via existing clinical preprocessing pipeline...")
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

    # Integrity verification
    overlap = set(data_bundle["train_df"]["patient_nbr"]).intersection(
        set(data_bundle["test_df"]["patient_nbr"])
    )
    assert len(overlap) == 0, f"Critical leakage detected: {len(overlap)} patients in both splits!"
    assert "readmitted" not in X_train.columns, "Target column leaked in training features!"
    assert "readmitted" not in X_test.columns, "Target column leaked in test features!"

    print(f"  [OK] Zero patient leakage verified: 0 overlapping patients between train and test.")
    print(f"  [OK] Train: {len(X_train):,} encounters ({data_meta['train_unique_patients']:,} patients)")
    print(f"  [OK] Test:  {len(X_test):,} encounters ({data_meta['test_unique_patients']:,} patients)")

    # 2. Build Random Forest pipeline
    print(f"\n[2/5] Building Random Forest Pipeline with hyperparameters:")
    print(f"      n_estimators={n_estimators}, max_depth={max_depth}, min_samples_split={min_samples_split}, "
          f"min_samples_leaf={min_samples_leaf}, max_features='{max_features}', class_weight='{class_weight}'")

    pipeline = build_random_forest_pipeline(
        preprocessor=preprocessor,
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        max_features=max_features,
        class_weight=class_weight,
        random_state=random_state,
        n_jobs=n_jobs,
    )

    # 3. Fit pipeline on training encounters only
    print(f"\n[3/5] Fitting Random Forest model strictly on {len(X_train):,} training encounters...")
    pipeline.fit(X_train, y_train)
    print(f"  [OK] Model fitting completed.")

    # 4. Evaluate out-of-fold on exact held-out test encounters
    print(f"\n[4/5] Evaluating on {len(X_test):,} held-out patient encounters (threshold = 0.50)...")
    rf_metrics = evaluate_model(pipeline, X_test, y_test, decision_threshold=0.5)
    top_features = extract_top_features(pipeline, top_n=20)

    # Load baseline metrics for fair comparison
    baseline_metrics, baseline_meta = load_baseline_artifacts(
        save_path,
        include_discharge_disposition=include_discharge_disposition,
    )

    if baseline_metrics is None:
        raise FileNotFoundError(
            f"Existing baseline metrics file not found in '{save_path}'. "
            "Cannot perform comparison without existing baseline artifacts."
        )

    comparison_summary = build_comparison_summary(baseline_metrics, rf_metrics, data_meta)

    # Print comprehensive head-to-head report
    print_comparison_report(
        rf_metrics=rf_metrics,
        baseline_metrics=baseline_metrics,
        rf_meta={"dataset_metadata": data_meta},
        comparison=comparison_summary,
        top_features=top_features,
    )

    # 5. Serialize all new artifacts separately (zero overwriting of baseline files)
    print(f"[5/5] Serializing Random Forest artifacts to: {save_path}")
    timestamp_str = datetime.datetime.now(datetime.timezone.utc).isoformat()

    rf_model_filename = (
        "random_forest_model.joblib"
        if not include_discharge_disposition
        else "random_forest_model_with_discharge_disp.joblib"
    )
    rf_metrics_filename = (
        "random_forest_metrics.json"
        if not include_discharge_disposition
        else "random_forest_metrics_with_discharge_disp.json"
    )
    rf_metadata_filename = (
        "random_forest_metadata.json"
        if not include_discharge_disposition
        else "random_forest_metadata_with_discharge_disp.json"
    )
    comparison_filename = (
        "model_comparison_summary.json"
        if not include_discharge_disposition
        else "model_comparison_summary_with_discharge_disp.json"
    )

    rf_model_path = save_path / rf_model_filename
    rf_metrics_path = save_path / rf_metrics_filename
    rf_metadata_path = save_path / rf_metadata_filename
    comparison_path = save_path / comparison_filename

    # Build comprehensive metadata document (no patient-identifying data)
    rf_full_metadata = {
        "model_type": "RandomForestClassifier",
        "hyperparameters": {
            "n_estimators": n_estimators,
            "max_depth": max_depth,
            "min_samples_split": min_samples_split,
            "min_samples_leaf": min_samples_leaf,
            "max_features": max_features,
            "class_weight": class_weight,
            "random_state": random_state,
            "n_jobs": n_jobs,
        },
        "created_at_utc": timestamp_str,
        "dataset_metadata": data_meta,
        "evaluation_threshold": 0.5,
        "metrics_summary": {
            "roc_auc": rf_metrics["roc_auc"],
            "pr_auc": rf_metrics["pr_auc"],
            "precision": rf_metrics["precision"],
            "recall": rf_metrics["recall"],
            "f1_score": rf_metrics["f1_score"],
            "specificity": rf_metrics["specificity"],
            "accuracy": rf_metrics["accuracy"],
        },
        "top_feature_importances": top_features,
        "disclaimer": (
            "RESEARCH PROTOTYPE DISCLAIMER: "
            "This model is developed for algorithmic research and workflow feasibility prototyping "
            "using historical diabetes encounter records. It is NOT a clinically validated diagnostic "
            "or prognostic medical device and does NOT claim clinical effectiveness."
        ),
    }

    # Save model pipeline
    joblib.dump(pipeline, rf_model_path)
    print(f"  [Artifact] Saved model pipeline:   {rf_model_path.name}")

    # Save metrics JSON
    with open(rf_metrics_path, "w", encoding="utf-8") as f:
        json.dump(rf_metrics, f, indent=2)
    print(f"  [Artifact] Saved metrics JSON:     {rf_metrics_path.name}")

    # Save metadata JSON
    with open(rf_metadata_path, "w", encoding="utf-8") as f:
        json.dump(rf_full_metadata, f, indent=2)
    print(f"  [Artifact] Saved metadata JSON:    {rf_metadata_path.name}")

    # Save model comparison summary JSON
    with open(comparison_path, "w", encoding="utf-8") as f:
        json.dump(comparison_summary, f, indent=2)
    print(f"  [Artifact] Saved comparison JSON:  {comparison_path.name}")

    return {
        "rf_pipeline": pipeline,
        "rf_metrics": rf_metrics,
        "rf_metadata": rf_full_metadata,
        "comparison_summary": comparison_summary,
        "paths": {
            "model": str(rf_model_path),
            "metrics": str(rf_metrics_path),
            "metadata": str(rf_metadata_path),
            "comparison": str(comparison_path),
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Train, evaluate, and compare Random Forest for Keel Health readmission prediction."
    )
    parser.add_argument(
        "--n-estimators",
        type=int,
        default=200,
        help="Number of decision trees in the forest (default: 200).",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=15,
        help="Maximum tree depth to prevent overfitting (default: 15).",
    )
    parser.add_argument(
        "--min-samples-split",
        type=int,
        default=20,
        help="Minimum samples required to split an internal node (default: 20).",
    )
    parser.add_argument(
        "--min-samples-leaf",
        type=int,
        default=10,
        help="Minimum samples required to be at a leaf node (default: 10).",
    )
    parser.add_argument(
        "--max-features",
        type=str,
        default="sqrt",
        help="Number of features per split ('sqrt', 'log2', or float) (default: 'sqrt').",
    )
    parser.add_argument(
        "--class-weight",
        type=str,
        default="balanced",
        help="Class weight adjustment ('balanced' or 'balanced_subsample') (default: 'balanced').",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=RANDOM_STATE,
        help=f"Deterministic random seed (default: {RANDOM_STATE}).",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Directory to save artifacts (default: configs.config.SAVED_MODELS_DIR).",
    )
    parser.add_argument(
        "--include-discharge-disp",
        action="store_true",
        default=False,
        help="Include discharge_disposition_id in features (default: False).",
    )

    args = parser.parse_args()

    train_and_save_random_forest(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        min_samples_split=args.min_samples_split,
        min_samples_leaf=args.min_samples_leaf,
        max_features=args.max_features,
        class_weight=args.class_weight,
        random_state=args.seed,
        include_discharge_disposition=args.include_discharge_disp,
        output_dir=args.output_dir,
    )


if __name__ == "__main__":
    main()
