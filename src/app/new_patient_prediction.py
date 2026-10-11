"""
Keel Health - New Patient Prediction Module

Enables interactive, manual entry of a new clinical encounter to obtain 30-day readmission
risk predictions and transparent linear feature attributions from the trained baseline model.

Key Architectural Safeguards:
1. Strict Schema Adherence: Encodes and scales all 41 baseline features matching the fitted
   preprocessing pipeline (8 numerical, 33 categorical).
2. Zero Outcome Leakage: Uses the existing serialized Logistic Regression pipeline without
   modifying weights, retraining, or modifying historical cohort queues.
3. Transparent Attribution: Computes exact log-odds linear contributions (beta_i * x_i)
   and derives localized transitional care considerations.
4. Input Safety: Safely handles missing diagnosis codes ('?') and unperformed lab tests
   ('Unknown'/'None') via the pipeline's OneHotEncoder and SimpleImputer policies.
5. Fictional Labeling: All sample profiles are explicitly marked as fictional, and all outputs
   are designated as algorithmic decision-support estimates.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Ensure project root is available in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.app.translations import (
    CLINICAL_DOMAINS_TRANSLATION,
    DIAG_CATEGORY_TRANSLATIONS,
    FEATURE_TRANSLATIONS,
    TIER_TRANSLATIONS,
    UI_STRINGS,
    t,
    translate_adm_source,
    translate_adm_type,
    translate_med_option,
    translate_tier,
)
from src.features.preprocessing import get_feature_manifest


def get_profile_badge(profile: Dict[str, Any], lang: str = "English") -> str:
    """Returns localized profile badge or English fallback."""
    key = profile.get("badge_key", "")
    return t(key, lang) if key and key in UI_STRINGS else profile.get("badge", "")


def get_profile_name(profile: Dict[str, Any], lang: str = "English") -> str:
    """Returns localized profile name or English fallback."""
    key = profile.get("name_key", "")
    return t(key, lang) if key and key in UI_STRINGS else profile.get("name", "")


def get_profile_desc(profile: Dict[str, Any], lang: str = "English") -> str:
    """Returns localized profile description or English fallback."""
    key = profile.get("desc_key", "")
    return t(key, lang) if key and key in UI_STRINGS else profile.get("description", "")


# -----------------------------------------------------------------------------
# Medication Feature Lists & Options
# -----------------------------------------------------------------------------
ALL_MEDICATIONS: List[str] = [
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

# Prominent medications displayed in primary view
PRIMARY_MEDICATIONS: List[str] = [
    "insulin",
    "metformin",
    "glipizide",
    "glyburide",
    "glimepiride",
    "pioglitazone",
    "rosiglitazone",
]

# Specialized medications kept in expander to maintain clean clinical layout
SPECIALIZED_MEDICATIONS: List[str] = [
    m for m in ALL_MEDICATIONS if m not in PRIMARY_MEDICATIONS
]

MED_OPTIONS_FOUR = ["No", "Steady", "Up", "Down"]
MED_OPTIONS_TWO = ["No", "Steady"]


# -----------------------------------------------------------------------------
# Fictional Sample Profiles
# -----------------------------------------------------------------------------
SAMPLE_PROFILES: Dict[str, Dict[str, Any]] = {
    "high_risk_geriatric": {
        "name_key": "prof_name_high_risk_geriatric",
        "badge_key": "prof_badge_high_risk_geriatric",
        "desc_key": "prof_desc_high_risk_geriatric",
        "name": "High-Risk Geriatric (Frequent Admissions & Insulin Instability)",
        "badge": "🚨 Higher Risk / Frequent Inpatient",
        "description": (
            "Fictional 82-year-old patient admitted through the ER with acute decompensated "
            "Heart Failure, 3 prior hospitalizations in the past year, marked hyperglycemia "
            "(A1C > 8, Glucose > 300), and upward insulin titration during the 8-day admission."
        ),
        "data": {
            "time_in_hospital": 8,
            "num_lab_procedures": 68,
            "num_procedures": 2,
            "num_medications": 24,
            "number_outpatient": 1,
            "number_emergency": 2,
            "number_inpatient": 3,
            "number_diagnoses": 9,
            "race": "AfricanAmerican",
            "gender": "Female",
            "age": "[80-90)",
            "admission_type_id": "1",  # Emergency
            "admission_source_id": "7",  # Emergency Room
            "max_glu_serum": ">300",
            "A1Cresult": ">8",
            "change": "Ch",
            "diabetesMed": "Yes",
            "diag_1": "428",  # Heart failure (Circulatory)
            "diag_2": "250.02",  # Diabetes
            "diag_3": "584",  # Acute kidney injury (Genitourinary)
            "insulin": "Up",
            "metformin": "No",
            "glipizide": "Steady",
            "glyburide": "No",
            "glimepiride": "No",
            "pioglitazone": "No",
            "rosiglitazone": "No",
            "repaglinide": "No",
            "nateglinide": "No",
            "chlorpropamide": "No",
            "acetohexamide": "No",
            "tolbutamide": "No",
            "acarbose": "No",
            "miglitol": "No",
            "troglitazone": "No",
            "tolazamide": "No",
            "glyburide-metformin": "No",
            "glipizide-metformin": "No",
            "glimepiride-pioglitazone": "No",
            "metformin-rosiglitazone": "No",
            "metformin-pioglitazone": "No",
        },
    },
    "moderate_risk_surgical": {
        "name_key": "prof_name_moderate_risk_surgical",
        "badge_key": "prof_badge_moderate_risk_surgical",
        "desc_key": "prof_desc_moderate_risk_surgical",
        "name": "Moderate-Risk Post-Surgical (Regimen Adjusted)",
        "badge": "⚠️ Moderate Risk / Regimen Adjustment",
        "description": (
            "Fictional 56-year-old patient admitted urgently for acute diverticular/GI condition, "
            "stayed 4 days with moderate lab testing, diabetic regimen adjusted with downward "
            "metformin titration, and 1 prior hospital stay in the past year."
        ),
        "data": {
            "time_in_hospital": 4,
            "num_lab_procedures": 42,
            "num_procedures": 3,
            "num_medications": 16,
            "number_outpatient": 2,
            "number_emergency": 0,
            "number_inpatient": 1,
            "number_diagnoses": 7,
            "race": "Caucasian",
            "gender": "Male",
            "age": "[50-60)",
            "admission_type_id": "2",  # Urgent
            "admission_source_id": "2",  # Clinic Referral
            "max_glu_serum": "Norm",
            "A1Cresult": ">7",
            "change": "Ch",
            "diabetesMed": "Yes",
            "diag_1": "530",  # Digestive
            "diag_2": "250",  # Diabetes
            "diag_3": "401",  # Hypertension
            "insulin": "Steady",
            "metformin": "Down",
            "glipizide": "No",
            "glyburide": "No",
            "glimepiride": "No",
            "pioglitazone": "No",
            "rosiglitazone": "No",
            "repaglinide": "No",
            "nateglinide": "No",
            "chlorpropamide": "No",
            "acetohexamide": "No",
            "tolbutamide": "No",
            "acarbose": "No",
            "miglitol": "No",
            "troglitazone": "No",
            "tolazamide": "No",
            "glyburide-metformin": "No",
            "glipizide-metformin": "No",
            "glimepiride-pioglitazone": "No",
            "metformin-rosiglitazone": "No",
            "metformin-pioglitazone": "No",
        },
    },
    "lower_risk_young_adult": {
        "name_key": "prof_name_lower_risk_young_adult",
        "badge_key": "prof_badge_lower_risk_young_adult",
        "desc_key": "prof_desc_lower_risk_young_adult",
        "name": "Lower-Risk Young Adult (First Admission & Stable Oral Regimen)",
        "badge": "✅ Lower Risk / First Admission",
        "description": (
            "Fictional 34-year-old patient admitted electively for orthopedic arthroscopy "
            "with zero prior acute hospitalizations or ER visits, normal glycemic lab markers, "
            "and stable single-agent metformin therapy."
        ),
        "data": {
            "time_in_hospital": 2,
            "num_lab_procedures": 24,
            "num_procedures": 1,
            "num_medications": 7,
            "number_outpatient": 0,
            "number_emergency": 0,
            "number_inpatient": 0,
            "number_diagnoses": 4,
            "race": "Asian",
            "gender": "Female",
            "age": "[30-40)",
            "admission_type_id": "3",  # Elective
            "admission_source_id": "1",  # Physician Referral
            "max_glu_serum": "Norm",
            "A1Cresult": "Norm",
            "change": "No",
            "diabetesMed": "Yes",
            "diag_1": "715",  # Musculoskeletal
            "diag_2": "250",  # Diabetes
            "diag_3": "V58",  # Other
            "metformin": "Steady",
            "insulin": "No",
            "glipizide": "No",
            "glyburide": "No",
            "glimepiride": "No",
            "pioglitazone": "No",
            "rosiglitazone": "No",
            "repaglinide": "No",
            "nateglinide": "No",
            "chlorpropamide": "No",
            "acetohexamide": "No",
            "tolbutamide": "No",
            "acarbose": "No",
            "miglitol": "No",
            "troglitazone": "No",
            "tolazamide": "No",
            "glyburide-metformin": "No",
            "glipizide-metformin": "No",
            "glimepiride-pioglitazone": "No",
            "metformin-rosiglitazone": "No",
            "metformin-pioglitazone": "No",
        },
    },
    "missing_data_edge_case": {
        "name_key": "prof_name_missing_data_edge_case",
        "badge_key": "prof_badge_missing_data_edge_case",
        "desc_key": "prof_desc_missing_data_edge_case",
        "name": "Missing Diagnostic Code & Unperformed Lab Tests (Documentation Edge Case)",
        "badge": "⚠️ Safety Edge Case / Incomplete Data",
        "description": (
            "Fictional 64-year-old male with unrecorded primary diagnosis billing code ('?'), "
            "unperformed HbA1c and fasting glucose tests, and unknown race. Verifies graceful "
            "handling of missing clinical records without crashing."
        ),
        "data": {
            "time_in_hospital": 3,
            "num_lab_procedures": 18,
            "num_procedures": 0,
            "num_medications": 10,
            "number_outpatient": 0,
            "number_emergency": 1,
            "number_inpatient": 1,
            "number_diagnoses": 5,
            "race": "Unknown",
            "gender": "Male",
            "age": "[60-70)",
            "admission_type_id": "1",  # Emergency
            "admission_source_id": "7",  # ER
            "max_glu_serum": "Unknown",  # Unperformed
            "A1Cresult": "Unknown",  # Unperformed
            "change": "No",
            "diabetesMed": "Yes",
            "diag_1": "?",  # Missing ICD-9 code
            "diag_2": "250",
            "diag_3": "?",
            "insulin": "Steady",
            "metformin": "No",
            "glipizide": "No",
            "glyburide": "No",
            "glimepiride": "No",
            "pioglitazone": "No",
            "rosiglitazone": "No",
            "repaglinide": "No",
            "nateglinide": "No",
            "chlorpropamide": "No",
            "acetohexamide": "No",
            "tolbutamide": "No",
            "acarbose": "No",
            "miglitol": "No",
            "troglitazone": "No",
            "tolazamide": "No",
            "glyburide-metformin": "No",
            "glipizide-metformin": "No",
            "glimepiride-pioglitazone": "No",
            "metformin-rosiglitazone": "No",
            "metformin-pioglitazone": "No",
        },
    },
    "extended_stay_polypharmacy": {
        "name_key": "prof_name_extended_stay_polypharmacy",
        "badge_key": "prof_badge_extended_stay_polypharmacy",
        "desc_key": "prof_desc_extended_stay_polypharmacy",
        "name": "Extended Stay (13 Days) with Extreme Polypharmacy (42 Meds)",
        "badge": "🚨 Higher Risk / Polypharmacy & Stay",
        "description": (
            "Fictional 85-year-old patient transferred from another hospital with complex "
            "respiratory infection, prolonged hospital stay of 13 days (near 14-day truncation limit), "
            "and 42 active medications triggering extreme polypharmacy warnings."
        ),
        "data": {
            "time_in_hospital": 13,
            "num_lab_procedures": 84,
            "num_procedures": 4,
            "num_medications": 42,
            "number_outpatient": 1,
            "number_emergency": 0,
            "number_inpatient": 2,
            "number_diagnoses": 9,
            "race": "Caucasian",
            "gender": "Female",
            "age": "[80-90)",
            "admission_type_id": "1",
            "admission_source_id": "4",  # Transfer from hospital
            "max_glu_serum": "None",
            "A1Cresult": "Norm",
            "change": "Ch",
            "diabetesMed": "Yes",
            "diag_1": "486",  # Pneumonia (Respiratory)
            "diag_2": "428",  # Heart failure (Circulatory)
            "diag_3": "250",  # Diabetes
            "insulin": "Down",
            "metformin": "Steady",
            "pioglitazone": "Steady",
            "glipizide": "No",
            "glyburide": "No",
            "glimepiride": "No",
            "rosiglitazone": "No",
            "repaglinide": "No",
            "nateglinide": "No",
            "chlorpropamide": "No",
            "acetohexamide": "No",
            "tolbutamide": "No",
            "acarbose": "No",
            "miglitol": "No",
            "troglitazone": "No",
            "tolazamide": "No",
            "glyburide-metformin": "No",
            "glipizide-metformin": "No",
            "glimepiride-pioglitazone": "No",
            "metformin-rosiglitazone": "No",
            "metformin-pioglitazone": "No",
        },
    },
    "frequent_er_respiratory": {
        "name_key": "prof_name_frequent_er_respiratory",
        "badge_key": "prof_badge_frequent_er_respiratory",
        "desc_key": "prof_desc_frequent_er_respiratory",
        "name": "Frequent ER Utilization with Chronic COPD (Non-Insulin Managed)",
        "badge": "⚠️ Moderate to High / ER Utilizer",
        "description": (
            "Fictional 74-year-old patient presenting via ER with acute COPD exacerbation, "
            "3 prior ER visits in the past year but 0 inpatient admissions, managed with oral "
            "sulfonylurea without insulin, with elevated A1C (> 8)."
        ),
        "data": {
            "time_in_hospital": 5,
            "num_lab_procedures": 51,
            "num_procedures": 0,
            "num_medications": 14,
            "number_outpatient": 4,
            "number_emergency": 3,
            "number_inpatient": 0,
            "number_diagnoses": 8,
            "race": "Hispanic",
            "gender": "Male",
            "age": "[70-80)",
            "admission_type_id": "1",
            "admission_source_id": "7",
            "max_glu_serum": ">200",
            "A1Cresult": ">8",
            "change": "No",
            "diabetesMed": "Yes",
            "diag_1": "496",  # COPD (Respiratory)
            "diag_2": "250",  # Diabetes
            "diag_3": "401",  # Hypertension
            "glipizide": "Steady",
            "insulin": "No",
            "metformin": "No",
            "glyburide": "No",
            "glimepiride": "No",
            "pioglitazone": "No",
            "rosiglitazone": "No",
            "repaglinide": "No",
            "nateglinide": "No",
            "chlorpropamide": "No",
            "acetohexamide": "No",
            "tolbutamide": "No",
            "acarbose": "No",
            "miglitol": "No",
            "troglitazone": "No",
            "tolazamide": "No",
            "glyburide-metformin": "No",
            "glipizide-metformin": "No",
            "glimepiride-pioglitazone": "No",
            "metformin-rosiglitazone": "No",
            "metformin-pioglitazone": "No",
        },
    },
}

DEFAULT_PROFILE_KEY = "high_risk_geriatric"


# -----------------------------------------------------------------------------
# Input Validation & Preprocessing Preparation
# -----------------------------------------------------------------------------
def validate_patient_input(
    raw_data: Dict[str, Any],
    lang: str = "English",
) -> Tuple[bool, List[str], pd.DataFrame]:
    """
    Validates user-submitted encounter values, checks boundary conditions,
    and returns a clean single-row DataFrame aligned strictly to model schema.

    Returns:
        (is_valid, advisory_notes, formatted_dataframe)
    """
    advisory_notes: List[str] = []
    num_cols, cat_cols, _ = get_feature_manifest(include_discharge_disposition=False)
    feature_cols = num_cols + cat_cols

    clean_dict: Dict[str, Any] = {}

    # 1. Continuous / Numerical feature validation & boundary clamping
    for num_col in num_cols:
        val = raw_data.get(num_col)
        try:
            val_num = float(val) if val is not None else 0.0
            if np.isnan(val_num):
                val_num = 0.0
        except (ValueError, TypeError):
            val_num = 0.0
            advisory_notes.append(f"Invalid numeric value for '{num_col}'. Defaulted to 0.")

        # Clinical boundary constraints
        if num_col == "time_in_hospital":
            val_num = max(1.0, min(14.0, val_num))
        elif num_col == "num_lab_procedures":
            val_num = max(1.0, min(132.0, val_num))
        elif num_col == "num_procedures":
            val_num = max(0.0, min(6.0, val_num))
        elif num_col == "num_medications":
            val_num = max(1.0, min(81.0, val_num))
        elif num_col == "number_diagnoses":
            val_num = max(1.0, min(16.0, val_num))
        else:
            val_num = max(0.0, val_num)

        clean_dict[num_col] = val_num

    # 2. Categorical feature normalization
    for cat_col in cat_cols:
        val_cat = raw_data.get(cat_col)
        if val_cat is None or pd.isna(val_cat):
            clean_str = "Unknown"
        else:
            clean_str = str(val_cat).strip()
            if clean_str in ["", "nan", "None", "?"]:
                clean_str = "Unknown" if cat_col not in ["diag_1", "diag_2", "diag_3"] else "?"

        # Diagnostic documentation check
        if cat_col == "diag_1" and clean_str in ["?", "Unknown", "Missing"]:
            advisory_notes.append(t("np_adv_missing_diag", lang))

        # Lab test unperformed advisory
        if cat_col == "A1Cresult" and clean_str in ["Unknown", "None", "?"]:
            advisory_notes.append(t("np_adv_missing_a1c", lang))
        if cat_col == "max_glu_serum" and clean_str in ["Unknown", "None", "?"]:
            advisory_notes.append(t("np_adv_missing_glu", lang))

        clean_dict[cat_col] = clean_str

    df_row = pd.DataFrame([clean_dict])[feature_cols]
    return True, advisory_notes, df_row


# -----------------------------------------------------------------------------
# Prediction & Clinical Attribution Workflow
# -----------------------------------------------------------------------------
def predict_new_patient(
    pipeline: Any,
    input_df: pd.DataFrame,
    high_threshold: float,
    mod_threshold: float,
    lang: str = "English",
) -> Dict[str, Any]:
    """
    Executes inference with the trained pipeline, computes priority tier,
    runs rule-based quality checks, calculates local linear attributions,
    and produces an individualized clinical summary.
    """
    from src.app.streamlit_app import (
        check_patient_data_quality,
        compute_local_explanation,
        derive_top_driver_labels,
        generate_patient_summary,
    )

    # 1. Generate model prediction
    probabilities = pipeline.predict_proba(input_df)[:, 1]
    prob_val = float(probabilities[0])
    score_pct = round(prob_val * 100, 1)

    # 2. Assign risk priority tier
    if prob_val >= high_threshold:
        risk_tier = "Higher Score"
    elif prob_val >= mod_threshold:
        risk_tier = "Moderate Score"
    else:
        risk_tier = "Lower Score"

    # 3. Calculate proximity to configured decision boundaries
    if prob_val >= high_threshold:
        margin = prob_val - high_threshold
        boundary_status = "above_high"
    elif prob_val >= mod_threshold:
        dist_to_high = high_threshold - prob_val
        dist_to_mod = prob_val - mod_threshold
        margin = min(dist_to_high, dist_to_mod)
        boundary_status = "moderate_band"
    else:
        margin = mod_threshold - prob_val
        boundary_status = "below_mod"

    near_boundary = (margin <= 0.03)

    # 4. Prepare display row for summary and data quality checkers
    row = input_df.iloc[0]
    diag_str = str(row.get("diag_1", ""))
    row_display = pd.Series({
        "encounter_label": "NEW-ENCOUNTER-001",
        "predicted_score": prob_val,
        "score_percent": score_pct,
        "age_group": str(row.get("age", "[50-60)")),
        "length_of_stay": int(row.get("time_in_hospital", 1)),
        "num_inpatient": int(row.get("number_inpatient", 0)),
        "num_emergency": int(row.get("number_emergency", 0)),
        "num_outpatient": int(row.get("number_outpatient", 0)),
        "num_medications": int(row.get("num_medications", 1)),
        "num_lab_procedures": int(row.get("num_lab_procedures", 1)),
        "number_diagnoses": int(row.get("number_diagnoses", 1)),
        "primary_diag": diag_str,
        "diabetes_med": str(row.get("diabetesMed", "Yes")),
        "race_display": str(row.get("race", "Unknown")),
        "max_glu_serum_display": str(row.get("max_glu_serum", "None")),
        "a1c_result_display": str(row.get("A1Cresult", "None")),
        "insulin": str(row.get("insulin", "No")),
        "change": str(row.get("change", "No")),
        "gender": str(row.get("gender", "Female")),
        "admission_type_id": str(row.get("admission_type_id", "1")),
        "admission_source_id": str(row.get("admission_source_id", "7")),
    })

    # 5. Rule-based clinical data quality audit
    dq_warnings = check_patient_data_quality(row_display, lang=lang)

    # 6. Mathematical local feature attribution
    pos_drivers, neg_drivers, intercept = compute_local_explanation(
        pipeline, input_df, top_n=5, lang=lang
    )

    # 7. Derive top clinical driver
    top_driver_list = derive_top_driver_labels(pd.DataFrame([row_display]))
    top_driver = top_driver_list[0] if top_driver_list else "Baseline Clinical Risk"

    # 8. Individualized clinical transitional care summary
    summary = generate_patient_summary(
        selected_row=row_display,
        selected_score=prob_val,
        selected_tier=risk_tier,
        pos_factors=pos_drivers,
        neg_factors=neg_drivers,
        lang=lang,
    )

    return {
        "predicted_score": prob_val,
        "score_percent": score_pct,
        "risk_tier": risk_tier,
        "boundary_margin": margin,
        "near_boundary": near_boundary,
        "boundary_status": boundary_status,
        "top_driver": top_driver,
        "dq_warnings": dq_warnings,
        "pos_drivers": pos_drivers,
        "neg_drivers": neg_drivers,
        "intercept": intercept,
        "summary": summary,
        "display_row": row_display,
    }


# -----------------------------------------------------------------------------
# Streamlit Tab Rendering
# -----------------------------------------------------------------------------
def render_new_patient_tab(
    pipeline: Any,
    high_threshold: float,
    mod_threshold: float,
    is_dark: bool,
    lang: str = "English",
) -> None:
    """
    Renders the interactive New Patient Prediction tab in the Keel Health dashboard.
    """
    from src.app.streamlit_app import apply_chart_theme

    st.markdown(
        f"""
        <div class="keel-card" style="margin-bottom: 1.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.5rem;">
                <div>
                    <div class="keel-card-title">➕ {t("np_header_title", lang)}</div>
                    <div class="keel-card-subtitle">{t("np_header_subtitle", lang)}</div>
                </div>
                <div style="background: {'rgba(99, 102, 241, 0.15)' if is_dark else '#EEF2FF'};
                            border: 1px solid {'#818CF8' if is_dark else '#6366F1'};
                            color: {'#C7D2FE' if is_dark else '#4338CA'};
                            font-size: 0.75rem; font-weight: 700; padding: 0.25rem 0.65rem; border-radius: 9999px;">
                    {t("np_badge_prototype", lang)}
                </div>
            </div>
            <div style="margin-top: 0.75rem; padding: 0.65rem 0.85rem; border-radius: 6px;
                        background: {'rgba(245, 158, 11, 0.08)' if is_dark else '#FFFBEB'};
                        border-left: 3px solid #F59E0B; font-size: 0.82rem; color: {'#FCD34D' if is_dark else '#92400E'};">
                ⚠️ <strong>{t("np_disclaimer_title", lang)}:</strong> {t("np_disclaimer_text", lang)}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -------------------------------------------------------------------------
    # Preset Fictional Profiles Selector
    # -------------------------------------------------------------------------
    st.markdown(f"##### 👤 {t('np_profile_select_title', lang)}")
    st.caption(t("np_profile_select_caption", lang))

    profile_keys = list(SAMPLE_PROFILES.keys())
    profile_names = [
        f"{get_profile_badge(SAMPLE_PROFILES[k], lang)} - {get_profile_name(SAMPLE_PROFILES[k], lang)}"
        for k in profile_keys
    ]

    p_col1, p_col2 = st.columns([3, 1])
    with p_col1:
        selected_p_idx = st.selectbox(
            label=t("np_profile_dropdown_label", lang),
            options=range(len(profile_keys)),
            format_func=lambda idx: profile_names[idx],
            key="np_profile_select_index",
            label_visibility="collapsed",
        )
    with p_col2:
        load_btn = st.button(f"📥 {t('np_btn_load_profile', lang)}", use_container_width=True)

    active_p_key = profile_keys[selected_p_idx]
    active_profile = SAMPLE_PROFILES[active_p_key]
    profile_desc = get_profile_desc(active_profile, lang)

    # Display scenario clinical narrative
    st.markdown(
        f"""
        <div style="background: {'rgba(15, 23, 42, 0.6)' if is_dark else '#F8FAFC'};
                    border: 1px dashed {'#475569' if is_dark else '#CBD5E1'};
                    padding: 0.65rem 0.85rem; border-radius: 6px; margin-bottom: 1rem; font-size: 0.83rem;">
            <strong>{t('np_scenario_brief_label', lang)}</strong> {profile_desc}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Initialize or update session state form variables upon loading
    form_keys = [
        "time_in_hospital", "num_lab_procedures", "num_procedures", "num_medications",
        "number_outpatient", "number_emergency", "number_inpatient", "number_diagnoses",
        "race", "gender", "age", "admission_type_id", "admission_source_id",
        "max_glu_serum", "A1Cresult", "change", "diabetesMed",
        "diag_1", "diag_2", "diag_3",
    ] + ALL_MEDICATIONS

    if load_btn or ("np_form_initialized" not in st.session_state):
        for k in form_keys:
            st.session_state[f"np_val_{k}"] = active_profile["data"].get(k)
        st.session_state["np_form_initialized"] = True
        st.session_state["np_active_profile_name"] = active_profile["name"]
        st.session_state["np_form_version"] = st.session_state.get("np_form_version", 0) + 1

    form_ver = st.session_state.get("np_form_version", 0)

    # -------------------------------------------------------------------------
    # Manual Input Form
    # -------------------------------------------------------------------------
    with st.form("new_patient_entry_form"):
        # Section 1: Demographics & Admission
        st.markdown(f"#### 1. {t('np_sec_demographics', lang)}")
        d_col1, d_col2, d_col3, d_col4 = st.columns(4)

        with d_col1:
            age_options = ["[0-10)", "[10-20)", "[20-30)", "[30-40)", "[40-50)", "[50-60)", "[60-70)", "[70-80)", "[80-90)", "[90-100)"]
            cur_age = str(st.session_state.get("np_val_age", "[50-60)"))
            age_idx = age_options.index(cur_age) if cur_age in age_options else 5
            val_age = st.selectbox(t("prof_age_bracket", lang), age_options, index=age_idx, key=f"np_in_age_{form_ver}")

        with d_col2:
            gender_options = ["Female", "Male", "Unknown/Invalid"]
            cur_gender = str(st.session_state.get("np_val_gender", "Female"))
            gender_idx = gender_options.index(cur_gender) if cur_gender in gender_options else 0
            val_gender = st.selectbox(t("prof_gender", lang), gender_options, index=gender_idx, key=f"np_in_gender_{form_ver}")

        with d_col3:
            race_options = ["Caucasian", "AfricanAmerican", "Hispanic", "Asian", "Other", "Unknown"]
            cur_race = str(st.session_state.get("np_val_race", "Caucasian"))
            race_idx = race_options.index(cur_race) if cur_race in race_options else 0
            val_race = st.selectbox(t("prof_race", lang), race_options, index=race_idx, key=f"np_in_race_{form_ver}")

        with d_col4:
            type_keys = ["1", "2", "3", "4", "5", "6", "7", "8"]
            cur_type = str(st.session_state.get("np_val_admission_type_id", "1"))
            type_idx = type_keys.index(cur_type) if cur_type in type_keys else 0
            val_adm_type = st.selectbox(
                t("prof_adm_type", lang),
                type_keys,
                index=type_idx,
                format_func=lambda k: translate_adm_type(k, lang),
                key=f"np_in_adm_type_{form_ver}",
            )

        # Section 2: Hospital Stay & Utilization History
        st.markdown(f"#### 2. {t('np_sec_utilization', lang)}")
        u_col1, u_col2, u_col3, u_col4 = st.columns(4)

        with u_col1:
            val_los = st.number_input(
                f"{t('prof_stay_days', lang)} (1-14)",
                min_value=1,
                max_value=14,
                value=int(st.session_state.get("np_val_time_in_hospital", 4)),
                step=1,
                key=f"np_in_los_{form_ver}",
            )
            val_inpatient = st.number_input(
                t("prof_prior_adm", lang),
                min_value=0,
                max_value=25,
                value=int(st.session_state.get("np_val_number_inpatient", 0)),
                step=1,
                key=f"np_in_inpatient_{form_ver}",
            )

        with u_col2:
            val_emergency = st.number_input(
                t("prof_prior_er", lang),
                min_value=0,
                max_value=25,
                value=int(st.session_state.get("np_val_number_emergency", 0)),
                step=1,
                key=f"np_in_emergency_{form_ver}",
            )
            val_outpatient = st.number_input(
                t("prof_prior_op", lang),
                min_value=0,
                max_value=40,
                value=int(st.session_state.get("np_val_number_outpatient", 0)),
                step=1,
                key=f"np_in_outpatient_{form_ver}",
            )

        with u_col3:
            val_labs = st.number_input(
                t("prof_lab_tests", lang),
                min_value=1,
                max_value=132,
                value=int(st.session_state.get("np_val_num_lab_procedures", 40)),
                step=1,
                key=f"np_in_labs_{form_ver}",
            )
            val_procedures = st.number_input(
                t("np_num_procedures", lang),
                min_value=0,
                max_value=6,
                value=int(st.session_state.get("np_val_num_procedures", 1)),
                step=1,
                key=f"np_in_procedures_{form_ver}",
            )

        with u_col4:
            val_med_count = st.number_input(
                t("prof_med_count", lang),
                min_value=1,
                max_value=81,
                value=int(st.session_state.get("np_val_num_medications", 15)),
                step=1,
                key=f"np_in_med_count_{form_ver}",
            )
            val_diag_count = st.number_input(
                t("np_num_diagnoses", lang),
                min_value=1,
                max_value=16,
                value=int(st.session_state.get("np_val_number_diagnoses", 7)),
                step=1,
                key=f"np_in_diag_count_{form_ver}",
            )

        # Section 3: Clinical Diagnoses (ICD-9 Codes)
        st.markdown(f"#### 3. {t('np_sec_diagnoses', lang)}")
        st.caption(t("np_sec_diagnoses_caption", lang))
        dg_col1, dg_col2, dg_col3, dg_col4 = st.columns(4)

        with dg_col1:
            val_diag1 = st.text_input(
                t("np_diag_1_label", lang),
                value=str(st.session_state.get("np_val_diag_1", "414")),
                key=f"np_in_diag1_{form_ver}",
            )
        with dg_col2:
            val_diag2 = st.text_input(
                t("np_diag_2_label", lang),
                value=str(st.session_state.get("np_val_diag_2", "250")),
                key=f"np_in_diag2_{form_ver}",
            )
        with dg_col3:
            val_diag3 = st.text_input(
                t("np_diag_3_label", lang),
                value=str(st.session_state.get("np_val_diag_3", "401")),
                key=f"np_in_diag3_{form_ver}",
            )
        with dg_col4:
            src_keys = ["7", "1", "2", "3", "4", "5", "6", "10", "20"]
            cur_src = str(st.session_state.get("np_val_admission_source_id", "7"))
            src_idx = src_keys.index(cur_src) if cur_src in src_keys else 0
            val_adm_src = st.selectbox(
                t("prof_adm_source", lang),
                src_keys,
                index=src_idx,
                format_func=lambda k: translate_adm_source(k, lang),
                key=f"np_in_adm_src_{form_ver}",
            )

        # Section 4: Glycemic Lab Markers & Medication Adjustment
        st.markdown(f"#### 4. {t('np_sec_glycemic', lang)}")
        g_col1, g_col2, g_col3, g_col4 = st.columns(4)

        with g_col1:
            a1c_options = ["None", "Norm", ">7", ">8", "Unknown"]
            cur_a1c = str(st.session_state.get("np_val_A1Cresult", "Norm"))
            a1c_idx = a1c_options.index(cur_a1c) if cur_a1c in a1c_options else 1
            val_a1c = st.selectbox(t("prof_a1c", lang), a1c_options, index=a1c_idx, key=f"np_in_a1c_{form_ver}")

        with g_col2:
            glu_options = ["None", "Norm", ">200", ">300", "Unknown"]
            cur_glu = str(st.session_state.get("np_val_max_glu_serum", "None"))
            glu_idx = glu_options.index(cur_glu) if cur_glu in glu_options else 0
            val_glu = st.selectbox(t("prof_glucose", lang), glu_options, index=glu_idx, key=f"np_in_glu_{form_ver}")

        with g_col3:
            chg_options = ["No", "Ch"]
            cur_chg = str(st.session_state.get("np_val_change", "No"))
            chg_idx = chg_options.index(cur_chg) if cur_chg in chg_options else 0
            val_change = st.selectbox(
                f"{t('prof_med_chg', lang)} (`change`)",
                chg_options,
                index=chg_idx,
                format_func=lambda c: t("np_med_ch_desc", lang) if c == "Ch" else t("np_med_no_desc", lang),
                key=f"np_in_change_{form_ver}",
            )

        with g_col4:
            dm_options = ["Yes", "No"]
            cur_dm = str(st.session_state.get("np_val_diabetesMed", "Yes"))
            dm_idx = dm_options.index(cur_dm) if cur_dm in dm_options else 0
            val_dm = st.selectbox(t("prof_dm_med", lang), dm_options, index=dm_idx, key=f"np_in_dm_{form_ver}")

        # Section 5: Specific Antidiabetic Agents
        st.markdown(f"#### 5. {t('np_sec_medications', lang)}")
        m_col1, m_col2, m_col3, m_col4 = st.columns(4)

        with m_col1:
            ins_cur = str(st.session_state.get("np_val_insulin", "No"))
            ins_idx = MED_OPTIONS_FOUR.index(ins_cur) if ins_cur in MED_OPTIONS_FOUR else 0
            val_insulin = st.selectbox(t("prof_insulin", lang), MED_OPTIONS_FOUR, index=ins_idx, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_insulin_{form_ver}")

        with m_col2:
            met_cur = str(st.session_state.get("np_val_metformin", "No"))
            met_idx = MED_OPTIONS_FOUR.index(met_cur) if met_cur in MED_OPTIONS_FOUR else 0
            val_metformin = st.selectbox("Metformin", MED_OPTIONS_FOUR, index=met_idx, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_metformin_{form_ver}")

        with m_col3:
            glp_cur = str(st.session_state.get("np_val_glipizide", "No"))
            glp_idx = MED_OPTIONS_FOUR.index(glp_cur) if glp_cur in MED_OPTIONS_FOUR else 0
            val_glipizide = st.selectbox("Glipizide", MED_OPTIONS_FOUR, index=glp_idx, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_glipizide_{form_ver}")

        with m_col4:
            gly_cur = str(st.session_state.get("np_val_glyburide", "No"))
            gly_idx = MED_OPTIONS_FOUR.index(gly_cur) if gly_cur in MED_OPTIONS_FOUR else 0
            val_glyburide = st.selectbox("Glyburide", MED_OPTIONS_FOUR, index=gly_idx, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_glyburide_{form_ver}")

        p2_col1, p2_col2, p2_col3, p2_col4 = st.columns(4)
        with p2_col1:
            glm_cur = str(st.session_state.get("np_val_glimepiride", "No"))
            glm_idx = MED_OPTIONS_FOUR.index(glm_cur) if glm_cur in MED_OPTIONS_FOUR else 0
            val_glimepiride = st.selectbox("Glimepiride", MED_OPTIONS_FOUR, index=glm_idx, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_glimepiride_{form_ver}")

        with p2_col2:
            pio_cur = str(st.session_state.get("np_val_pioglitazone", "No"))
            pio_idx = MED_OPTIONS_FOUR.index(pio_cur) if pio_cur in MED_OPTIONS_FOUR else 0
            val_pioglitazone = st.selectbox("Pioglitazone", MED_OPTIONS_FOUR, index=pio_idx, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_pioglitazone_{form_ver}")

        with p2_col3:
            ros_cur = str(st.session_state.get("np_val_rosiglitazone", "No"))
            ros_idx = MED_OPTIONS_FOUR.index(ros_cur) if ros_cur in MED_OPTIONS_FOUR else 0
            val_rosiglitazone = st.selectbox("Rosiglitazone", MED_OPTIONS_FOUR, index=ros_idx, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_rosiglitazone_{form_ver}")

        with p2_col4:
            rep_cur = str(st.session_state.get("np_val_repaglinide", "No"))
            rep_idx = MED_OPTIONS_FOUR.index(rep_cur) if rep_cur in MED_OPTIONS_FOUR else 0
            val_repaglinide = st.selectbox("Repaglinide", MED_OPTIONS_FOUR, index=rep_idx, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_repaglinide_{form_ver}")

        # Specialized Oral Agents Expander
        with st.expander(f"➕ {t('np_more_meds_expander', lang)}"):
            e_col1, e_col2, e_col3 = st.columns(3)
            with e_col1:
                cur_nat = str(st.session_state.get("np_val_nateglinide", "No"))
                val_nateglinide = st.selectbox("Nateglinide", MED_OPTIONS_FOUR, index=MED_OPTIONS_FOUR.index(cur_nat) if cur_nat in MED_OPTIONS_FOUR else 0, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_nateglinide_{form_ver}")
                cur_chl = str(st.session_state.get("np_val_chlorpropamide", "No"))
                val_chlorpropamide = st.selectbox("Chlorpropamide", MED_OPTIONS_FOUR, index=MED_OPTIONS_FOUR.index(cur_chl) if cur_chl in MED_OPTIONS_FOUR else 0, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_chlorpropamide_{form_ver}")
                cur_aca = str(st.session_state.get("np_val_acarbose", "No"))
                aca_opts = ["No", "Steady", "Up"]
                val_acarbose = st.selectbox("Acarbose", aca_opts, index=aca_opts.index(cur_aca) if cur_aca in aca_opts else 0, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_acarbose_{form_ver}")
                cur_mig = str(st.session_state.get("np_val_miglitol", "No"))
                val_miglitol = st.selectbox("Miglitol", MED_OPTIONS_FOUR, index=MED_OPTIONS_FOUR.index(cur_mig) if cur_mig in MED_OPTIONS_FOUR else 0, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_miglitol_{form_ver}")
                cur_tol = str(st.session_state.get("np_val_tolbutamide", "No"))
                val_tolbutamide = st.selectbox("Tolbutamide", MED_OPTIONS_TWO, index=MED_OPTIONS_TWO.index(cur_tol) if cur_tol in MED_OPTIONS_TWO else 0, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_tolbutamide_{form_ver}")
            with e_col2:
                cur_tola = str(st.session_state.get("np_val_tolazamide", "No"))
                tola_opts = ["No", "Steady", "Up"]
                val_tolazamide = st.selectbox("Tolazamide", tola_opts, index=tola_opts.index(cur_tola) if cur_tola in tola_opts else 0, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_tolazamide_{form_ver}")
                cur_ace = str(st.session_state.get("np_val_acetohexamide", "No"))
                val_acetohexamide = st.selectbox("Acetohexamide", MED_OPTIONS_TWO, index=MED_OPTIONS_TWO.index(cur_ace) if cur_ace in MED_OPTIONS_TWO else 0, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_acetohexamide_{form_ver}")
                cur_tro = str(st.session_state.get("np_val_troglitazone", "No"))
                val_troglitazone = st.selectbox("Troglitazone", MED_OPTIONS_TWO, index=MED_OPTIONS_TWO.index(cur_tro) if cur_tro in MED_OPTIONS_TWO else 0, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_troglitazone_{form_ver}")
                cur_glym = str(st.session_state.get("np_val_glyburide-metformin", "No"))
                val_glyburide_met = st.selectbox("Glyburide-Metformin", MED_OPTIONS_FOUR, index=MED_OPTIONS_FOUR.index(cur_glym) if cur_glym in MED_OPTIONS_FOUR else 0, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_glyburide_met_{form_ver}")
                cur_glpm = str(st.session_state.get("np_val_glipizide-metformin", "No"))
                val_glipizide_met = st.selectbox("Glipizide-Metformin", MED_OPTIONS_TWO, index=MED_OPTIONS_TWO.index(cur_glpm) if cur_glpm in MED_OPTIONS_TWO else 0, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_glipizide_met_{form_ver}")
            with e_col3:
                val_glimepiride_pio = st.selectbox("Glimepiride-Pioglitazone", ["No"], index=0, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_glimepiride_pio_{form_ver}")
                cur_mr = str(st.session_state.get("np_val_metformin-rosiglitazone", "No"))
                val_met_ros = st.selectbox("Metformin-Rosiglitazone", MED_OPTIONS_TWO, index=MED_OPTIONS_TWO.index(cur_mr) if cur_mr in MED_OPTIONS_TWO else 0, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_met_ros_{form_ver}")
                cur_mp = str(st.session_state.get("np_val_metformin-pioglitazone", "No"))
                val_met_pio = st.selectbox("Metformin-Pioglitazone", MED_OPTIONS_TWO, index=MED_OPTIONS_TWO.index(cur_mp) if cur_mp in MED_OPTIONS_TWO else 0, format_func=lambda o: translate_med_option(o, lang), key=f"np_in_met_pio_{form_ver}")

        # Form Submit Button
        st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
        predict_submitted = st.form_submit_button(
            f"🚀 {t('np_btn_predict', lang)}",
            use_container_width=True,
            type="primary",
        )

    # -------------------------------------------------------------------------
    # Inference & Results Presentation
    # -------------------------------------------------------------------------
    if predict_submitted:
        # Assemble dictionary from submitted form inputs
        raw_submission = {
            "time_in_hospital": val_los,
            "num_lab_procedures": val_labs,
            "num_procedures": val_procedures,
            "num_medications": val_med_count,
            "number_outpatient": val_outpatient,
            "number_emergency": val_emergency,
            "number_inpatient": val_inpatient,
            "number_diagnoses": val_diag_count,
            "race": val_race,
            "gender": val_gender,
            "age": val_age,
            "admission_type_id": val_adm_type,
            "admission_source_id": val_adm_src,
            "max_glu_serum": val_glu,
            "A1Cresult": val_a1c,
            "change": val_change,
            "diabetesMed": val_dm,
            "diag_1": val_diag1,
            "diag_2": val_diag2,
            "diag_3": val_diag3,
            "insulin": val_insulin,
            "metformin": val_metformin,
            "glipizide": val_glipizide,
            "glyburide": val_glyburide,
            "glimepiride": val_glimepiride,
            "pioglitazone": val_pioglitazone,
            "rosiglitazone": val_rosiglitazone,
            "repaglinide": val_repaglinide,
            "nateglinide": val_nateglinide,
            "chlorpropamide": val_chlorpropamide,
            "acarbose": val_acarbose,
            "miglitol": val_miglitol,
            "tolbutamide": val_tolbutamide,
            "tolazamide": val_tolazamide,
            "acetohexamide": val_acetohexamide,
            "troglitazone": val_troglitazone,
            "glyburide-metformin": val_glyburide_met,
            "glipizide-metformin": val_glipizide_met,
            "glimepiride-pioglitazone": val_glimepiride_pio,
            "metformin-rosiglitazone": val_met_ros,
            "metformin-pioglitazone": val_met_pio,
        }

        # 1. Validate inputs safely
        is_valid, advisories, input_df = validate_patient_input(raw_submission, lang=lang)
        if not is_valid:
            st.error(t("np_validation_error", lang))
            return

        # Store last prediction in session state
        pred_res = predict_new_patient(
            pipeline=pipeline,
            input_df=input_df,
            high_threshold=high_threshold,
            mod_threshold=mod_threshold,
            lang=lang,
        )
        st.session_state["np_latest_result"] = pred_res
        st.session_state["np_latest_advisories"] = advisories

    # Render results if available
    latest_result = st.session_state.get("np_latest_result")
    if latest_result is not None:
        score_val = latest_result["predicted_score"]
        score_pct = latest_result["score_percent"]
        tier = latest_result["risk_tier"]
        advisories = st.session_state.get("np_latest_advisories", [])

        st.markdown("---")
        st.markdown(
            f"""
            <div class="keel-card" style="border-top: 4px solid {'#EF4444' if tier == 'Higher Score' else ('#F59E0B' if tier == 'Moderate Score' else '#10B981')};">
                <div class="keel-card-title">📈 {t('np_results_title', lang)}</div>
                <div class="keel-card-subtitle">{t('np_results_subtitle', lang)}</div>
            """,
            unsafe_allow_html=True,
        )

        # 3 Top KPI Cards for New Prediction
        res_k1, res_k2, res_k3 = st.columns(3)

        with res_k1:
            score_color = "#F87171" if tier == "Higher Score" else ("#FBBF24" if tier == "Moderate Score" else "#34D399")
            st.markdown(
                f"""
                <div class="keel-card" style="padding: 1rem; border-left: 3px solid {score_color};">
                    <div class="keel-card-subtitle">{t('metric_pred_score', lang)}</div>
                    <div style="font-size: 2.2rem; font-weight: 800; color: {score_color}; line-height: 1.1;">
                        {score_pct:.1f}%
                    </div>
                    <div style="font-size: 0.8rem; color: {'#94A3B8' if is_dark else '#64748B'};">
                        {t('np_raw_logit_prob', lang, val=score_val)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with res_k2:
            tier_badge_bg = (
                "rgba(239, 68, 68, 0.15)" if tier == "Higher Score"
                else ("rgba(245, 158, 11, 0.15)" if tier == "Moderate Score" else "rgba(16, 185, 129, 0.15)")
            )
            tier_badge_text = (
                "#FCA5A5" if is_dark and tier == "Higher Score"
                else ("#DC2626" if tier == "Higher Score"
                else ("#FCD34D" if is_dark and tier == "Moderate Score"
                else ("#D97706" if tier == "Moderate Score"
                else ("#6EE7B7" if is_dark else "#059669"))))
            )
            st.markdown(
                f"""
                <div class="keel-card" style="padding: 1rem; border-left: 3px solid {tier_badge_text};">
                    <div class="keel-card-subtitle">{t('col_model_tier', lang)}</div>
                    <div style="margin-top: 0.4rem;">
                        <span style="background-color: {tier_badge_bg}; color: {tier_badge_text};
                                     padding: 0.35rem 0.75rem; border-radius: 9999px; font-weight: 700; font-size: 1.1rem;
                                     display: inline-block;">
                            {translate_tier(tier, lang)}
                        </span>
                    </div>
                    <div style="font-size: 0.8rem; color: {'#94A3B8' if is_dark else '#64748B'}; margin-top: 0.45rem;">
                        {t('np_thresholds_label', lang, high=high_threshold, mod=mod_threshold)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with res_k3:
            margin_val = latest_result["boundary_margin"]
            is_near = latest_result["near_boundary"]
            margin_text = f"±{margin_val*100:.1f}% ({margin_val:.3f})"
            st.markdown(
                f"""
                <div class="keel-card" style="padding: 1rem; border-left: 3px solid {'#F59E0B' if is_near else '#38BDF8'};">
                    <div class="keel-card-subtitle">{t('np_margin_label', lang)}</div>
                    <div style="font-size: 1.35rem; font-weight: 700; color: {'#FBBF24' if is_near else ('#38BDF8' if is_dark else '#0284C7')}; line-height: 1.3;">
                        {margin_text}
                    </div>
                    <div style="font-size: 0.8rem; color: {'#94A3B8' if is_dark else '#64748B'}; margin-top: 0.3rem;">
                        {'⚠️ ' + t('boundary_indicator_near', lang) if is_near else '✓ ' + t('boundary_indicator_comfortable', lang)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Advisories and Rule-Based Data Quality Checks
        dq_flags = latest_result["dq_warnings"]
        if dq_flags or advisories:
            warning_items = []
            doc_label = t("np_doc_notice", lang)
            for adv in advisories:
                warning_items.append(f"<li><strong>{doc_label}:</strong> {adv}</li>")
            for w in dq_flags:
                warning_items.append(f"<li><strong>{w['type']}:</strong> {w['text']}</li>")

            st.markdown(
                f"""
                <div style="background-color: {'rgba(245, 158, 11, 0.12)' if is_dark else '#FFFBEB'};
                            border-left: 4px solid #F59E0B; padding: 0.75rem 1rem; border-radius: 6px; margin: 1rem 0;">
                    <div style="font-weight: 700; font-size: 0.9rem; color: {'#FBBF24' if is_dark else '#B45309'}; margin-bottom: 0.35rem;">
                        ⚠️ {t('dq_title', lang)} ({len(warning_items)})
                    </div>
                    <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.85rem; color: {'#E2E8F0' if is_dark else '#1E293B'};">
                        {''.join(warning_items)}
                    </ul>
                    <div style="font-size: 0.75rem; color: {'#94A3B8' if is_dark else '#64748B'}; margin-top: 0.4rem;">
                        {t('dq_disclaimer', lang)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # -------------------------------------------------------------
        # Why this risk score? Patient-specific justification
        # -------------------------------------------------------------
        pos_factors = latest_result.get("pos_drivers", [])
        neg_factors = latest_result.get("neg_drivers", [])
        intercept_val = latest_result.get("intercept", 0.0)

        st.markdown("---")
        st.markdown(f"### 💡 {t('why_this_risk_score', lang)}")

        tier_label = translate_tier(tier, lang)
        st.markdown(
            f"**Patient Predicted Risk Probability:** `{score_pct:.1f}%` ({score_val:.4f}) &nbsp;|&nbsp; "
            f"**Assigned Risk Category:** `{tier_label}`"
        )
        st.caption(t("attribution_caption", lang))

        if not pos_factors and not neg_factors:
            st.info(f"ℹ️ {t('attribution_unavailable', lang)}")
        else:
            exp_c1, exp_c2 = st.columns(2)

            with exp_c1:
                st.markdown(f"##### 🔺 {t('factors_pushing_higher', lang)}")
                st.caption(f"{t('pos_chart_xaxis', lang)} $(\\beta_i x_i > 0)$:")
                if pos_factors:
                    for f in pos_factors:
                        st.markdown(f"- **{f['clinical_name']}**: `+{f['contribution']:.3f}` log-odds")
                    pos_df = pd.DataFrame(pos_factors)
                    pos_bar_color = "#F87171" if is_dark else "#DC2626"
                    pos_chart = (
                        alt.Chart(pos_df)
                        .mark_bar(color=pos_bar_color, cornerRadiusTopRight=4, cornerRadiusBottomRight=4)
                        .encode(
                            x=alt.X("contribution:Q", title=t("pos_chart_xaxis", lang)),
                            y=alt.Y("clinical_name:N", sort="-x", title=None),
                            tooltip=["clinical_name", alt.Tooltip("contribution:Q", format=".3f")],
                        )
                        .properties(height=180)
                    )
                    pos_chart = apply_chart_theme(pos_chart, is_dark=is_dark)
                    st.altair_chart(pos_chart, use_container_width=True, theme=None)
                else:
                    st.info(t("pos_empty_state", lang))

            with exp_c2:
                st.markdown(f"##### 🔻 {t('factors_pushing_lower', lang)}")
                st.caption(f"{t('neg_chart_xaxis', lang)} $(\\beta_i x_i < 0)$:")
                if neg_factors:
                    for f in neg_factors:
                        st.markdown(f"- **{f['clinical_name']}**: `{f['contribution']:.3f}` log-odds")
                    neg_df = pd.DataFrame(neg_factors)
                    neg_bar_color = "#34D399" if is_dark else "#059669"
                    neg_chart = (
                        alt.Chart(neg_df)
                        .mark_bar(color=neg_bar_color, cornerRadiusTopRight=4, cornerRadiusBottomRight=4)
                        .encode(
                            x=alt.X("contribution:Q", title=t("neg_chart_xaxis", lang)),
                            y=alt.Y("clinical_name:N", sort="x", title=None),
                            tooltip=["clinical_name", alt.Tooltip("contribution:Q", format=".3f")],
                        )
                        .properties(height=180)
                    )
                    neg_chart = apply_chart_theme(neg_chart, is_dark=is_dark)
                    st.altair_chart(neg_chart, use_container_width=True, theme=None)
                else:
                    st.info(t("neg_empty_state", lang))

        st.caption(f"{t('intercept_caption', lang, val=intercept_val)}")

        # Individualized Clinical Narrative Summary
        summary = latest_result["summary"]
        if summary:
            st.markdown("---")
            st.markdown(f"#### 📋 {t('summary_box_header', lang)}")
            st.markdown(
                f"""
                <div style="background-color: {'rgba(30, 41, 59, 0.7)' if is_dark else '#F8FAFC'};
                            border: 1px solid {'#334155' if is_dark else '#E2E8F0'};
                            padding: 1.15rem; border-radius: 8px; margin-top: 0.5rem;">
                    <div style="font-size: 0.95rem; line-height: 1.5; color: {'#F1F5F9' if is_dark else '#0F172A'};">
                        {summary['overview']}
                    </div>
                    <div style="margin-top: 0.85rem; font-weight: 700; font-size: 0.88rem; color: {'#94A3B8' if is_dark else '#475569'};">
                        {t('summary_box_factors_title', lang)}:
                    </div>
                    <ul style="margin: 0.35rem 0 0 1.25rem; font-size: 0.88rem; color: {'#E2E8F0' if is_dark else '#334155'};">
                        {''.join(f'<li>{f}</li>' for f in summary['key_factors'])}
                    </ul>
                    <div style="margin-top: 0.85rem; font-weight: 700; font-size: 0.88rem; color: {'#94A3B8' if is_dark else '#475569'};">
                        {t('summary_box_followup_label', lang)}:
                    </div>
                    <div style="margin-top: 0.25rem; font-size: 0.88rem; color: {'#CBD5E1' if is_dark else '#1E293B'};">
                        {summary['follow_up']}
                    </div>
                    <div style="margin-top: 0.85rem; font-size: 0.76rem; color: {'#64748B' if is_dark else '#94A3B8'}; border-top: 1px dashed {'#334155' if is_dark else '#E2E8F0'}; padding-top: 0.5rem;">
                        {summary['disclaimer']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)
