"""
Keel Health - Models Package

Provides baseline classifier construction, training pipelines, evaluation routines,
and artifact management for hospital readmission risk prediction.
"""

from src.models.train_model import (
    build_baseline_pipeline,
    evaluate_model,
    extract_top_features,
    print_evaluation_report,
    train_and_save_baseline,
)

__all__ = [
    "build_baseline_pipeline",
    "evaluate_model",
    "extract_top_features",
    "print_evaluation_report",
    "train_and_save_baseline",
]
