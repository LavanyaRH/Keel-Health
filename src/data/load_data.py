"""
Keel Health - Raw Data Ingestion Module

Provides loading and inspection utilities for the UCI Diabetes 130-US Hospitals dataset.
Does not perform any data modifications, preprocessing, or feature transformations.
"""

import sys
from pathlib import Path
from typing import Any, Dict, Optional
import pandas as pd

# Ensure project root is available in sys.path for seamless imports
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from configs.config import RAW_DIABETIC_DATA_PATH


def load_raw_data(filepath: Optional[Path | str] = None) -> pd.DataFrame:
    """
    Loads the raw diabetic dataset from CSV into a pandas DataFrame.

    Parameters:
        filepath: Optional custom path to the dataset CSV file.
                  Defaults to configs.config.RAW_DIABETIC_DATA_PATH.

    Returns:
        pd.DataFrame: Raw, unmodified encounter data.
    """
    target_path = Path(filepath) if filepath is not None else RAW_DIABETIC_DATA_PATH
    
    if not target_path.exists():
        raise FileNotFoundError(
            f"Dataset file not found at: {target_path}. "
            "Please ensure diabetic_data.csv is placed in data/raw/."
        )

    return pd.read_csv(target_path)


def inspect_raw_data(df: Optional[pd.DataFrame] = None) -> Dict[str, Any]:
    """
    Inspects the raw dataset and reports structural characteristics,
    column types, missing values, and the target distribution.

    Parameters:
        df: Optional existing DataFrame to inspect.
            If None, load_raw_data() will be called automatically.

    Returns:
        Dict[str, Any]: Dictionary containing shape, columns, dtypes,
                        missing value counts, and readmitted distribution.
    """
    if df is None:
        df = load_raw_data()

    shape = df.shape
    columns = list(df.columns)
    dtypes = {col: str(dtype) for col, dtype in df.dtypes.items()}
    missing_counts = df.isna().sum().to_dict()
    
    # Missing counts represented as '?' (raw UCI dataset convention)
    question_mark_counts = {
        col: int((df[col] == "?").sum())
        for col in df.columns
        if (df[col] == "?").any()
    }

    readmitted_dist = {}
    if "readmitted" in df.columns:
        readmitted_dist = df["readmitted"].value_counts().to_dict()

    summary = {
        "shape": shape,
        "num_rows": shape[0],
        "num_cols": shape[1],
        "columns": columns,
        "dtypes": dtypes,
        "missing_counts": missing_counts,
        "missing_question_mark_counts": question_mark_counts,
        "readmitted_distribution": readmitted_dist,
    }

    print("=" * 60)
    print("KEEL HEALTH - RAW DATASET INSPECTION REPORT")
    print("=" * 60)
    print(f"Dataset Shape: {shape[0]:,} rows x {shape[1]} columns\n")
    
    print("Target Column ('readmitted') Distribution:")
    for label, count in readmitted_dist.items():
        pct = (count / shape[0]) * 100
        print(f"  - {label:>5}: {count:7,} ({pct:5.2f}%)")
    
    print(f"\nTotal Columns: {len(columns)}")
    print(f"Standard NaN/Null Columns with missing values: {sum(1 for v in missing_counts.values() if v > 0)}")
    print(f"Columns with '?' placeholder values: {len(question_mark_counts)}")
    if question_mark_counts:
        for col, count in sorted(question_mark_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
            pct = (count / shape[0]) * 100
            print(f"  - {col}: {count:,} ({pct:.2f}%)")
    print("=" * 60)

    return summary


if __name__ == "__main__":
    inspect_raw_data()
