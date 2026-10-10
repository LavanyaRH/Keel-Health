"""
Keel Health - Prototype Configuration
Centralized settings and clinical risk thresholds for the hackathon prototype.
"""

from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = BASE_DIR / "src" / "models"

# Dataset paths
RAW_DIABETIC_DATA_PATH = RAW_DATA_DIR / "diabetic_data.csv"
RAW_IDS_MAPPING_PATH = RAW_DATA_DIR / "IDS_mapping.csv"

# Clinical Risk Thresholds (Readmission probability)
HIGH_RISK_THRESHOLD = 0.70
MEDIUM_RISK_THRESHOLD = 0.40

# Default model settings
RANDOM_STATE = 42
TARGET_COL = "readmitted"
POSITIVE_TARGET_CLASS = "<30"
TEST_SIZE = 0.20

# Discharge disposition codes corresponding to expired or hospice care
# 11: Expired, 13: Hospice/home, 14: Hospice/medical facility,
# 19, 20, 21: Expired at home/facility/unknown
TERMINAL_DISCHARGE_IDS = [11, 13, 14, 19, 20, 21]

# Saved model artifacts directory
SAVED_MODELS_DIR = BASE_DIR / "models" / "saved"
