# Keel Health - Predictive Analytics Prototype

Healthcare predictive analytics prototype for HackFest 2026.
Keel Health assists hospitals in identifying discharged patients who may be at higher risk of 30-day readmission and prioritizing timely follow-up clinical care.

## Key Capabilities
- **Risk Scoring**: Predicts readmission likelihood based on clinical, encounter, and demographic features.
- **Explainable Factors**: Highlights key patient risk drivers to support informed clinical decisions.
- **Clinician Triage UI**: An interactive Streamlit dashboard designed for care coordinators and discharge planners.

## Data Strategy
- **Primary Data**: Historical clinical encounter dataset (e.g., standard hospital readmission benchmarks) stored under `data/raw/`.
- **Synthetic Data**: Reserved strictly for testing edge cases, automated test fixtures, and live demo sandboxing.

## Project Structure
```text
Keel-Health/
├── .gitignore
├── README.md
├── requirements.txt         # Core dependencies (Streamlit, pandas, scikit-learn, etc.)
├── configs/
│   └── config.py            # Centralized project configuration & clinical risk thresholds
├── data/
│   ├── raw/                 # Primary raw clinical encounter datasets
│   └── processed/           # Cleaned & feature-engineered datasets
├── notebooks/               # Prototyping & exploratory analysis
└── src/
    ├── __init__.py
    ├── app/                 # Streamlit clinician triage application
    ├── data/                # Data ingestion & demo/test synthetic generator routines
    ├── features/            # Clinical feature extraction & transformers
    └── models/              # Model training, inference, and saved-model handling
```
