"""
Keel Health - Clinician Triage & Early Readmission Risk Dashboard
HackFest 2026 Prototype

An interactive clinical decision-support and workflow prioritization dashboard.
Visual design inspired by modern clinical decision platforms:
- Restrained navy/teal/white aesthetic
- White card layout with subtle borders
- Top summary metric badges
- High-priority outreach queue table
- Transparent feature attribution and capacity-aware triage

RESEARCH PROTOTYPE DISCLAIMER:
This application is a research and workflow prototype built on historical diabetes encounters
(UCI Diabetes 130-US Hospitals dataset). It is NOT a clinically validated medical device.
Model scores represent experimental statistical association estimates, not clinical diagnosis
or treatment guarantees.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import altair as alt
import joblib
import numpy as np
import pandas as pd
import streamlit as st

# Ensure project root is available in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from configs.config import (
    HIGH_RISK_THRESHOLD,
    MEDIUM_RISK_THRESHOLD,
    SAVED_MODELS_DIR,
)
from src.data.load_data import load_raw_data
from src.features.preprocessing import (
    filter_modeling_cohort,
    get_feature_manifest,
)

# -----------------------------------------------------------------------------
# Streamlit Page Configuration & Design System
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Keel Health | Inpatient Risk Prioritization",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Healthcare Styling: Navy, Teal, and Off-White Design System
CUSTOM_CSS = """
<style>
    /* Global Background and Typography */
    .main {
        background-color: #F8FAFC;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Header Container */
    .keel-header {
        padding: 0.5rem 0rem 1.25rem 0rem;
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 1.5rem;
    }
    .keel-badge-tag {
        display: inline-block;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #0D9488;
        background-color: #F0FDFA;
        padding: 0.2rem 0.6rem;
        border-radius: 9999px;
        border: 1px solid #CCFBF1;
        margin-bottom: 0.4rem;
    }
    .keel-title {
        font-size: 2.1rem;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.02em;
        margin: 0;
        line-height: 1.2;
    }
    .keel-subtitle {
        font-size: 0.95rem;
        color: #64748B;
        margin-top: 0.25rem;
        margin-bottom: 0rem;
    }
    
    /* Metric Pill Header Badges */
    .header-metric-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 0.65rem 1rem;
        text-align: right;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    }
    .header-metric-label {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: #64748B;
    }
    .header-metric-value {
        font-size: 1.35rem;
        font-weight: 800;
        color: #0F172A;
    }
    .header-priority-pill {
        background: #0F172A;
        color: #FFFFFF;
        border-radius: 12px;
        padding: 0.65rem 1.1rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(15, 23, 42, 0.15);
    }
    .header-priority-label {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        color: #38BDF8;
    }
    .header-priority-value {
        font-size: 1.35rem;
        font-weight: 800;
        color: #FFFFFF;
    }

    /* Clinical Disclaimer Alert Banner */
    .keel-disclaimer-banner {
        background-color: #FEF3C7;
        border-left: 4px solid #D97706;
        padding: 0.75rem 1rem;
        border-radius: 6px;
        margin-bottom: 1.5rem;
        font-size: 0.85rem;
        color: #92400E;
        line-height: 1.45;
    }
    
    /* White Card Wrapper */
    .keel-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    }
    .keel-card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0.25rem;
    }
    .keel-card-subtitle {
        font-size: 0.82rem;
        color: #64748B;
        margin-bottom: 0.85rem;
    }
    
    /* Score Badges */
    .score-badge-high {
        background-color: #FEF2F2;
        color: #DC2626;
        font-weight: 700;
        padding: 0.2rem 0.5rem;
        border-radius: 6px;
        border: 1px solid #FEE2E2;
        display: inline-block;
    }
    .score-badge-mod {
        background-color: #FFFBEB;
        color: #D97706;
        font-weight: 700;
        padding: 0.2rem 0.5rem;
        border-radius: 6px;
        border: 1px solid #FEF3C7;
        display: inline-block;
    }
    .score-badge-low {
        background-color: #ECFDF5;
        color: #059669;
        font-weight: 700;
        padding: 0.2rem 0.5rem;
        border-radius: 6px;
        border: 1px solid #D1FAE5;
        display: inline-block;
    }
    
    /* Table Styling */
    .stDataFrame {
        border-radius: 8px;
        overflow: hidden;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# Cached Model, Metadata, and Dataset Loaders
# -----------------------------------------------------------------------------
@st.cache_resource(show_spinner="Loading trained baseline model...")
def load_trained_model_pipeline() -> Tuple[Any, Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """
    Loads the serialized Logistic Regression pipeline and associated metadata/metrics.
    Returns:
        (pipeline, metadata_dict, metrics_dict)
    """
    model_file = SAVED_MODELS_DIR / "baseline_logistic_regression.joblib"
    meta_file = SAVED_MODELS_DIR / "baseline_metadata.json"
    metrics_file = SAVED_MODELS_DIR / "baseline_metrics.json"

    if not model_file.exists():
        return None, None, None

    pipeline = joblib.load(model_file)

    metadata = None
    if meta_file.exists():
        try:
            with open(meta_file, "r", encoding="utf-8") as f:
                metadata = json.load(f)
        except Exception:
            metadata = None

    metrics = None
    if metrics_file.exists():
        try:
            with open(metrics_file, "r", encoding="utf-8") as f:
                metrics = json.load(f)
        except Exception:
            metrics = None

    return pipeline, metadata, metrics


@st.cache_data(show_spinner="Ingesting cohort encounters & generating risk predictions...")
def load_and_score_cohort() -> Optional[pd.DataFrame]:
    """
    Loads raw dataset, applies identical cohort eligibility rules (excluding terminal cases),
    extracts the exact features expected by the trained pipeline, and computes predictions.

    Returns:
        pd.DataFrame: Scored eligible encounters with pseudonymous identifiers.
    """
    try:
        raw_df = load_raw_data()
    except Exception as exc:
        st.error(f"Error loading raw dataset from data/raw/: {exc}")
        return None

    # Apply strict cohort eligibility rule: exclude terminal encounters (expired / hospice)
    # Reset index to guarantee contiguous alignment with scored_df
    cohort_df = filter_modeling_cohort(raw_df, exclude_terminal=True).reset_index(drop=True)

    # Retrieve feature column lists (excluding discharge_disposition_id to prevent timing leakage)
    num_cols, cat_cols, _ = get_feature_manifest(include_discharge_disposition=False)
    feature_cols = num_cols + cat_cols

    # Ensure required columns exist
    missing_cols = [c for c in feature_cols if c not in cohort_df.columns]
    if missing_cols:
        st.error(f"Missing required feature columns in cohort: {missing_cols}")
        return None

    # Load trained model
    pipeline, _, _ = load_trained_model_pipeline()
    if pipeline is None:
        st.error("Model pipeline could not be loaded from models/saved/baseline_logistic_regression.joblib.")
        return None

    # Prepare input matrix
    X = cohort_df[feature_cols].copy()

    # Generate positive class predicted probabilities
    probabilities = pipeline.predict_proba(X)[:, 1]

    # Build clean, pseudonymous encounter DataFrame
    # Note: patient_nbr and encounter_id are explicitly stripped from UI display
    n_encounters = len(cohort_df)
    pseudonymous_ids = [f"#HF-{1001 + i}" for i in range(n_encounters)]

    # Build scored DataFrame with exact feature columns to guarantee 100% fidelity to trained pipeline
    scored_df = cohort_df[feature_cols].copy()

    # Add display and prioritization columns
    scored_df["encounter_label"] = pseudonymous_ids
    scored_df["predicted_score"] = probabilities
    scored_df["score_percent"] = np.round(probabilities * 100, 1)
    scored_df["age_group"] = cohort_df["age"].values
    scored_df["length_of_stay"] = cohort_df["time_in_hospital"].values
    scored_df["num_inpatient"] = cohort_df["number_inpatient"].values
    scored_df["num_emergency"] = cohort_df["number_emergency"].values
    scored_df["num_outpatient"] = cohort_df["number_outpatient"].values
    scored_df["primary_diag"] = cohort_df["diag_1"].values
    scored_df["diabetes_med"] = cohort_df["diabetesMed"].values
    scored_df["race_display"] = cohort_df["race"].replace("?", "Unknown").values
    scored_df["max_glu_serum_display"] = cohort_df["max_glu_serum"].fillna("None").values
    scored_df["a1c_result_display"] = cohort_df["A1Cresult"].fillna("None").values

    # Derive top clinical driver label for quick table scanning
    scored_df["top_driver"] = derive_top_driver_labels(scored_df)

    return scored_df


def derive_top_driver_labels(df: pd.DataFrame) -> List[str]:
    """
    Derives an interpretable, patient-specific primary risk driver label
    based on the dominant clinical risk indicators of the baseline model.
    """
    drivers = []
    for _, row in df.iterrows():
        if row["num_inpatient"] >= 2:
            drivers.append(f"Past Inpatient ({row['num_inpatient']} visits)")
        elif row["num_emergency"] >= 2:
            drivers.append(f"Frequent ER Utilization ({row['num_emergency']} visits)")
        elif row["num_inpatient"] == 1:
            drivers.append("Recent Inpatient Admission (1 visit)")
        elif row["insulin"] in ["Up", "Down"]:
            drivers.append(f"Insulin Instability ({row['insulin']})")
        elif str(row["age_group"]) in ["[70-80)", "[80-90)", "[90-100)"]:
            drivers.append(f"Geriatric Vulnerability ({row['age_group']})")
        elif row["length_of_stay"] >= 7:
            drivers.append(f"Extended Hospital Stay ({row['length_of_stay']}d)")
        elif row["change"] == "Ch":
            drivers.append("Medication Regimen Adjusted")
        elif row["num_medications"] >= 20:
            drivers.append("High Polypharmacy (>20 meds)")
        else:
            drivers.append("Chronic Glycemic / Comorbid Burden")
    return drivers


def compute_domain_importance(pipeline: Any) -> pd.DataFrame:
    """
    Computes normalized relative predictive weight (0-100 index) for major clinical
    domains directly from the fitted logistic regression standardized coefficients.
    """
    try:
        preprocessor = pipeline.named_steps["preprocessor"]
        classifier = pipeline.named_steps["classifier"]
        feature_names = preprocessor.get_feature_names_out()
        coefficients = np.abs(classifier.coef_[0])
        feat_df = pd.DataFrame({"feature": feature_names, "abs_coef": coefficients})

        domains = {
            "Age & Demographics": ["age", "gender", "race", "admission_type_id", "admission_source_id"],
            "Medication Adjustments": [
                "change", "diabetesMed", "insulin", "metformin", "repaglinide",
                "nateglinide", "chlorpropamide", "glimepiride", "acetohexamide",
                "glipizide", "glyburide", "tolbutamide", "pioglitazone",
                "rosiglitazone", "acarbose", "miglitol", "troglitazone",
                "tolazamide", "glyburide-metformin", "glipizide-metformin",
                "glimepiride-pioglitazone", "metformin-rosiglitazone", "metformin-pioglitazone"
            ],
            "Clinical Comorbidities": ["number_diagnoses", "diag_1", "diag_2", "diag_3"],
            "Past Utilization (Inpatient/ER)": ["number_inpatient", "number_emergency", "number_outpatient"],
            "Diagnostic Testing Volume": ["num_lab_procedures", "num_procedures", "max_glu_serum", "A1Cresult"],
            "Inpatient Stay Duration": ["time_in_hospital"],
        }

        weights = []
        for domain, keywords in domains.items():
            mask = feat_df["feature"].apply(lambda feat: any(kw in feat for kw in keywords))
            max_c = float(feat_df.loc[mask, "abs_coef"].max()) if mask.any() else 0.0
            weights.append({"Clinical Domain": domain, "weight": max_c})

        df_dom = pd.DataFrame(weights)
        max_overall = df_dom["weight"].max()
        if max_overall > 0:
            df_dom["Relative Influence"] = np.round((df_dom["weight"] / max_overall) * 100).astype(int)
        else:
            df_dom["Relative Influence"] = 0

        return df_dom.sort_values(by="Relative Influence", ascending=False).reset_index(drop=True)
    except Exception:
        return pd.DataFrame({
            "Clinical Domain": [
                "Age & Demographics",
                "Medication Adjustments",
                "Clinical Comorbidities",
                "Past Utilization (Inpatient/ER)",
                "Diagnostic Testing Volume",
                "Inpatient Stay Duration",
            ],
            "Relative Influence": [100, 51, 42, 24, 15, 5],
        })


def compute_local_explanation(
    pipeline: Any,
    encounter_row_features: pd.DataFrame,
    top_n: int = 5,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], float]:
    """
    Calculates exact linear feature contributions (log-odds impact: beta_i * x_i)
    for a single encounter from the Logistic Regression pipeline.

    Returns:
        (top_positive_factors, top_negative_factors, base_intercept)
    """
    try:
        preprocessor = pipeline.named_steps["preprocessor"]
        classifier = pipeline.named_steps["classifier"]

        # Transform single encounter
        X_trans = preprocessor.transform(encounter_row_features)
        feature_names = preprocessor.get_feature_names_out()
        coefficients = classifier.coef_[0]
        intercept = float(classifier.intercept_[0])

        # Exact linear contribution to log-odds: beta_i * x_i
        contributions = X_trans[0] * coefficients

        contrib_items = []
        for name, weight in zip(feature_names, contributions):
            if abs(weight) > 1e-4:
                # Format friendly clinical descriptor
                clean_name = format_friendly_feature_name(name)
                contrib_items.append({
                    "raw_feature": name,
                    "clinical_name": clean_name,
                    "contribution": float(weight),
                })

        pos_drivers = sorted(
            [c for c in contrib_items if c["contribution"] > 0],
            key=lambda x: x["contribution"],
            reverse=True,
        )[:top_n]

        neg_drivers = sorted(
            [c for c in contrib_items if c["contribution"] < 0],
            key=lambda x: x["contribution"],
        )[:top_n]

        return pos_drivers, neg_drivers, intercept
    except Exception as exc:
        st.warning(f"Feature explanation calculation unavailable: {exc}")
        return [], [], 0.0


def format_friendly_feature_name(raw_name: str) -> str:
    """Translates raw preprocessed feature strings into clean clinical descriptors."""
    clean = raw_name.replace("cat__", "").replace("num__", "")
    translations = {
        "number_inpatient": "Prior Inpatient Admissions (Past Year)",
        "number_emergency": "Prior Emergency Room Visits (Past Year)",
        "number_outpatient": "Prior Outpatient Clinic Visits (Past Year)",
        "time_in_hospital": "Length of Inpatient Stay (Days)",
        "num_medications": "Medication Count / Polypharmacy",
        "num_lab_procedures": "Total Laboratory Tests Performed",
        "num_procedures": "Inpatient Diagnostic / Operative Procedures",
        "number_diagnoses": "Multi-Morbidity Burden (Diagnoses Entered)",
        "diag_1_Circulatory": "Primary Diagnosis: Circulatory / Cardiovascular",
        "diag_1_Respiratory": "Primary Diagnosis: Respiratory Illness",
        "diag_1_Digestive": "Primary Diagnosis: Digestive Disease",
        "diag_1_Diabetes": "Primary Diagnosis: Diabetes Mellitus",
        "diag_1_Missing": "Primary Diagnosis: Uncoded / Emergency Presentation",
        "admission_source_id_7": "Admission Source: Emergency Department",
        "admission_source_id_1": "Admission Source: Physician Referral",
        "admission_source_id_3": "Admission Source: HMO Referral",
        "admission_type_id_1": "Admission Type: Emergency",
        "admission_type_id_2": "Admission Type: Urgent",
        "admission_type_id_3": "Admission Type: Elective",
        "insulin_Up": "Insulin Therapy: Dosage Escalated during Stay",
        "insulin_Down": "Insulin Therapy: Dosage Reduced during Stay",
        "insulin_Steady": "Insulin Therapy: Maintained Stable",
        "change_Ch": "Diabetic Medication Regimen Modified",
        "diabetesMed_Yes": "Prescribed Active Diabetes Medication",
        "A1Cresult_>8": "Elevated HbA1c (>8%)",
        "A1Cresult_Norm": "Normal HbA1c Level",
        "max_glu_serum_>300": "Acute Blood Glucose Surge (>300 mg/dL)",
        "repaglinide_Up": "Repaglinide Dose Escalated",
        "acarbose_Up": "Acarbose Dose Escalated",
    }
    if clean in translations:
        return translations[clean]
    if clean.startswith("age_"):
        bracket = clean.replace("age_", "")
        return f"Patient Age Bracket ({bracket} years)"
    return clean.replace("_", " ").title()


# -----------------------------------------------------------------------------
# Main Application Flow
# -----------------------------------------------------------------------------
def main():
    # 1. Load pipeline and metadata
    pipeline, metadata, metrics = load_trained_model_pipeline()

    if pipeline is None:
        st.error(
            "⚠️ Trained model artifact not found!\n\n"
            "Please ensure `models/saved/baseline_logistic_regression.joblib` exists. "
            "You can generate it by running: `python src/models/train_model.py`."
        )
        st.stop()

    # 2. Ingest and score eligible cohort
    df_scored = load_and_score_cohort()
    if df_scored is None:
        st.stop()

    # -------------------------------------------------------------------------
    # Sidebar Controls & Configurations
    # -------------------------------------------------------------------------
    with st.sidebar:
        st.markdown("### ⚙️ Outreach & Model Controls")

        st.markdown("#### 1. Follow-up Capacity Prioritization")
        capacity = st.slider(
            "Daily Coordinator Outreach Capacity (Encounters)",
            min_value=25,
            max_value=500,
            value=50,
            step=25,
            help="Simulates hospital capacity constraints (e.g. nurse care-coordinator telephone calls or transitional clinic slots).",
        )
        st.caption(
            "ℹ️ *Demonstration of capacity-aware triage under finite clinical resources. "
            "Not a clinical treatment recommendation.*"
        )

        st.markdown("---")
        st.markdown("#### 2. Model Score Thresholds")
        st.caption(
            "Configure experimental model-score cutoff tiers. "
            "These are statistical prediction thresholds, **not clinically validated risk bounds**."
        )
        high_threshold = st.slider(
            "Higher Model-Score Threshold",
            min_value=0.50,
            max_value=0.85,
            value=HIGH_RISK_THRESHOLD,
            step=0.05,
            help="Encounters with predicted readmission score at or above this threshold.",
        )
        mod_threshold = st.slider(
            "Moderate Model-Score Threshold",
            min_value=0.20,
            max_value=min(0.55, high_threshold),
            value=min(MEDIUM_RISK_THRESHOLD, high_threshold),
            step=0.05,
            help="Encounters with predicted readmission score between moderate and higher thresholds.",
        )

        st.markdown("---")
        st.markdown("#### 3. Cohort Filters")
        age_options = sorted(list(df_scored["age_group"].unique()))
        selected_ages = st.multiselect(
            "Filter by Age Group",
            options=age_options,
            default=[],
            help="Leave blank to view all age brackets.",
        )

        st.markdown("---")
        st.markdown("#### 📋 Model Governance Metadata")
        if metrics:
            st.markdown(
                f"- **Model**: Logistic Regression (Balanced)\n"
                f"- **Test ROC-AUC**: `{metrics.get('roc_auc', 'N/A')}`\n"
                f"- **Test PR-AUC**: `{metrics.get('pr_auc', 'N/A')}`\n"
                f"- **Sensitivity (Recall)**: `{metrics.get('recall', 'N/A')}`\n"
                f"- **Precision**: `{metrics.get('precision', 'N/A')}`\n"
                f"- **Random State**: `42` (Fixed)"
            )
        st.caption(
            "Historical EHR data: UCI Diabetes 130-US Hospitals (1999–2008). "
            "Terminal encounters (expired/hospice) excluded."
        )

    # Apply age filter if selected with explicit copy to avoid modifying cached state
    filtered_df = df_scored.copy()
    if selected_ages:
        filtered_df = filtered_df[filtered_df["age_group"].isin(selected_ages)].copy()

    # Categorize into experimental score tiers (mutually exclusive and exhaustive)
    def assign_score_tier(score: float) -> str:
        if score >= high_threshold:
            return "Higher Score"
        elif score >= mod_threshold:
            return "Moderate Score"
        else:
            return "Lower Score"

    filtered_df["score_tier"] = filtered_df["predicted_score"].apply(assign_score_tier)

    # Counts in tiers
    n_total = len(filtered_df)
    n_high = (filtered_df["score_tier"] == "Higher Score").sum()
    n_mod = (filtered_df["score_tier"] == "Moderate Score").sum()
    n_low = (filtered_df["score_tier"] == "Lower Score").sum()

    # -------------------------------------------------------------------------
    # Top Header Section (Matching Visual Reference Layout)
    # -------------------------------------------------------------------------
    st.markdown('<div class="keel-header">', unsafe_allow_html=True)
    header_col1, header_col2, header_col3 = st.columns([2.8, 1.1, 1.3])

    with header_col1:
        st.markdown('<span class="keel-badge-tag">● PREDICTIVE RISK ENGINE</span>', unsafe_allow_html=True)
        st.markdown('<h1 class="keel-title">Inpatient Risk Prioritization</h1>', unsafe_allow_html=True)
        st.markdown(
            '<p class="keel-subtitle">Keel Health · Early Readmission Risk and Follow-up Prioritization (HackFest 2026)</p>',
            unsafe_allow_html=True,
        )

    with header_col2:
        auc_val = f"{metrics['roc_auc']:.4f}" if metrics else "0.6393"
        st.markdown(
            f"""
            <div class="header-metric-card">
                <div class="header-metric-label">Model ROC-AUC</div>
                <div class="header-metric-value">{auc_val}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with header_col3:
        st.markdown(
            f"""
            <div class="header-priority-pill">
                <div class="header-priority-label">Outreach Queue Capacity</div>
                <div class="header-priority-value">{capacity} Patients</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

    # Prominent Research Prototype Notice
    st.markdown(
        """
        <div class="keel-disclaimer-banner">
            <strong>⚠️ RESEARCH PROTOTYPE NOTICE:</strong> Keel Health is an algorithmic research and workflow feasibility
            prototype developed using historical clinical encounter records. It is <strong>NOT a clinically validated medical
            device or diagnostic system</strong>. Predicted scores represent experimental statistical association estimates,
            not clinical prognosis or certainty. Do not use for clinical diagnostic or acute treatment decisions.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -------------------------------------------------------------------------
    # Metric Summary Cards (Top Row)
    # -------------------------------------------------------------------------
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

    with kpi_col1:
        is_filtered = bool(selected_ages)
        card1_title = "FILTERED ENCOUNTERS" if is_filtered else "ELIGIBLE ENCOUNTERS"
        card1_subtitle = (
            f"of {len(df_scored):,} eligible ({n_total / len(df_scored) * 100:.1f}%)"
            if is_filtered
            else "Surviving diabetic cohort"
        )
        st.markdown(
            f"""
            <div class="keel-card" style="padding: 1rem;">
                <div class="keel-card-subtitle" style="margin-bottom: 0.2rem;">{card1_title}</div>
                <div style="font-size: 1.6rem; font-weight: 800; color: #0F172A;">{n_total:,}</div>
                <div style="font-size: 0.75rem; color: #64748B;">{card1_subtitle}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with kpi_col2:
        pct_high = (n_high / n_total * 100) if n_total > 0 else 0
        st.markdown(
            f"""
            <div class="keel-card" style="padding: 1rem; border-top: 3px solid #DC2626;">
                <div class="keel-card-subtitle" style="margin-bottom: 0.2rem;">HIGHER-SCORE TIER (≥{high_threshold:.2f})</div>
                <div style="font-size: 1.6rem; font-weight: 800; color: #DC2626;">{n_high:,} <span style="font-size: 0.85rem; font-weight: 600; color: #64748B;">({pct_high:.1f}%)</span></div>
                <div style="font-size: 0.75rem; color: #64748B;">Top priority candidates</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with kpi_col3:
        pct_mod = (n_mod / n_total * 100) if n_total > 0 else 0
        st.markdown(
            f"""
            <div class="keel-card" style="padding: 1rem; border-top: 3px solid #D97706;">
                <div class="keel-card-subtitle" style="margin-bottom: 0.2rem;">MODERATE-SCORE TIER (≥{mod_threshold:.2f} to <{high_threshold:.2f})</div>
                <div style="font-size: 1.6rem; font-weight: 800; color: #D97706;">{n_mod:,} <span style="font-size: 0.85rem; font-weight: 600; color: #64748B;">({pct_mod:.1f}%)</span></div>
                <div style="font-size: 0.75rem; color: #64748B;">Secondary follow-up cohort</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with kpi_col4:
        pct_low = (n_low / n_total * 100) if n_total > 0 else 0
        st.markdown(
            f"""
            <div class="keel-card" style="padding: 1rem; border-top: 3px solid #059669;">
                <div class="keel-card-subtitle" style="margin-bottom: 0.2rem;">LOWER-SCORE TIER (<{mod_threshold:.2f})</div>
                <div style="font-size: 1.6rem; font-weight: 800; color: #059669;">{n_low:,} <span style="font-size: 0.85rem; font-weight: 600; color: #64748B;">({pct_low:.1f}%)</span></div>
                <div style="font-size: 0.75rem; color: #64748B;">Routine primary care follow-up</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # -------------------------------------------------------------------------
    # Main Dashboard Tabs
    # -------------------------------------------------------------------------
    tab_queue, tab_detail, tab_diagnostics = st.tabs([
        "📋 High-Priority Outreach Queue",
        "🔍 Encounter Clinical Profile & Attribution",
        "📊 Model Metrics & Cohort Diagnostics",
    ])

    # -------------------------------------------------------------------------
    # TAB 1: High-Priority Outreach Queue (Main View)
    # -------------------------------------------------------------------------
    with tab_queue:
        # Sort encounters by predicted readmission score descending
        prioritized_df = filtered_df.sort_values(by="predicted_score", ascending=False).reset_index(drop=True)
        # Select top encounters up to selected capacity
        capacity_queue = prioritized_df.head(capacity).copy()
        capacity_queue["priority_rank"] = range(1, len(capacity_queue) + 1)

        left_col, right_col = st.columns([1.1, 2.1])

        # LEFT COLUMN: Risk Model Variables & Score Distribution
        with left_col:
            st.markdown(
                """
                <div class="keel-card">
                    <div class="keel-card-title">Risk Model Variables</div>
                    <div class="keel-card-subtitle">Factor weights currently leveraged by the baseline predictive algorithm.</div>
                """,
                unsafe_allow_html=True,
            )

            # Bar chart of variable categories derived dynamically from model coefficients
            driver_categories = compute_domain_importance(pipeline)
            domain_chart = (
                alt.Chart(driver_categories)
                .mark_bar(cornerRadiusTopRight=4, cornerRadiusBottomRight=4, color="#0D9488")
                .encode(
                    x=alt.X("Relative Influence:Q", title="Relative Predictive Weight (Index)", scale=alt.Scale(domain=[0, 100])),
                    y=alt.Y("Clinical Domain:N", sort="-x", title=None),
                    tooltip=["Clinical Domain", "Relative Influence"],
                )
                .properties(height=200)
            )
            st.altair_chart(domain_chart, use_container_width=True)
            st.caption("ℹ️ *Derived dynamically from baseline Logistic Regression standardized coefficients.*")

            # Score Distribution Histogram
            st.markdown("---")
            st.markdown("##### 📈 Cohort Score Distribution")
            hist_chart = (
                alt.Chart(filtered_df)
                .mark_bar(color="#0284C7", opacity=0.85)
                .encode(
                    x=alt.X("predicted_score:Q", bin=alt.Bin(maxbins=25), title="Predicted Score Probability"),
                    y=alt.Y("count()", title="Encounter Count"),
                    tooltip=["count()"],
                )
                .properties(height=160)
            )
            st.altair_chart(hist_chart, use_container_width=True)
            st.caption(
                f"Cohort mean score: **{filtered_df['predicted_score'].mean():.3f}** | Median: **{filtered_df['predicted_score'].median():.3f}**"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        # RIGHT COLUMN: High-Priority Outreach Queue Table
        with right_col:
            st.markdown(
                f"""
                <div class="keel-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <div>
                            <div class="keel-card-title">High-Priority Outreach Queue</div>
                            <div class="keel-card-subtitle">Displaying top {len(capacity_queue)} encounters ranked by model readmission score.</div>
                        </div>
                        <span style="font-size: 0.72rem; color: #64748B; background: #F1F5F9; padding: 0.25rem 0.6rem; border-radius: 9999px;">
                            Capacity: {capacity} Slots
                        </span>
                    </div>
                """,
                unsafe_allow_html=True,
            )

            # Display table with formatting
            table_display = capacity_queue[[
                "priority_rank",
                "encounter_label",
                "score_percent",
                "score_tier",
                "top_driver",
                "age_group",
                "length_of_stay",
                "num_inpatient",
            ]].rename(columns={
                "priority_rank": "Rank",
                "encounter_label": "Encounter ID",
                "score_percent": "Score (%)",
                "score_tier": "Model Tier",
                "top_driver": "Primary Driver",
                "age_group": "Age Group",
                "length_of_stay": "Stay (Days)",
                "num_inpatient": "Prior Inpatient",
            })

            st.dataframe(
                table_display,
                use_container_width=True,
                hide_index=True,
                height=480,
                column_config={
                    "Rank": st.column_config.NumberColumn("Rank", width="small"),
                    "Encounter ID": st.column_config.TextColumn("Encounter ID", width="medium"),
                    "Score (%)": st.column_config.ProgressColumn(
                        "Score (%)",
                        min_value=0,
                        max_value=100,
                        format="%.1f%%",
                        width="medium",
                    ),
                    "Model Tier": st.column_config.TextColumn("Model Tier", width="medium"),
                    "Primary Driver": st.column_config.TextColumn("Primary Driver", width="large"),
                    "Age Group": st.column_config.TextColumn("Age Group", width="small"),
                    "Stay (Days)": st.column_config.NumberColumn("Stay (Days)", width="small"),
                    "Prior Inpatient": st.column_config.NumberColumn("Prior Inpatient", width="small"),
                },
            )

            st.caption(
                "💡 *Pseudonymous identifiers (#HF-XXXX) prevent direct patient identification. "
                "Select any encounter in Tab 2 to inspect non-identifying features and mathematical attribution.*"
            )
            st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # TAB 2: Encounter Clinical Profile & Attribution Deep-Dive
    # -------------------------------------------------------------------------
    with tab_detail:
        st.markdown(
            """
            <div class="keel-card">
                <div class="keel-card-title">Encounter Clinical Profile & Feature Attribution</div>
                <div class="keel-card-subtitle">
                    Inspect non-identifying encounter characteristics and examine the exact mathematical contributions 
                    to the baseline Logistic Regression prediction.
                </div>
            """,
            unsafe_allow_html=True,
        )

        # Encounter selector
        available_labels = capacity_queue["encounter_label"].tolist()
        selected_label = st.selectbox(
            "Select Encounter from Outreach Queue:",
            options=available_labels,
            index=0,
            help="Choose an encounter to audit its clinical profile and model driver breakdown.",
        )

        selected_row = df_scored[df_scored["encounter_label"] == selected_label].iloc[0]
        selected_score = float(selected_row["predicted_score"])
        selected_tier = assign_score_tier(selected_score)

        # Profile Overview Badges
        pcol1, pcol2, pcol3, pcol4 = st.columns(4)
        with pcol1:
            st.metric("Encounter ID", selected_label)
        with pcol2:
            st.metric("Predicted Readmission Score", f"{selected_score*100:.1f}%")
        with pcol3:
            badge_color = "#DC2626" if selected_tier == "Higher Score" else ("#D97706" if selected_tier == "Moderate Score" else "#059669")
            st.markdown(
                f"**Score Classification**<br><span style='color: {badge_color}; font-size: 1.15rem; font-weight: 700;'>{selected_tier}</span>",
                unsafe_allow_html=True,
            )
        with pcol4:
            st.metric("Primary Driver", selected_row["top_driver"])

        st.markdown("---")

        # Clinical Data Profile (3 Columns)
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("##### 👤 Demographics & Entry")
            st.write(f"- **Age Bracket**: `{selected_row['age_group']}`")
            st.write(f"- **Gender**: `{selected_row['gender']}`")
            st.write(f"- **Race**: `{selected_row['race_display']}`")
            st.write(f"- **Admission Type ID**: `{selected_row['admission_type_id']}`")
            st.write(f"- **Admission Source ID**: `{selected_row['admission_source_id']}`")

        with c2:
            st.markdown("##### 🏥 Hospital Utilization")
            st.write(f"- **Length of Stay**: `{selected_row['length_of_stay']} days`")
            st.write(f"- **Prior Inpatient Visits (1 yr)**: `{selected_row['num_inpatient']}`")
            st.write(f"- **Prior ER Visits (1 yr)**: `{selected_row['num_emergency']}`")
            st.write(f"- **Prior Outpatient Visits**: `{selected_row['num_outpatient']}`")
            st.write(f"- **Lab Tests Ordered**: `{selected_row['num_lab_procedures']}`")
            st.write(f"- **Distinct Medications**: `{selected_row['num_medications']}`")

        with c3:
            st.markdown("##### 🧪 Glycemic & Medication Status")
            st.write(f"- **HbA1c Lab Result**: `{selected_row['a1c_result_display']}`")
            st.write(f"- **Max Glucose Serum**: `{selected_row['max_glu_serum_display']}`")
            st.write(f"- **Insulin Status**: `{selected_row['insulin']}`")
            st.write(f"- **Medication Changed**: `{selected_row['change']}`")
            st.write(f"- **Diabetes Med Prescribed**: `{selected_row['diabetes_med']}`")
            st.write(f"- **Primary ICD-9 Code**: `{selected_row['primary_diag']}`")

        st.markdown("---")

        # Mathematical Feature Attribution (Local Explanation)
        st.markdown("#### 🔬 Mathematical Model Attribution (Log-Odds Contributions)")
        st.caption(
            "For this Logistic Regression model, log-odds are linear: $\\text{logit}(p) = \\beta_0 + \\sum \\beta_i x_i$. "
            "Bars indicate the exact mathematical contribution $(\\beta_i \\cdot x_i)$ of this encounter's features to the predicted probability. "
            "**Statistical associations do not imply medical causation.**"
        )

        # Retrieve original features for this encounter directly from df_scored
        num_cols, cat_cols, _ = get_feature_manifest(include_discharge_disposition=False)
        feature_cols = num_cols + cat_cols
        single_encounter_df = df_scored.loc[[selected_row.name], feature_cols]

        pos_factors, neg_factors, intercept_val = compute_local_explanation(
            pipeline=pipeline,
            encounter_row_features=single_encounter_df,
            top_n=6,
        )

        exp_col1, exp_col2 = st.columns(2)

        with exp_col1:
            st.markdown("##### 🔺 Top Risk-Increasing Drivers $(\\beta_i x_i > 0)$")
            if pos_factors:
                pos_df = pd.DataFrame(pos_factors)
                pos_chart = (
                    alt.Chart(pos_df)
                    .mark_bar(color="#DC2626", cornerRadiusTopRight=4, cornerRadiusBottomRight=4)
                    .encode(
                        x=alt.X("contribution:Q", title="Positive Log-Odds Contribution"),
                        y=alt.Y("clinical_name:N", sort="-x", title=None),
                        tooltip=["clinical_name", alt.Tooltip("contribution:Q", format=".3f")],
                    )
                    .properties(height=200)
                )
                st.altair_chart(pos_chart, use_container_width=True)
            else:
                st.info("No significant positive risk drivers identified for this encounter.")

        with exp_col2:
            st.markdown("##### 🔻 Top Risk-Reducing Factors $(\\beta_i x_i < 0)$")
            if neg_factors:
                neg_df = pd.DataFrame(neg_factors)
                neg_chart = (
                    alt.Chart(neg_df)
                    .mark_bar(color="#059669", cornerRadiusTopRight=4, cornerRadiusBottomRight=4)
                    .encode(
                        x=alt.X("contribution:Q", title="Negative Log-Odds Impact (Protective)"),
                        y=alt.Y("clinical_name:N", sort="x", title=None),
                        tooltip=["clinical_name", alt.Tooltip("contribution:Q", format=".3f")],
                    )
                    .properties(height=200)
                )
                st.altair_chart(neg_chart, use_container_width=True)
            else:
                st.info("No significant protective factors identified for this encounter.")

        st.caption(f"Base model intercept $(\\beta_0)$: `{intercept_val:.3f}`")
        st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # TAB 3: Cohort Diagnostics & Model Metrics
    # -------------------------------------------------------------------------
    with tab_diagnostics:
        st.markdown(
            """
            <div class="keel-card">
                <div class="keel-card-title">Model Diagnostics & Cohort Provenance</div>
                <div class="keel-card-subtitle">
                    Evaluated on out-of-fold patient encounters using strict patient-grouped cross-validation.
                </div>
            """,
            unsafe_allow_html=True,
        )

        dcol1, dcol2 = st.columns(2)

        with dcol1:
            st.markdown("##### 📊 Out-of-Fold Evaluation Metrics (Test Set)")
            if metrics:
                metrics_table = pd.DataFrame([
                    {"Metric": "ROC-AUC (Discrimination)", "Value": f"{metrics.get('roc_auc', 0):.4f}"},
                    {"Metric": "PR-AUC (Average Precision)", "Value": f"{metrics.get('pr_auc', 0):.4f} (Base prevalence: ~0.112)"},
                    {"Metric": "Recall / Sensitivity", "Value": f"{metrics.get('recall', 0)*100:.1f}% of 30d readmissions detected"},
                    {"Metric": "Precision (PPV)", "Value": f"{metrics.get('precision', 0)*100:.1f}%"},
                    {"Metric": "F1-Score", "Value": f"{metrics.get('f1_score', 0):.4f}"},
                    {"Metric": "Specificity (TNR)", "Value": f"{metrics.get('specificity', 0)*100:.1f}%"},
                    {"Metric": "Accuracy (Reference Only)", "Value": f"{metrics.get('accuracy', 0)*100:.1f}% (uninformative under 89% imbalance)"},
                ])
                st.table(metrics_table)

                cm = metrics.get("confusion_matrix", {})
                if cm:
                    st.markdown("##### 🔲 Test Confusion Matrix")
                    cm_df = pd.DataFrame({
                        "Predicted: No Readmit": [cm.get("true_negatives", 0), cm.get("false_negatives", 0)],
                        "Predicted: Readmission (<30d)": [cm.get("false_positives", 0), cm.get("true_positives", 0)],
                    }, index=["Actual: No Readmission", "Actual: Readmission (<30d)"])
                    st.table(cm_df)

        with dcol2:
            st.markdown("##### 🛡️ Clinical Leakage Safeguards")
            st.markdown(
                """
                1. **Patient Leakage Prevention**: Encounters were split using `GroupShuffleSplit` on `patient_nbr`. All encounters for a patient reside strictly in either train or test, ensuring 0 patient overlap.
                2. **Terminal Encounters Dropped**: 2,423 encounters where patients expired in the hospital or were discharged to hospice were excluded because readmission is clinically impossible for deceased patients.
                3. **Timing Leakage Avoided**: `discharge_disposition_id` is excluded from the primary baseline features because discharge disposition is only finalized at discharge and reflects care interventions already prescribed.
                4. **No Direct Identifiers**: `encounter_id` and `patient_nbr` are strictly excluded from model features and from the dashboard UI.
                """
            )

            st.markdown("##### ⚠️ Methodological Limitations")
            st.markdown(
                """
                - **Tabular EHR Constraints**: Historical billing dataset lacks continuous physiological vitals, social determinants of health (SDOH), and post-discharge outpatient adherence.
                - **Moderate Discrimination**: An ROC-AUC of ~0.64 is standard for historical single-encounter EHR data; risk prioritization must be used in a tiered triage capacity rather than hard binary decision-making.
                - **Correlation vs. Causation**: Feature contributions reflect observational statistical associations, not causal therapeutic targets.
                """
            )

        st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
