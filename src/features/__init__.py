"""
Keel Health - Features Package

Provides clinical feature engineering, categorical standardization, ICD-9 grouping,
and patient-grouped cohort preparation pipelines.
"""

from src.features.preprocessing import (
    CategoricalStandardizer,
    ICD9Categorizer,
    build_preprocessor,
    create_binary_target,
    filter_modeling_cohort,
    get_feature_manifest,
    patient_grouped_split,
    prepare_dataset,
)

__all__ = [
    "ICD9Categorizer",
    "CategoricalStandardizer",
    "filter_modeling_cohort",
    "create_binary_target",
    "get_feature_manifest",
    "patient_grouped_split",
    "build_preprocessor",
    "prepare_dataset",
]
