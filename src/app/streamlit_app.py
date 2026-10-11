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
    RAW_DIABETIC_DATA_PATH,
    SAVED_MODELS_DIR,
)
from src.data.load_data import load_raw_data
from src.features.preprocessing import (
    filter_modeling_cohort,
    get_feature_manifest,
)
from src.app.translations import (
    CLINICAL_DOMAINS_TRANSLATION,
    DIAG_CATEGORY_TRANSLATIONS,
    FEATURE_TRANSLATIONS,
    LANGUAGES,
    TIER_TRANSLATIONS,
    get_action_word,
    get_summary_context,
    get_summary_disclaimer,
    get_summary_factor,
    get_summary_followup,
    get_summary_followup_wrapped,
    get_summary_tier_intro,
    t,
    translate_driver_label,
    translate_tier,
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

def get_theme_css(is_dark: bool) -> str:
    """Generates cohesive healthcare-inspired CSS tailored for Light Mode or Dark Mode."""
    if is_dark:
        bg_main = "#0F172A"            # Deep slate navy
        bg_sidebar = "#1E293B"         # Slate-800
        bg_card = "#1E293B"            # Slate-800
        text_main = "#F8FAFC"          # Slate-50
        text_secondary = "#E2E8F0"     # Slate-200
        text_muted = "#94A3B8"         # Slate-400
        border_color = "#334155"       # Slate-700
        card_shadow = "0 2px 6px rgba(0, 0, 0, 0.35)"

        badge_color = "#2DD4BF"        # Luminous Teal
        badge_bg = "#134E4A"           # Teal-900
        badge_border = "#0F766E"       # Teal-700

        priority_bg = "#0284C7"        # Sky-600
        priority_label_color = "#BAE6FD" # Sky-100

        disclaimer_bg = "#451A03"      # Deep Amber-950
        disclaimer_border = "#F59E0B"  # Amber-500
        disclaimer_text = "#FDE68A"    # Amber-200

        capacity_bg = "#334155"        # Slate-700

        summary_box_bg = "#0B132B"     # Deep Midnight Navy
        summary_box_border = "#14B8A6" # Teal-500
        summary_fu_bg = "#0F172A"      # Slate-900
        summary_fu_text = "#F1F5F9"    # Slate-100

        badge_high_bg = "#450A0A"
        badge_high_text = "#F87171"
        badge_high_border = "#7F1D1D"

        badge_mod_bg = "#451A03"
        badge_mod_text = "#FBBF24"
        badge_mod_border = "#78350F"

        badge_low_bg = "#064E3B"
        badge_low_text = "#34D399"
        badge_low_border = "#065F46"

        tab_active = "#2DD4BF"
        tab_inactive = "#94A3B8"
        input_bg = "#1E293B"
        table_header_bg = "#0F172A"
        code_bg = "#0F172A"
        code_text = "#38BDF8"
    else:
        bg_main = "#F8FAFC"            # Slate-50 off-white
        bg_sidebar = "#FFFFFF"
        bg_card = "#FFFFFF"
        text_main = "#0F172A"          # Slate-900
        text_secondary = "#334155"     # Slate-700
        text_muted = "#64748B"         # Slate-500
        border_color = "#E2E8F0"       # Slate-200
        card_shadow = "0 1px 3px rgba(0, 0, 0, 0.04)"

        badge_color = "#0D9488"        # Teal-600
        badge_bg = "#F0FDFA"           # Teal-50
        badge_border = "#CCFBF1"       # Teal-100

        priority_bg = "#0F172A"        # Slate-900
        priority_label_color = "#38BDF8" # Sky-400

        disclaimer_bg = "#FEF3C7"      # Amber-100
        disclaimer_border = "#D97706"  # Amber-600
        disclaimer_text = "#92400E"    # Amber-800

        capacity_bg = "#F1F5F9"        # Slate-100

        summary_box_bg = "#F8FAFC"     # Slate-50
        summary_box_border = "#0D9488" # Teal-600
        summary_fu_bg = "#FFFFFF"
        summary_fu_text = "#1E293B"    # Slate-800

        badge_high_bg = "#FEF2F2"
        badge_high_text = "#DC2626"
        badge_high_border = "#FEE2E2"

        badge_mod_bg = "#FFFBEB"
        badge_mod_text = "#D97706"
        badge_mod_border = "#FEF3C7"

        badge_low_bg = "#ECFDF5"
        badge_low_text = "#059669"
        badge_low_border = "#D1FAE5"

        tab_active = "#0D9488"
        tab_inactive = "#64748B"
        input_bg = "#FFFFFF"
        table_header_bg = "#F8FAFC"
        code_bg = "#F1F5F9"
        code_text = "#0F172A"

    return f"""
<style>
    /* Global App Background and Typography */
    .stApp, [data-testid="stAppViewContainer"], .main {{
        background-color: {bg_main} !important;
        color: {text_main} !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }}
    
    /* Sidebar Styling */
    [data-testid="stSidebar"], [data-testid="stSidebarContent"], section[data-testid="stSidebar"] {{
        background-color: {bg_sidebar} !important;
        border-right: 1px solid {border_color} !important;
    }}
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4, [data-testid="stSidebar"] h5, [data-testid="stSidebar"] h6 {{
        color: {text_main} !important;
    }}
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {{
        color: {text_secondary} !important;
    }}
    [data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {{
        color: {text_muted} !important;
    }}
    [data-testid="stSidebar"] hr {{
        border-color: {border_color} !important;
    }}

    /* Header Container */
    .keel-header {{
        padding: 0.5rem 0rem 1.25rem 0rem;
        border-bottom: 1px solid {border_color};
        margin-bottom: 1.5rem;
    }}
    .keel-badge-tag {{
        display: inline-block;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: {badge_color};
        background-color: {badge_bg};
        padding: 0.2rem 0.6rem;
        border-radius: 9999px;
        border: 1px solid {badge_border};
        margin-bottom: 0.4rem;
    }}
    .keel-title {{
        font-size: 2.1rem;
        font-weight: 800;
        color: {text_main};
        letter-spacing: -0.02em;
        margin: 0;
        line-height: 1.2;
    }}
    .keel-subtitle {{
        font-size: 0.95rem;
        color: {text_muted};
        margin-top: 0.25rem;
        margin-bottom: 0rem;
    }}
    
    /* Metric Pill Header Badges */
    .header-metric-card {{
        background: {bg_card};
        border: 1px solid {border_color};
        border-radius: 12px;
        padding: 0.65rem 1rem;
        text-align: right;
        box-shadow: {card_shadow};
    }}
    .header-metric-label {{
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: {text_muted};
    }}
    .header-metric-value {{
        font-size: 1.35rem;
        font-weight: 800;
        color: {text_main};
    }}
    .header-priority-pill {{
        background: {priority_bg};
        color: #FFFFFF;
        border-radius: 12px;
        padding: 0.65rem 1.1rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(15, 23, 42, 0.25);
    }}
    .header-priority-label {{
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        color: {priority_label_color};
    }}
    .header-priority-value {{
        font-size: 1.35rem;
        font-weight: 800;
        color: #FFFFFF;
    }}

    /* Clinical Disclaimer Alert Banner */
    .keel-disclaimer-banner {{
        background-color: {disclaimer_bg};
        border-left: 4px solid {disclaimer_border};
        padding: 0.75rem 1rem;
        border-radius: 6px;
        margin-bottom: 1.5rem;
        font-size: 0.85rem;
        color: {disclaimer_text};
        line-height: 1.45;
    }}
    
    /* Card Wrapper */
    .keel-card {{
        background-color: {bg_card};
        border: 1px solid {border_color};
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1.25rem;
        box-shadow: {card_shadow};
    }}
    .keel-card-title {{
        font-size: 1.1rem;
        font-weight: 700;
        color: {text_main};
        margin-bottom: 0.25rem;
    }}
    .keel-card-subtitle {{
        font-size: 0.82rem;
        color: {text_muted};
        margin-bottom: 0.85rem;
    }}
    
    /* KPI Metrics in Header */
    .kpi-metric-val {{
        font-size: 1.6rem;
        font-weight: 800;
        color: {text_main};
    }}
    .kpi-metric-sub {{
        font-size: 0.75rem;
        color: {text_muted};
    }}
    .table-capacity-badge {{
        font-size: 0.72rem;
        color: {text_muted};
        background: {capacity_bg};
        padding: 0.25rem 0.6rem;
        border-radius: 9999px;
    }}

    /* Score Badges */
    .score-badge-high {{
        background-color: {badge_high_bg};
        color: {badge_high_text};
        font-weight: 700;
        padding: 0.2rem 0.5rem;
        border-radius: 6px;
        border: 1px solid {badge_high_border};
        display: inline-block;
    }}
    .score-badge-mod {{
        background-color: {badge_mod_bg};
        color: {badge_mod_text};
        font-weight: 700;
        padding: 0.2rem 0.5rem;
        border-radius: 6px;
        border: 1px solid {badge_mod_border};
        display: inline-block;
    }}
    .score-badge-low {{
        background-color: {badge_low_bg};
        color: {badge_low_text};
        font-weight: 700;
        padding: 0.2rem 0.5rem;
        border-radius: 6px;
        border: 1px solid {badge_low_border};
        display: inline-block;
    }}

    /* Patient Summary Callout Card */
    .patient-summary-box {{
        background-color: {summary_box_bg};
        border: 1px solid {border_color};
        border-left: 4px solid {summary_box_border};
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-top: 0.85rem;
        margin-bottom: 1.25rem;
    }}
    .patient-summary-header {{
        font-size: 1.05rem;
        font-weight: 700;
        color: {text_main};
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }}
    .patient-summary-overview {{
        font-size: 0.92rem;
        color: {text_secondary};
        line-height: 1.5;
        margin-bottom: 0.75rem;
    }}
    .patient-summary-factors-title {{
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: {text_muted};
        margin-top: 0.6rem;
        margin-bottom: 0.35rem;
    }}
    .patient-summary-factors-list {{
        margin: 0.25rem 0 0.65rem 1.25rem;
        padding: 0;
        color: {text_secondary};
        font-size: 0.88rem;
        line-height: 1.5;
    }}
    .patient-summary-factors-list li {{
        margin-bottom: 0.35rem;
    }}
    .patient-summary-followup {{
        background-color: {summary_fu_bg};
        border: 1px solid {border_color};
        border-radius: 6px;
        padding: 0.65rem 0.85rem;
        margin-top: 0.65rem;
        font-size: 0.86rem;
        color: {summary_fu_text};
        line-height: 1.45;
    }}
    .patient-summary-disclaimer {{
        font-size: 0.75rem;
        color: {text_muted};
        margin-top: 0.45rem;
        font-style: italic;
        line-height: 1.35;
    }}

    /* Streamlit Native Element Theming */
    h1, h2, h3, h4, h5, h6, [data-testid="stHeadingWithActionElements"] {{
        color: {text_main} !important;
    }}
    p, span, div[data-testid="stMarkdownContainer"] > p, div[data-testid="stMarkdownContainer"] > ul > li {{
        color: {text_secondary};
    }}
    div[data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] p {{
        color: {text_muted} !important;
    }}
    [data-testid="stMetricValue"] {{
        color: {text_main} !important;
    }}
    [data-testid="stMetricLabel"] {{
        color: {text_muted} !important;
    }}
    hr {{
        border-color: {border_color} !important;
    }}

    /* Tabs Styling */
    button[data-baseweb="tab"] {{
        color: {tab_inactive} !important;
        background-color: transparent !important;
    }}
    button[data-baseweb="tab"][aria-selected="true"] {{
        color: {tab_active} !important;
    }}
    [data-baseweb="tab-highlight"] {{
        background-color: {tab_active} !important;
    }}
    [data-baseweb="tab-border"] {{
        background-color: {border_color} !important;
    }}

    /* Inputs, Selectbox, and Popover Menus */
    [data-baseweb="select"] > div {{
        background-color: {input_bg} !important;
        border-color: {border_color} !important;
        color: {text_main} !important;
    }}
    [data-baseweb="popover"], [data-baseweb="menu"] {{
        background-color: {input_bg} !important;
        color: {text_main} !important;
    }}
    [data-testid="stSlider"] label {{
        color: {text_main} !important;
    }}

    /* Tables and DataFrames */
    .stDataFrame {{
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid {border_color};
    }}
    [data-testid="stTable"] table {{
        background-color: {bg_card} !important;
        color: {text_main} !important;
        border-color: {border_color} !important;
    }}
    [data-testid="stTable"] th {{
        background-color: {table_header_bg} !important;
        color: {text_main} !important;
        border-color: {border_color} !important;
    }}
    [data-testid="stTable"] td {{
        border-color: {border_color} !important;
        color: {text_main} !important;
    }}
    code {{
        background-color: {code_bg} !important;
        color: {code_text} !important;
        border: 1px solid {border_color} !important;
    }}
</style>
"""


def apply_chart_theme(chart: alt.Chart, is_dark: bool) -> alt.Chart:
    """Applies theme-aligned background, axis typography, grid, and stroke to Altair charts."""
    label_color = "#94A3B8" if is_dark else "#475569"
    title_color = "#F8FAFC" if is_dark else "#1E293B"
    grid_color = "#334155" if is_dark else "#E2E8F0"
    domain_color = "#475569" if is_dark else "#CBD5E1"
    stroke_color = "#334155" if is_dark else "#E2E8F0"

    return (
        chart
        .configure(background="transparent")
        .configure_axis(
            labelColor=label_color,
            titleColor=title_color,
            gridColor=grid_color,
            domainColor=domain_color,
            tickColor=domain_color,
            labelFontSize=11,
            titleFontSize=12,
        )
        .configure_view(
            stroke=stroke_color,
        )
    )


def render_chart_data_toggle(key: str, lang: str = "English") -> str:
    """
    Renders an explicit, visible, reversible Graph / Data toggle for charts.
    Uses canonical string keys ('graph', 'data') to ensure stability across
    language changes without throwing Streamlit option value exceptions.
    """
    label_map = {
        "graph": f"📊 {t('btn_graph', lang)}",
        "data": f"📋 {t('btn_data', lang)}",
    }
    if hasattr(st, "segmented_control"):
        mode = st.segmented_control(
            label=t("lbl_view_mode", lang),
            options=["graph", "data"],
            default="graph",
            format_func=lambda x: label_map.get(x, x),
            key=key,
            label_visibility="collapsed",
        )
        return mode or "graph"
    else:
        mode = st.radio(
            label=t("lbl_view_mode", lang),
            options=["graph", "data"],
            index=0,
            horizontal=True,
            format_func=lambda x: label_map.get(x, x),
            key=key,
            label_visibility="collapsed",
        )
        return mode or "graph"


# -----------------------------------------------------------------------------
# Preferences & Query Parameters Initialization (Persist across browser refresh)
# -----------------------------------------------------------------------------
LANG_PARAM_MAP = {
    "english": "English", "en": "English",
    "हिन्दी": "हिन्दी", "hindi": "हिन्दी", "hi": "हिन्दी",
    "ಕನ್ನಡ": "ಕನ್ನಡ", "kannada": "ಕನ್ನಡ", "kn": "ಕನ್ನಡ",
}

if "language" not in st.session_state:
    raw_lang = str(st.query_params.get("lang", "")).strip().lower()
    restored_lang = LANG_PARAM_MAP.get(raw_lang, "English")
    st.session_state["language"] = restored_lang

if "theme" not in st.session_state:
    raw_theme = str(st.query_params.get("theme", "")).strip().lower()
    restored_theme = "Dark Mode" if raw_theme in ["dark", "dark mode"] else "Light Mode"
    st.session_state["theme"] = restored_theme

if "dark_mode_toggle" not in st.session_state:
    st.session_state["dark_mode_toggle"] = (st.session_state["theme"] == "Dark Mode")

is_dark_global = (st.session_state.get("theme", "Light Mode") == "Dark Mode")
st.markdown(get_theme_css(is_dark_global), unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# Cached Model, Metadata, and Dataset Loaders
# -----------------------------------------------------------------------------
def get_file_mtime(file_path: Path) -> float:
    """Returns file modification timestamp or 0.0 if not found, for cache key invalidation."""
    try:
        return file_path.stat().st_mtime if file_path.exists() else 0.0
    except OSError:
        return 0.0


@st.cache_resource(show_spinner="Loading trained baseline model...")
def _load_model_cached(model_path_str: str, mtime: float) -> Tuple[Any, Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """Loads model pipeline, metadata, and metrics keyed on path and modification time."""
    model_file = Path(model_path_str)
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


def load_trained_model_pipeline(
    model_path: Optional[Path | str] = None,
) -> Tuple[Any, Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """
    Loads the serialized Logistic Regression pipeline and associated metadata/metrics.
    Cache key incorporates model path and file modification time to prevent stale cache.
    Returns:
        (pipeline, metadata_dict, metrics_dict)
    """
    target_path = Path(model_path) if model_path is not None else (SAVED_MODELS_DIR / "baseline_logistic_regression.joblib")
    mtime = get_file_mtime(target_path)
    return _load_model_cached(str(target_path), mtime)


@st.cache_data(show_spinner="Ingesting cohort encounters & generating risk predictions...")
def _get_scored_cohort_cached(
    data_path_str: str,
    data_mtime: float,
    model_path_str: str,
    model_mtime: float,
    _pipeline: Any,
) -> Optional[pd.DataFrame]:
    try:
        raw_df = load_raw_data(data_path_str)
    except Exception as exc:
        st.error(f"Error loading raw dataset from {data_path_str}: {exc}")
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

    if _pipeline is None:
        st.error("Model pipeline could not be loaded.")
        return None

    # Prepare input matrix
    X = cohort_df[feature_cols].copy()

    # Generate positive class predicted probabilities
    probabilities = _pipeline.predict_proba(X)[:, 1]

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

    # Derive top clinical driver label for quick table scanning (fast array iteration)
    scored_df["top_driver"] = derive_top_driver_labels(scored_df)

    # Separate binary historical outcome field (strictly for retrospective validation; never a feature)
    scored_df["historical_readmit_30d"] = (cohort_df["readmitted"] == "<30").astype(int).values

    # Pre-sort cohort descending by predicted_score once so reruns never re-sort 99k rows
    scored_df = scored_df.sort_values(by="predicted_score", ascending=False).reset_index(drop=True)

    return scored_df


def load_and_score_cohort(
    data_path: Optional[Path | str] = None,
    model_path: Optional[Path | str] = None,
) -> Optional[pd.DataFrame]:
    """
    Loads raw dataset, applies identical cohort eligibility rules (excluding terminal cases),
    extracts the exact features expected by the trained pipeline, computes predictions,
    and returns encounters pre-sorted by predicted readmission risk.
    """
    target_data = Path(data_path) if data_path is not None else RAW_DIABETIC_DATA_PATH
    target_model = Path(model_path) if model_path is not None else (SAVED_MODELS_DIR / "baseline_logistic_regression.joblib")

    data_mtime = get_file_mtime(target_data)
    model_mtime = get_file_mtime(target_model)

    pipeline, _, _ = load_trained_model_pipeline(target_model)
    if pipeline is None:
        st.error("Model pipeline could not be loaded from models/saved/baseline_logistic_regression.joblib.")
        return None

    return _get_scored_cohort_cached(
        str(target_data),
        data_mtime,
        str(target_model),
        model_mtime,
        _pipeline=pipeline,
    )


def derive_top_driver_labels(df: pd.DataFrame) -> List[str]:
    """
    Derives an interpretable, patient-specific primary risk driver label
    based on the dominant clinical risk indicators of the baseline model.
    Optimized to iterate through NumPy arrays for fast vectorized execution.
    """
    inpatient = df["num_inpatient"].to_numpy()
    emergency = df["num_emergency"].to_numpy()
    insulin = df["insulin"].to_numpy()
    age = df["age_group"].astype(str).to_numpy()
    los = df["length_of_stay"].to_numpy()
    change = df["change"].to_numpy()
    num_meds = df["num_medications"].to_numpy()

    drivers = []
    for inp, emg, ins, a, l, chg, med in zip(
        inpatient, emergency, insulin, age, los, change, num_meds
    ):
        if inp >= 2:
            drivers.append(f"Past Inpatient ({inp} visits)")
        elif emg >= 2:
            drivers.append(f"Frequent ER Utilization ({emg} visits)")
        elif inp == 1:
            drivers.append("Recent Inpatient Admission (1 visit)")
        elif ins in ["Up", "Down"]:
            drivers.append(f"Insulin Instability ({ins})")
        elif a in ["[70-80)", "[80-90)", "[90-100)"]:
            drivers.append(f"Geriatric Vulnerability ({a})")
        elif l >= 7:
            drivers.append(f"Extended Hospital Stay ({l}d)")
        elif chg == "Ch":
            drivers.append("Medication Regimen Adjusted")
        elif med >= 20:
            drivers.append("High Polypharmacy (>20 meds)")
        else:
            drivers.append("Chronic Glycemic / Comorbid Burden")
    return drivers


def compute_score_histogram_bins(scores_arr: np.ndarray, bins: int = 25) -> pd.DataFrame:
    """
    Pre-aggregates predicted score probabilities into histogram bins using NumPy.
    Returns a compact DataFrame (25 rows) suitable for fast Altair rendering without
    serializing the full cohort across the Streamlit websocket.
    """
    if len(scores_arr) == 0:
        return pd.DataFrame(columns=["bin_start", "bin_end", "count", "pct"])
    counts, bin_edges = np.histogram(scores_arr, bins=bins)
    total = len(scores_arr)
    pcts = (counts / total * 100.0) if total > 0 else np.zeros_like(counts, dtype=float)
    return pd.DataFrame({
        "bin_start": bin_edges[:-1],
        "bin_end": bin_edges[1:],
        "count": counts,
        "pct": pcts,
    })


@st.cache_data
def compute_domain_importance(_pipeline: Any, lang: str = "English") -> pd.DataFrame:
    """
    Computes normalized relative predictive weight (0-100 index) for major clinical
    domains directly from the fitted logistic regression standardized coefficients.
    """
    try:
        preprocessor = _pipeline.named_steps["preprocessor"]
        classifier = _pipeline.named_steps["classifier"]
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

        res_df = df_dom.sort_values(by="Relative Influence", ascending=False).reset_index(drop=True)
        if lang != "English":
            res_df["Clinical Domain"] = res_df["Clinical Domain"].apply(
                lambda d: CLINICAL_DOMAINS_TRANSLATION.get(d, {}).get(lang, d)
            )
        return res_df
    except Exception:
        fallback_domains = [
            "Age & Demographics",
            "Medication Adjustments",
            "Clinical Comorbidities",
            "Past Utilization (Inpatient/ER)",
            "Diagnostic Testing Volume",
            "Inpatient Stay Duration",
        ]
        if lang != "English":
            fallback_domains = [
                CLINICAL_DOMAINS_TRANSLATION.get(d, {}).get(lang, d) for d in fallback_domains
            ]
        return pd.DataFrame({
            "Clinical Domain": fallback_domains,
            "Relative Influence": [100, 51, 42, 24, 15, 5],
        })


def compute_local_explanation(
    pipeline: Any,
    encounter_row_features: pd.DataFrame,
    top_n: int = 5,
    lang: str = "English",
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
                clean_name = format_friendly_feature_name(name, lang=lang)
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


def format_friendly_feature_name(raw_name: str, lang: str = "English") -> str:
    """Translates raw preprocessed feature strings into clean clinical descriptors."""
    clean = raw_name.replace("cat__", "").replace("num__", "")
    if clean in FEATURE_TRANSLATIONS:
        return FEATURE_TRANSLATIONS[clean].get(lang, FEATURE_TRANSLATIONS[clean]["English"])
    if clean.startswith("age_"):
        bracket = clean.replace("age_", "")
        if lang == "हिन्दी":
            return f"रोगी आयु वर्ग ({bracket} वर्ष)"
        elif lang == "ಕನ್ನಡ":
            return f"ರೋಗಿಯ ವಯಸ್ಸಿನ ವರ್ಗ ({bracket} ವರ್ಷಗಳು)"
        return f"Patient Age Bracket ({bracket} years)"
    clean_title = clean.replace("_", " ").title()
    return clean_title


def format_primary_diag(diag_val: Any, lang: str = "English") -> str:
    """Translates raw ICD-9 primary diagnosis code into an interpretable clinical category."""
    if pd.isna(diag_val) or diag_val is None:
        cat_key = "Not documented in billing records"
        return DIAG_CATEGORY_TRANSLATIONS.get(cat_key, {}).get(lang, cat_key)
    s = str(diag_val).strip()
    if s in ["?", "", "Missing", "None", "nan"]:
        cat_key = "Not documented in billing records"
        return DIAG_CATEGORY_TRANSLATIONS.get(cat_key, {}).get(lang, cat_key)
    if s.startswith("V") or s.startswith("E"):
        cat_key = "Supplemental / external factor code"
        return DIAG_CATEGORY_TRANSLATIONS.get(cat_key, {}).get(lang, cat_key)
    try:
        code = float(s)
    except ValueError:
        if lang == "हिन्दी":
            return f"ICD-9 कोड {s}"
        elif lang == "ಕನ್ನಡ":
            return f"ICD-9 ಕೋಡ್ {s}"
        return f"ICD-9 code {s}"

    if (390 <= code <= 459) or code == 785:
        cat_key = "Circulatory / cardiovascular condition"
    elif (460 <= code <= 519) or code == 786:
        cat_key = "Respiratory condition"
    elif (520 <= code <= 579) or code == 787:
        cat_key = "Digestive condition"
    elif 250 <= code < 251:
        cat_key = "Diabetes mellitus"
    elif 800 <= code <= 999:
        cat_key = "Injury / trauma"
    elif 710 <= code <= 739:
        cat_key = "Musculoskeletal condition"
    elif (580 <= code <= 629) or code == 788:
        cat_key = "Genitourinary condition"
    elif 140 <= code <= 239:
        cat_key = "Neoplasm / oncology"
    else:
        if lang == "हिन्दी":
            return f"ICD-9 स्थिति (कोड {s})"
        elif lang == "ಕನ್ನಡ":
            return f"ICD-9 ಸ್ಥಿತಿ (ಕೋಡ್ {s})"
        return f"ICD-9 condition (code {s})"

    return DIAG_CATEGORY_TRANSLATIONS.get(cat_key, {}).get(lang, cat_key)


def check_patient_data_quality(selected_row: pd.Series, lang: str = "English") -> List[Dict[str, str]]:
    """
    Performs basic, rule-based data-quality and outlier checks on a single patient record.
    Checks for:
      - Missing A1C test record
      - Missing or unrecorded primary diagnosis
      - Extreme acute healthcare utilization (inpatient/ER visits)
      - Extreme length of stay (near or at dataset truncation ceiling)
      - Extreme medication count (high polypharmacy)

    Note: These are baseline heuristic checks for demo review and do not represent
    comprehensive clinical data validation or error certification.
    """
    warnings_list: List[Dict[str, str]] = []

    def _safe_int(val: Any) -> int:
        if pd.isna(val) or val is None:
            return 0
        try:
            return max(0, int(val))
        except (ValueError, TypeError):
            return 0

    # 1. Missing A1C record
    a1c_val = str(selected_row.get("a1c_result_display", "")).strip().lower()
    if a1c_val in ["none", "nan", "", "unknown"]:
        warnings_list.append({
            "type": t("dq_type_missing_lab", lang),
            "text": t("dq_missing_a1c", lang),
        })

    # 2. Missing Primary Diagnosis
    diag_val = str(selected_row.get("primary_diag", "")).strip()
    if diag_val in ["?", "", "nan", "None", "Unknown"]:
        warnings_list.append({
            "type": t("dq_type_missing_diag", lang),
            "text": t("dq_missing_diag", lang),
        })

    # 3. Extreme Prior Utilization (>= 6 inpatient or >= 6 ER visits)
    inp = _safe_int(selected_row.get("num_inpatient", 0))
    emg = _safe_int(selected_row.get("num_emergency", 0))
    if inp >= 6 or emg >= 6:
        warnings_list.append({
            "type": t("dq_type_unusual_util", lang),
            "text": t("dq_unusual_util", lang, inpatient=inp, emergency=emg),
        })

    # 4. Extreme Hospital Stay (>= 12 days; dataset truncation is 14)
    los = _safe_int(selected_row.get("length_of_stay", 0))
    if los >= 12:
        warnings_list.append({
            "type": t("dq_type_unusual_stay", lang),
            "text": t("dq_unusual_stay", lang, days=los),
        })

    # 5. Extreme Polypharmacy (>= 35 medications)
    meds = _safe_int(selected_row.get("num_medications", 0))
    if meds >= 35:
        warnings_list.append({
            "type": t("dq_type_unusual_meds", lang),
            "text": t("dq_unusual_meds", lang, meds=meds),
        })

    return warnings_list


def compute_retrospective_top_k_metrics(
    df_scored: pd.DataFrame,
    k_values: Tuple[int, int] = (10, 20),
) -> Dict[str, Any]:
    """
    Computes retrospective early readmission metrics on historical records (<30d)
    for the top K1 and top K2 model-ranked encounters.

    Precision@K is defined strictly as:
        (Historical early readmissions within top K) / K
    """
    if "historical_readmit_30d" not in df_scored.columns:
        return {}

    n_total = len(df_scored)
    targets = df_scored["historical_readmit_30d"].values

    k1, k2 = k_values
    actual_k1 = min(k1, n_total)
    actual_k2 = min(k2, n_total)

    hits_k1 = int(targets[:actual_k1].sum()) if actual_k1 > 0 else 0
    prec_k1 = float(hits_k1 / actual_k1) if actual_k1 > 0 else 0.0

    hits_k2 = int(targets[:actual_k2].sum()) if actual_k2 > 0 else 0
    prec_k2 = float(hits_k2 / actual_k2) if actual_k2 > 0 else 0.0

    additional_hits = hits_k2 - hits_k1

    return {
        "k1": k1,
        "actual_k1": actual_k1,
        "hits_k1": hits_k1,
        "prec_k1": prec_k1,
        "k2": k2,
        "actual_k2": actual_k2,
        "hits_k2": hits_k2,
        "prec_k2": prec_k2,
        "additional_hits": additional_hits,
        "total_cohort": n_total,
    }


def generate_patient_summary(
    selected_row: pd.Series,
    selected_score: float,
    selected_tier: str,
    pos_factors: List[Dict[str, Any]],
    neg_factors: List[Dict[str, Any]],
    lang: str = "English",
) -> Dict[str, Any]:
    """
    Generates an individualized, deterministic clinical decision-support summary
    for the selected encounter without external LLM calls.

    Supports English, Hindi, and Kannada using centralized localized templates.
    Reflects the encounter's actual model score and priority tier using cautious language,
    distinguishes positive drivers from score-lowering factors using local model
    attribution results, and tailors transitional care considerations to recorded data.

    Returns:
        Dict[str, Any]: Keys: 'overview', 'key_factors', 'follow_up', 'disclaimer'
    """
    # -------------------------------------------------------------------------
    # Safe Value Extraction & Type Normalization
    # -------------------------------------------------------------------------
    try:
        score_val = float(selected_score)
        if np.isnan(score_val):
            score_val = 0.5
    except (ValueError, TypeError):
        score_val = 0.5

    score_pct = round(score_val * 100, 1)

    if not isinstance(selected_tier, str) or not selected_tier.strip():
        if score_val >= 0.70:
            selected_tier = "Higher Score"
        elif score_val >= 0.40:
            selected_tier = "Moderate Score"
        else:
            selected_tier = "Lower Score"

    def _safe_int(val: Any, default: int = 0) -> int:
        if pd.isna(val) or val is None:
            return default
        try:
            return max(0, int(val))
        except (ValueError, TypeError):
            return default

    def _safe_str(val: Any, default: str = "") -> str:
        if pd.isna(val) or val is None:
            return default
        s = str(val).strip()
        return default if s in ["", "nan", "None"] else s

    num_inpatient = _safe_int(selected_row.get("num_inpatient", 0))
    num_emergency = _safe_int(selected_row.get("num_emergency", 0))
    num_outpatient = _safe_int(selected_row.get("num_outpatient", 0))
    length_of_stay = _safe_int(selected_row.get("length_of_stay", 0))
    num_medications = _safe_int(selected_row.get("num_medications", 0))
    num_diagnoses = _safe_int(selected_row.get("number_diagnoses", 0))
    num_procedures = _safe_int(selected_row.get("num_procedures", 0))

    insulin_val = _safe_str(selected_row.get("insulin"), "No")
    change_val = _safe_str(selected_row.get("change"), "No")
    diabetes_med = _safe_str(selected_row.get("diabetes_med"), "No")
    age_bracket = _safe_str(selected_row.get("age_group"), "Unknown")
    a1c_display = _safe_str(selected_row.get("a1c_result_display"), "None")
    glu_display = _safe_str(selected_row.get("max_glu_serum_display"), "None")
    diag_desc = format_primary_diag(selected_row.get("primary_diag", ""), lang=lang)

    # Local attribution lookup maps
    pos_map: Dict[str, float] = {}
    for f in (pos_factors or []):
        raw = f.get("raw_feature", "")
        contrib = float(f.get("contribution", 0.0))
        if raw and contrib > 0:
            pos_map[raw] = contrib

    neg_map: Dict[str, float] = {}
    for f in (neg_factors or []):
        raw = f.get("raw_feature", "")
        contrib = float(f.get("contribution", 0.0))
        if raw and contrib < 0:
            neg_map[raw] = abs(contrib)

    # -------------------------------------------------------------------------
    # 1. Plain-English / Localized Overview
    # -------------------------------------------------------------------------
    if score_val >= 0.85:
        tier_intro = get_summary_tier_intro("highest_tier", score_pct, selected_tier, lang)
    elif selected_tier == "Higher Score":
        tier_intro = get_summary_tier_intro("higher_tier", score_pct, selected_tier, lang)
    elif score_val >= 0.50:
        tier_intro = get_summary_tier_intro("mod_high", score_pct, selected_tier, lang)
    elif selected_tier == "Moderate Score":
        tier_intro = get_summary_tier_intro("mod_tier", score_pct, selected_tier, lang)
    elif score_val >= 0.20:
        tier_intro = get_summary_tier_intro("lower_mod", score_pct, selected_tier, lang)
    else:
        tier_intro = get_summary_tier_intro("lowest_tier", score_pct, selected_tier, lang)

    # Specific contextual narrative tailored to encounter utilization pattern
    if num_inpatient >= 3 or num_emergency >= 3:
        context_sentence = get_summary_context("frequent_acute", num_inpatient, num_emergency, lang)
    elif num_inpatient >= 1 and num_emergency == 0:
        context_sentence = get_summary_context("inpatient_only", num_inpatient, num_emergency, lang)
    elif num_inpatient == 0 and num_emergency >= 1:
        context_sentence = get_summary_context("emergency_only", num_inpatient, num_emergency, lang)
    elif num_inpatient >= 1 and num_emergency >= 1:
        context_sentence = get_summary_context("both_moderate", num_inpatient, num_emergency, lang)
    else:  # num_inpatient == 0 and num_emergency == 0
        if selected_tier == "Higher Score":
            context_sentence = get_summary_context("zero_util_high", num_inpatient, num_emergency, lang)
        elif selected_tier == "Moderate Score":
            context_sentence = get_summary_context("zero_util_mod", num_inpatient, num_emergency, lang)
        else:
            context_sentence = get_summary_context("zero_util_low", num_inpatient, num_emergency, lang)

    overview = f"{tier_intro} {context_sentence}"

    # -------------------------------------------------------------------------
    # 2. Extract Meaningful Factors Distinguishing Higher vs Lower Score Attribution
    # -------------------------------------------------------------------------
    candidates: List[Dict[str, Any]] = []

    # Category: Prior Utilization
    if num_inpatient > 0 or num_emergency > 0:
        util_contrib = pos_map.get("num__number_inpatient", 0.0) + pos_map.get("num__number_emergency", 0.0)
        util_imp = 5.0 + util_contrib * 2.5 + num_inpatient * 0.15 + num_emergency * 0.05
        if num_inpatient >= 3 and num_emergency >= 3:
            util_text = get_summary_factor("util_pos_frequent", lang, inpatient=num_inpatient, emergency=num_emergency)
        elif num_inpatient > 0 and num_emergency > 0:
            util_text = get_summary_factor("util_pos_both", lang, inpatient=num_inpatient, emergency=num_emergency)
        elif num_inpatient > 0 and num_emergency == 0:
            util_text = get_summary_factor("util_pos_inp_only", lang, inpatient=num_inpatient)
        else:
            util_text = get_summary_factor("util_pos_er_only", lang, emergency=num_emergency)
        candidates.append({"category": "utilization", "direction": "pos", "importance": util_imp, "text": util_text})
    else:
        util_contrib = neg_map.get("num__number_inpatient", 0.0) + neg_map.get("num__number_emergency", 0.0)
        util_imp = 4.0 + util_contrib * 2.5
        util_text = get_summary_factor("util_neg_zero", lang)
        candidates.append({"category": "utilization", "direction": "neg", "importance": util_imp, "text": util_text})

    # Category: Glycemic Medications & Adjustments
    if insulin_val in ["Up", "Down"]:
        action_word = get_action_word("escalated" if insulin_val == "Up" else "reduced", lang)
        ins_contrib = pos_map.get(f"cat__insulin_{insulin_val}", 0.0)
        ins_imp = 4.5 + ins_contrib * 2.5
        candidates.append({
            "category": "medication_change",
            "direction": "pos",
            "importance": ins_imp,
            "text": get_summary_factor("ins_pos", lang, change_desc=action_word, status=insulin_val),
        })
    elif change_val == "Ch":
        chg_contrib = pos_map.get("cat__change_Ch", 0.0)
        chg_imp = 3.8 + chg_contrib * 2.5
        candidates.append({
            "category": "medication_change",
            "direction": "pos",
            "importance": chg_imp,
            "text": get_summary_factor("chg_pos", lang),
        })
    elif insulin_val == "Steady":
        ins_contrib = neg_map.get("cat__insulin_Steady", 0.0)
        ins_imp = 3.2 + ins_contrib * 2.0
        candidates.append({
            "category": "medication_change",
            "direction": "neg",
            "importance": ins_imp,
            "text": get_summary_factor("ins_neg_steady", lang),
        })
    elif diabetes_med == "No":
        dm_contrib = neg_map.get("cat__diabetesMed_No", 0.0)
        dm_imp = 3.5 + dm_contrib * 2.5
        candidates.append({
            "category": "medication_change",
            "direction": "neg",
            "importance": dm_imp,
            "text": get_summary_factor("dm_neg_no", lang),
        })

    # Category: Length of Stay
    if length_of_stay >= 7:
        stay_contrib = pos_map.get("num__time_in_hospital", 0.0)
        stay_imp = 3.5 + stay_contrib * 2.5 + (length_of_stay - 7) * 0.1
        candidates.append({
            "category": "length_of_stay",
            "direction": "pos",
            "importance": stay_imp,
            "text": get_summary_factor("stay_pos", lang, days=length_of_stay),
        })
    elif 0 < length_of_stay <= 2:
        stay_contrib = neg_map.get("num__time_in_hospital", 0.0)
        stay_imp = 3.2 + stay_contrib * 2.5
        candidates.append({
            "category": "length_of_stay",
            "direction": "neg",
            "importance": stay_imp,
            "text": get_summary_factor("stay_neg", lang, days=length_of_stay),
        })

    # Category: Medication Count / Polypharmacy
    if num_medications >= 18:
        med_contrib = pos_map.get("num__num_medications", 0.0)
        med_imp = 3.6 + med_contrib * 2.5 + (num_medications - 18) * 0.05
        candidates.append({
            "category": "polypharmacy",
            "direction": "pos",
            "importance": med_imp,
            "text": get_summary_factor("med_pos", lang, meds=num_medications),
        })
    elif 0 < num_medications <= 6:
        med_contrib = neg_map.get("num__num_medications", 0.0)
        med_imp = 3.0 + med_contrib * 2.5
        candidates.append({
            "category": "polypharmacy",
            "direction": "neg",
            "importance": med_imp,
            "text": get_summary_factor("med_neg", lang, meds=num_medications),
        })

    # Category: Multi-morbidity Burden (Diagnoses Entered)
    if num_diagnoses >= 9:
        diag_cnt_contrib = pos_map.get("num__number_diagnoses", 0.0)
        diag_cnt_imp = 3.3 + diag_cnt_contrib * 2.5
        candidates.append({
            "category": "morbidity",
            "direction": "pos",
            "importance": diag_cnt_imp,
            "text": get_summary_factor("diag_cnt_pos", lang, diagnoses=num_diagnoses),
        })
    elif 0 < num_diagnoses <= 4:
        diag_cnt_contrib = neg_map.get("num__number_diagnoses", 0.0)
        diag_cnt_imp = 3.0 + diag_cnt_contrib * 2.5
        candidates.append({
            "category": "morbidity",
            "direction": "neg",
            "importance": diag_cnt_imp,
            "text": get_summary_factor("diag_cnt_neg", lang, diagnoses=num_diagnoses),
        })

    # Category: Inpatient Procedures
    if num_procedures >= 3:
        proc_contrib = pos_map.get("num__num_procedures", 0.0)
        proc_imp = 3.2 + proc_contrib * 2.5 + (num_procedures - 3) * 0.1
        candidates.append({
            "category": "procedures",
            "direction": "pos",
            "importance": proc_imp,
            "text": get_summary_factor("proc_pos", lang, procedures=num_procedures),
        })
    elif num_procedures == 0 and "num__num_procedures" in neg_map:
        proc_contrib = neg_map.get("num__num_procedures", 0.0)
        proc_imp = 2.8 + proc_contrib * 2.5
        candidates.append({
            "category": "procedures",
            "direction": "neg",
            "importance": proc_imp,
            "text": get_summary_factor("proc_neg", lang),
        })

    # Category: Age Demographic
    if age_bracket in ["[70-80)", "[80-90)", "[90-100)"]:
        age_contrib = pos_map.get(f"cat__age_{age_bracket}", 0.0)
        age_imp = 3.0 + age_contrib * 3.0
        candidates.append({
            "category": "age",
            "direction": "pos",
            "importance": age_imp,
            "text": get_summary_factor("age_pos", lang, age=age_bracket),
        })
    elif age_bracket in ["[0-10)", "[10-20)", "[20-30)", "[30-40)"]:
        age_contrib = neg_map.get(f"cat__age_{age_bracket}", 0.0)
        age_imp = 3.5 + age_contrib * 3.0
        candidates.append({
            "category": "age",
            "direction": "neg",
            "importance": age_imp,
            "text": get_summary_factor("age_neg", lang, age=age_bracket),
        })

    # Category: Glycemic Labs
    if a1c_display in [">8", ">7"]:
        a1c_contrib = pos_map.get(f"cat__A1Cresult_{a1c_display}", 0.0)
        a1c_imp = 3.5 + a1c_contrib * 2.5
        candidates.append({
            "category": "labs",
            "direction": "pos",
            "importance": a1c_imp,
            "text": get_summary_factor("a1c_pos", lang, a1c=a1c_display),
        })
    elif a1c_display == "Norm":
        a1c_contrib = neg_map.get("cat__A1Cresult_Norm", 0.0)
        a1c_imp = 3.0 + a1c_contrib * 2.5
        candidates.append({
            "category": "labs",
            "direction": "neg",
            "importance": a1c_imp,
            "text": get_summary_factor("a1c_neg_norm", lang),
        })
    elif a1c_display == "None" and selected_tier in ["Higher Score", "Moderate Score"]:
        candidates.append({
            "category": "labs",
            "direction": "pos",
            "importance": 2.7,
            "text": get_summary_factor("a1c_missing", lang),
        })

    if glu_display in [">300", ">200"]:
        glu_contrib = pos_map.get(f"cat__max_glu_serum_{glu_display}", 0.0)
        glu_imp = 3.2 + glu_contrib * 2.5
        candidates.append({
            "category": "glucose_surge",
            "direction": "pos",
            "importance": glu_imp,
            "text": get_summary_factor("glu_pos", lang, glucose=glu_display),
        })

    # Category: Primary Diagnosis
    not_doc = DIAG_CATEGORY_TRANSLATIONS["Not documented in billing records"].get(lang, "Not documented in billing records")
    if diag_desc != not_doc:
        diag_pos = any("cat__diag_1_" in k for k in pos_map)
        diag_neg = any("cat__diag_1_" in k for k in neg_map)
        if diag_pos:
            diag_contrib = max([pos_map[k] for k in pos_map if "cat__diag_1_" in k] or [0.0])
            candidates.append({
                "category": "diagnosis",
                "direction": "pos",
                "importance": 2.8 + diag_contrib * 2.5,
                "text": get_summary_factor("diag_pos", lang, diag=diag_desc),
            })
        elif diag_neg:
            diag_contrib = max([neg_map[k] for k in neg_map if "cat__diag_1_" in k] or [0.0])
            candidates.append({
                "category": "diagnosis",
                "direction": "neg",
                "importance": 2.8 + diag_contrib * 2.5,
                "text": get_summary_factor("diag_neg", lang, diag=diag_desc),
            })
        else:
            candidates.append({
                "category": "diagnosis",
                "direction": "pos" if selected_tier == "Higher Score" else "neg",
                "importance": 2.0,
                "text": get_summary_factor("diag_neutral", lang, diag=diag_desc),
            })
    else:
        candidates.append({
            "category": "diagnosis",
            "direction": "neg",
            "importance": 2.2,
            "text": get_summary_factor("diag_missing", lang),
        })

    # Separate into positive and negative candidate lists
    pos_cands = [c for c in candidates if c["direction"] == "pos"]
    neg_cands = [c for c in candidates if c["direction"] == "neg"]

    pos_cands.sort(key=lambda c: c["importance"], reverse=True)
    neg_cands.sort(key=lambda c: c["importance"], reverse=True)

    # Select balanced 2-3 factors without category duplicates
    selected_factors: List[str] = []
    used_categories = set()

    if selected_tier == "Higher Score":
        # 2 positive factors + 1 negative/mitigating factor (or 3 positive)
        for c in pos_cands:
            if c["category"] not in used_categories:
                selected_factors.append(c["text"])
                used_categories.add(c["category"])
                if len(selected_factors) >= 2:
                    break
        for c in neg_cands:
            if c["category"] not in used_categories:
                selected_factors.append(c["text"])
                used_categories.add(c["category"])
                break
        if len(selected_factors) < 3:
            for c in pos_cands:
                if c["category"] not in used_categories:
                    selected_factors.append(c["text"])
                    used_categories.add(c["category"])
                    if len(selected_factors) >= 3:
                        break

    elif selected_tier == "Moderate Score":
        # 1-2 positive + 1-2 negative
        if pos_cands:
            selected_factors.append(pos_cands[0]["text"])
            used_categories.add(pos_cands[0]["category"])
        if neg_cands:
            selected_factors.append(neg_cands[0]["text"])
            used_categories.add(neg_cands[0]["category"])
        remaining = [c for c in (pos_cands + neg_cands) if c["category"] not in used_categories]
        remaining.sort(key=lambda c: c["importance"], reverse=True)
        if remaining and len(selected_factors) < 3:
            selected_factors.append(remaining[0]["text"])
            used_categories.add(remaining[0]["category"])

    else:  # Lower Score
        # 2 negative factors + 1 positive/context factor (or 3 negative)
        for c in neg_cands:
            if c["category"] not in used_categories:
                selected_factors.append(c["text"])
                used_categories.add(c["category"])
                if len(selected_factors) >= 2:
                    break
        for c in pos_cands:
            if c["category"] not in used_categories:
                selected_factors.append(c["text"])
                used_categories.add(c["category"])
                break
        if len(selected_factors) < 3:
            for c in neg_cands:
                if c["category"] not in used_categories:
                    selected_factors.append(c["text"])
                    used_categories.add(c["category"])
                    if len(selected_factors) >= 3:
                        break

    # Fallback to guarantee at least 2 factors
    if len(selected_factors) < 2:
        if diag_desc != not_doc:
            selected_factors.append(get_summary_factor("diag_neutral", lang, diag=diag_desc))
        else:
            selected_factors.append(get_summary_factor("diag_missing", lang))

    # -------------------------------------------------------------------------
    # 3. Tailored Follow-Up Considerations (Options for clinical team review)
    # -------------------------------------------------------------------------
    considerations: List[str] = []

    # Priority 1: Medication adjustments & polypharmacy
    if insulin_val in ["Up", "Down"]:
        action_word = get_action_word("escalated" if insulin_val == "Up" else "reduced", lang)
        considerations.append(get_summary_followup("fu_insulin", lang, action=action_word))
    elif change_val == "Ch":
        considerations.append(get_summary_followup("fu_chg", lang))
    elif num_medications >= 18:
        considerations.append(get_summary_followup("fu_polypharmacy", lang, meds=num_medications))

    # Priority 2: Utilization history & post-discharge transition
    if num_inpatient >= 2 or num_emergency >= 2:
        considerations.append(get_summary_followup("fu_util_frequent", lang, inpatient=num_inpatient, emergency=num_emergency))
    elif num_inpatient == 1 or num_emergency == 1:
        considerations.append(get_summary_followup("fu_util_single", lang))

    # Priority 3: Glycemic lab follow-up
    if a1c_display == "None":
        considerations.append(get_summary_followup("fu_a1c_missing", lang))
    elif a1c_display in [">8", ">7"]:
        considerations.append(get_summary_followup("fu_a1c_elevated", lang, a1c=a1c_display))
    elif glu_display in [">300", ">200"]:
        considerations.append(get_summary_followup("fu_glucose_surge", lang, glucose=glu_display))

    # Priority 4: Extended stay
    if length_of_stay >= 7 and len(considerations) < 2:
        considerations.append(get_summary_followup("fu_extended_stay", lang, days=length_of_stay))

    # Default fallbacks if no specific considerations triggered
    if not considerations:
        if selected_tier == "Higher Score":
            considerations.append(get_summary_followup("fu_fallback_high", lang))
        elif selected_tier == "Moderate Score":
            considerations.append(get_summary_followup("fu_fallback_mod", lang))
        else:
            considerations.append(get_summary_followup("fu_fallback_low", lang))

    follow_up_text = get_summary_followup_wrapped(considerations, lang)
    disclaimer = get_summary_disclaimer(lang)

    return {
        "overview": overview,
        "key_factors": selected_factors,
        "follow_up": follow_up_text,
        "disclaimer": disclaimer,
    }


# -----------------------------------------------------------------------------
# Main Application Flow
# -----------------------------------------------------------------------------
def main():
    # 1. Load pipeline and metadata
    pipeline, metadata, metrics = load_trained_model_pipeline()

    if pipeline is None:
        lang = st.session_state.get("language", "English")
        st.error(t("err_model_not_found", lang))
        st.stop()

    # 2. Ingest and score eligible cohort
    df_scored = load_and_score_cohort()
    if df_scored is None:
        st.stop()

    # -------------------------------------------------------------------------
    # Sidebar Controls & Configurations
    # -------------------------------------------------------------------------
    with st.sidebar:
        # Language Selector Dropdown (Persisted in st.session_state)
        LANG_DISPLAY_OPTIONS = ["English", "हिन्दी (Hindi)", "ಕನ್ನಡ (Kannada)"]
        LANG_TO_CODE = {
            "English": "English",
            "हिन्दी (Hindi)": "हिन्दी",
            "ಕನ್ನಡ (Kannada)": "ಕನ್ನಡ",
            "हिन्दी": "हिन्दी",
            "ಕನ್ನಡ": "ಕನ್ನಡ",
        }
        CODE_TO_DISPLAY = {
            "English": "English",
            "हिन्दी": "हिन्दी (Hindi)",
            "ಕನ್ನಡ": "ಕನ್ನಡ (Kannada)",
            "हिन्दी (Hindi)": "हिन्दी (Hindi)",
            "ಕನ್ನಡ (Kannada)": "ಕನ್ನಡ (Kannada)",
        }

        current_lang_raw = st.session_state.get("language", "English")
        canonical_lang = LANG_TO_CODE.get(current_lang_raw, "English")
        current_display = CODE_TO_DISPLAY.get(canonical_lang, "English")
        lang_idx = LANG_DISPLAY_OPTIONS.index(current_display) if current_display in LANG_DISPLAY_OPTIONS else 0

        selected_display = st.selectbox(
            "Language / भाषा / ಭಾಷೆ",
            options=LANG_DISPLAY_OPTIONS,
            index=lang_idx,
            key="language_dropdown",
            help=t("lang_help", canonical_lang),
        )
        selected_canonical = LANG_TO_CODE.get(selected_display, "English")
        if selected_canonical != canonical_lang:
            st.session_state["language"] = selected_canonical
            st.query_params["lang"] = selected_canonical
            st.rerun()

        lang = selected_canonical
        if st.query_params.get("lang") != lang:
            st.query_params["lang"] = lang

        # Theme Selector Toggle (Persisted in st.session_state, independent of language)
        current_theme_code = st.session_state.get("theme", "Light Mode")
        is_dark_current = (current_theme_code == "Dark Mode")

        if st.session_state.get("dark_mode_toggle") != is_dark_current:
            st.session_state["dark_mode_toggle"] = is_dark_current

        def on_theme_toggle_change():
            st.session_state["theme"] = "Dark Mode" if st.session_state.get("dark_mode_toggle", False) else "Light Mode"
            st.query_params["theme"] = "dark" if st.session_state.get("dark_mode_toggle", False) else "light"

        st.toggle(
            "Dark Mode",
            key="dark_mode_toggle",
            on_change=on_theme_toggle_change,
            help=t("theme_help", lang),
        )

        is_dark = (st.session_state.get("theme", "Light Mode") == "Dark Mode")
        desired_theme_param = "dark" if is_dark else "light"
        if st.query_params.get("theme") != desired_theme_param:
            st.query_params["theme"] = desired_theme_param

        st.markdown("---")

        st.markdown(f"### {t('sidebar_controls_title', lang)}")

        st.markdown(f"#### {t('capacity_section_title', lang)}")
        raw_cap = st.query_params.get("capacity", "")
        try:
            cap_int = int(raw_cap)
            init_capacity = cap_int if (25 <= cap_int <= 500) else 50
        except (ValueError, TypeError):
            init_capacity = 50

        capacity = st.slider(
            t("capacity_slider_label", lang),
            min_value=25,
            max_value=500,
            value=init_capacity,
            step=25,
            help=t("capacity_slider_help", lang),
        )
        st.caption(t("capacity_caption", lang))
        if st.query_params.get("capacity") != str(capacity):
            st.query_params["capacity"] = str(capacity)

        st.markdown("---")
        st.markdown(f"#### {t('thresholds_section_title', lang)}")
        st.caption(t("thresholds_caption", lang))

        raw_high = st.query_params.get("high_th", "")
        try:
            high_float = round(float(raw_high), 2)
            init_high = high_float if (0.50 <= high_float <= 0.85) else HIGH_RISK_THRESHOLD
        except (ValueError, TypeError):
            init_high = HIGH_RISK_THRESHOLD

        high_threshold = st.slider(
            t("high_threshold_label", lang),
            min_value=0.50,
            max_value=0.85,
            value=init_high,
            step=0.05,
            help=t("high_threshold_help", lang),
        )
        if st.query_params.get("high_th") != f"{high_threshold:.2f}":
            st.query_params["high_th"] = f"{high_threshold:.2f}"

        max_mod_val = min(0.55, high_threshold)
        raw_mod = st.query_params.get("mod_th", "")
        try:
            mod_float = round(float(raw_mod), 2)
            init_mod = mod_float if (0.20 <= mod_float <= max_mod_val) else min(MEDIUM_RISK_THRESHOLD, high_threshold)
        except (ValueError, TypeError):
            init_mod = min(MEDIUM_RISK_THRESHOLD, high_threshold)

        mod_threshold = st.slider(
            t("mod_threshold_label", lang),
            min_value=0.20,
            max_value=max_mod_val,
            value=init_mod,
            step=0.05,
            help=t("mod_threshold_help", lang),
        )
        if st.query_params.get("mod_th") != f"{mod_threshold:.2f}":
            st.query_params["mod_th"] = f"{mod_threshold:.2f}"

        st.markdown("---")
        st.markdown(f"#### {t('filters_section_title', lang)}")
        age_options = sorted(list(df_scored["age_group"].unique()))

        raw_ages = st.query_params.get("ages", "")
        init_ages = []
        if raw_ages:
            parsed_ages = [a.strip() for a in raw_ages.split(",") if a.strip()]
            init_ages = [a for a in parsed_ages if a in age_options]

        selected_ages = st.multiselect(
            t("age_filter_label", lang),
            options=age_options,
            default=init_ages,
            help=t("age_filter_help", lang),
        )
        curr_ages_str = ",".join(selected_ages) if selected_ages else ""
        if curr_ages_str:
            if st.query_params.get("ages") != curr_ages_str:
                st.query_params["ages"] = curr_ages_str
        elif "ages" in st.query_params:
            del st.query_params["ages"]

        st.markdown("---")
        st.markdown(f"#### {t('governance_title', lang)}")
        if metrics:
            st.markdown(
                f"- **{t('governance_model_label', lang)}**: {t('governance_model_val', lang)}\n"
                f"- **{t('gov_roc_auc', lang)}**: `{metrics.get('roc_auc', 'N/A')}`\n"
                f"- **{t('gov_pr_auc', lang)}**: `{metrics.get('pr_auc', 'N/A')}`\n"
                f"- **{t('gov_recall', lang)}**: `{metrics.get('recall', 'N/A')}`\n"
                f"- **{t('gov_precision', lang)}**: `{metrics.get('precision', 'N/A')}`\n"
                f"- **{t('gov_random_state', lang)}**: `42` (Fixed)"
            )
        st.caption(t("governance_caption", lang))

    # Apply age filter if selected; since df_scored is pre-sorted, filtered_df preserves sorted order
    if selected_ages:
        filtered_df = df_scored[df_scored["age_group"].isin(selected_ages)]
    else:
        filtered_df = df_scored

    # Categorize into experimental score tiers (mutually exclusive and exhaustive)
    def assign_score_tier(score: float) -> str:
        if score >= high_threshold:
            return "Higher Score"
        elif score >= mod_threshold:
            return "Moderate Score"
        else:
            return "Lower Score"

    # Fast vectorized counts using NumPy boolean masks
    scores = filtered_df["predicted_score"].to_numpy()
    n_total = len(scores)
    n_high = int((scores >= high_threshold).sum())
    n_mod = int(((scores >= mod_threshold) & (scores < high_threshold)).sum())
    n_low = int((scores < mod_threshold).sum())

    # -------------------------------------------------------------------------
    # Top Header Section (Matching Visual Reference Layout)
    # -------------------------------------------------------------------------
    st.markdown('<div class="keel-header">', unsafe_allow_html=True)
    header_col1, header_col2, header_col3 = st.columns([2.8, 1.1, 1.3])

    with header_col1:
        st.markdown(f'<span class="keel-badge-tag">{t("badge_tag", lang)}</span>', unsafe_allow_html=True)
        st.markdown(f'<h1 class="keel-title">{t("header_title", lang)}</h1>', unsafe_allow_html=True)
        st.markdown(
            f'<p class="keel-subtitle">{t("header_subtitle", lang)}</p>',
            unsafe_allow_html=True,
        )

    with header_col2:
        auc_val = f"{metrics['roc_auc']:.4f}" if metrics else "0.6393"
        st.markdown(
            f"""
            <div class="header-metric-card">
                <div class="header-metric-label">{t("header_auc_label", lang)}</div>
                <div class="header-metric-value">{auc_val}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with header_col3:
        st.markdown(
            f"""
            <div class="header-priority-pill">
                <div class="header-priority-label">{t("header_capacity_label", lang)}</div>
                <div class="header-priority-value">{capacity} {t("patients_suffix", lang)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

    # Prominent Research Prototype Notice
    st.markdown(
        f"""
        <div class="keel-disclaimer-banner">
            {t("disclaimer_banner", lang)}
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
        card1_title = t("kpi_filtered_title", lang) if is_filtered else t("kpi_eligible_title", lang)
        card1_subtitle = (
            f"{t('kpi_of', lang)} {len(df_scored):,} {t('kpi_eligible_short', lang)} ({n_total / len(df_scored) * 100:.1f}%)"
            if is_filtered
            else t("kpi_eligible_sub", lang)
        )
        card1_val_color = "#F8FAFC" if is_dark else "#0F172A"
        st.markdown(
            f"""
            <div class="keel-card" style="padding: 1rem;">
                <div class="keel-card-subtitle" style="margin-bottom: 0.2rem;">{card1_title}</div>
                <div class="kpi-metric-val" style="color: {card1_val_color};">{n_total:,}</div>
                <div class="kpi-metric-sub">{card1_subtitle}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with kpi_col2:
        pct_high = (n_high / n_total * 100) if n_total > 0 else 0
        card2_color = "#F87171" if is_dark else "#DC2626"
        st.markdown(
            f"""
            <div class="keel-card" style="padding: 1rem; border-top: 3px solid {card2_color};">
                <div class="keel-card-subtitle" style="margin-bottom: 0.2rem;">{t("kpi_high_title", lang, threshold=high_threshold)}</div>
                <div class="kpi-metric-val" style="color: {card2_color};">{n_high:,} <span class="kpi-metric-sub" style="font-weight: 600;">({pct_high:.1f}%)</span></div>
                <div class="kpi-metric-sub">{t("kpi_high_sub", lang)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with kpi_col3:
        pct_mod = (n_mod / n_total * 100) if n_total > 0 else 0
        card3_color = "#FBBF24" if is_dark else "#D97706"
        st.markdown(
            f"""
            <div class="keel-card" style="padding: 1rem; border-top: 3px solid {card3_color};">
                <div class="keel-card-subtitle" style="margin-bottom: 0.2rem;">{t("kpi_mod_title", lang, mod=mod_threshold, high=high_threshold)}</div>
                <div class="kpi-metric-val" style="color: {card3_color};">{n_mod:,} <span class="kpi-metric-sub" style="font-weight: 600;">({pct_mod:.1f}%)</span></div>
                <div class="kpi-metric-sub">{t("kpi_mod_sub", lang)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with kpi_col4:
        pct_low = (n_low / n_total * 100) if n_total > 0 else 0
        card4_color = "#34D399" if is_dark else "#059669"
        st.markdown(
            f"""
            <div class="keel-card" style="padding: 1rem; border-top: 3px solid {card4_color};">
                <div class="keel-card-subtitle" style="margin-bottom: 0.2rem;">{t("kpi_low_title", lang, threshold=mod_threshold)}</div>
                <div class="kpi-metric-val" style="color: {card4_color};">{n_low:,} <span class="kpi-metric-sub" style="font-weight: 600;">({pct_low:.1f}%)</span></div>
                <div class="kpi-metric-sub">{t("kpi_low_sub", lang)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # -------------------------------------------------------------------------
    # Main Dashboard Tabs
    # -------------------------------------------------------------------------
    tab_queue, tab_detail, tab_diagnostics, tab_predict = st.tabs([
        t("tab_queue_title", lang),
        t("tab_detail_title", lang),
        t("tab_diagnostics_title", lang),
        t("tab_predict_title", lang),
    ])

    # -------------------------------------------------------------------------
    # TAB 1: High-Priority Outreach Queue (Main View)
    # -------------------------------------------------------------------------
    with tab_queue:
        # Select top encounters up to selected capacity (pre-sorted order is preserved)
        capacity_queue = filtered_df.head(capacity).copy()
        capacity_queue["priority_rank"] = range(1, len(capacity_queue) + 1)
        # Assign score tier only to encounters in the outreach queue (at most capacity rows)
        capacity_queue["score_tier"] = np.where(
            capacity_queue["predicted_score"] >= high_threshold,
            "Higher Score",
            np.where(capacity_queue["predicted_score"] >= mod_threshold, "Moderate Score", "Lower Score"),
        )

        left_col, right_col = st.columns([1.1, 2.1])

        # LEFT COLUMN: Risk Model Variables & Score Distribution
        with left_col:
            st.markdown(
                f"""
                <div class="keel-card">
                    <div class="keel-card-title">{t("card_variables_title", lang)}</div>
                    <div class="keel-card-subtitle">{t("card_variables_subtitle", lang)}</div>
                """,
                unsafe_allow_html=True,
            )

            # Bar chart of variable categories derived dynamically from model coefficients
            driver_categories = compute_domain_importance(pipeline, lang=lang)
            view_domain = render_chart_data_toggle(key="toggle_view_domain", lang=lang)

            if view_domain == "data":
                st.dataframe(driver_categories, use_container_width=True, hide_index=True, height=200)
            else:
                domain_color = "#2DD4BF" if is_dark else "#0D9488"
                domain_chart = (
                    alt.Chart(driver_categories)
                    .mark_bar(cornerRadiusTopRight=4, cornerRadiusBottomRight=4, color=domain_color)
                    .encode(
                        x=alt.X("Relative Influence:Q", title=t("chart_variables_xaxis", lang), scale=alt.Scale(domain=[0, 100])),
                        y=alt.Y("Clinical Domain:N", sort="-x", title=None),
                        tooltip=[
                            alt.Tooltip("Clinical Domain:N", title=t("col_clinical_domain", lang)),
                            alt.Tooltip("Relative Influence:Q", title=t("col_relative_influence", lang), format=".0f"),
                        ],
                    )
                    .properties(height=200)
                )
                domain_chart = apply_chart_theme(domain_chart, is_dark=is_dark)
                st.altair_chart(domain_chart, use_container_width=True, theme=None)

            st.caption(t("chart_variables_caption", lang))

            # Score Distribution Histogram (Optimized with NumPy aggregated bins)
            st.markdown("---")
            h_col1, h_col2 = st.columns([1.8, 1.2])
            with h_col1:
                st.markdown(f"##### {t('hist_title', lang)}")
            with h_col2:
                view_hist = render_chart_data_toggle(key="toggle_view_hist", lang=lang)

            hist_df = compute_score_histogram_bins(scores, bins=25)
            if view_hist == "data":
                hist_table = pd.DataFrame({
                    t("hist_col_range", lang): [f"{r['bin_start']:.2f} – {r['bin_end']:.2f}" for _, r in hist_df.iterrows()],
                    t("hist_col_count", lang): [f"{int(r['count']):,}" for _, r in hist_df.iterrows()],
                    t("hist_col_pct", lang): [f"{r['pct']:.1f}%" for _, r in hist_df.iterrows()],
                })
                st.dataframe(hist_table, use_container_width=True, hide_index=True, height=160)
            else:
                hist_color = "#38BDF8" if is_dark else "#0284C7"
                hist_chart = (
                    alt.Chart(hist_df)
                    .mark_bar(color=hist_color, opacity=0.85)
                    .encode(
                        x=alt.X("bin_start:Q", bin="binned", title=t("hist_xaxis", lang)),
                        x2="bin_end:Q",
                        y=alt.Y("count:Q", title=t("hist_yaxis", lang)),
                        tooltip=[
                            alt.Tooltip("bin_start:Q", title=t("hist_tt_start", lang), format=".2f"),
                            alt.Tooltip("bin_end:Q", title=t("hist_tt_end", lang), format=".2f"),
                            alt.Tooltip("count:Q", title=t("hist_tt_count", lang), format=","),
                        ],
                    )
                    .properties(height=160)
                )
                hist_chart = apply_chart_theme(hist_chart, is_dark=is_dark)
                st.altair_chart(hist_chart, use_container_width=True, theme=None)

            mean_score = float(np.mean(scores)) if len(scores) > 0 else 0.0
            median_score = float(np.median(scores)) if len(scores) > 0 else 0.0
            st.caption(
                f"{t('cohort_mean_score', lang)}: **{mean_score:.3f}** | {t('cohort_median_score', lang)}: **{median_score:.3f}**"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        # RIGHT COLUMN: High-Priority Outreach Queue Table
        with right_col:
            st.markdown(
                f"""
                <div class="keel-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <div>
                            <div class="keel-card-title">{t("card_queue_title", lang)}</div>
                            <div class="keel-card-subtitle">{t("card_queue_subtitle", lang, count=len(capacity_queue))}</div>
                        </div>
                        <span class="table-capacity-badge">
                            {t("capacity_slots_label", lang, capacity=capacity)}
                        </span>
                    </div>
                """,
                unsafe_allow_html=True,
            )

            # Display table with localized columns
            col_rank_name = t("col_rank", lang)
            col_enc_name = t("col_encounter_id", lang)
            col_score_name = t("col_score_pct", lang)
            col_tier_name = t("col_model_tier", lang)
            col_driver_name = t("col_primary_driver", lang)
            col_age_name = t("col_age_group", lang)
            col_stay_name = t("col_stay_days", lang)
            col_prior_name = t("col_prior_admissions", lang)

            table_display = capacity_queue[[
                "priority_rank",
                "encounter_label",
                "score_percent",
                "score_tier",
                "top_driver",
                "age_group",
                "length_of_stay",
                "num_inpatient",
            ]].copy()

            # Translate tier and driver labels for display only
            table_display["score_tier"] = table_display["score_tier"].apply(lambda tv: translate_tier(tv, lang=lang))
            table_display["top_driver"] = table_display["top_driver"].apply(lambda dv: translate_driver_label(dv, lang=lang))

            table_display = table_display.rename(columns={
                "priority_rank": col_rank_name,
                "encounter_label": col_enc_name,
                "score_percent": col_score_name,
                "score_tier": col_tier_name,
                "top_driver": col_driver_name,
                "age_group": col_age_name,
                "length_of_stay": col_stay_name,
                "num_inpatient": col_prior_name,
            })

            st.dataframe(
                table_display,
                use_container_width=True,
                hide_index=True,
                height=480,
                column_config={
                    col_rank_name: st.column_config.NumberColumn(col_rank_name, width="small"),
                    col_enc_name: st.column_config.TextColumn(col_enc_name, width="small"),
                    col_score_name: st.column_config.ProgressColumn(
                        col_score_name,
                        min_value=0,
                        max_value=100,
                        format="%.1f%%",
                        width="medium",
                    ),
                    col_tier_name: st.column_config.TextColumn(col_tier_name, width="small"),
                    col_driver_name: st.column_config.TextColumn(col_driver_name, width="medium"),
                    col_age_name: st.column_config.TextColumn(col_age_name, width="small"),
                    col_stay_name: st.column_config.NumberColumn(col_stay_name, width="small"),
                    col_prior_name: st.column_config.NumberColumn(col_prior_name, width="small"),
                },
            )

            st.caption(t("queue_caption", lang))
            st.markdown("</div>", unsafe_allow_html=True)

            # Retrospective Top-10 vs. Top-20 Capacity Simulation Card
            retro_stats = compute_retrospective_top_k_metrics(df_scored, k_values=(10, 20))
            if retro_stats:
                st.markdown(
                    f"""
                    <div class="keel-card" style="margin-top: 1rem;">
                        <div class="keel-card-title">{t("retro_title", lang)}</div>
                        <div class="keel-card-subtitle">{t("retro_subtitle", lang)}</div>
                    """,
                    unsafe_allow_html=True,
                )
                k1 = retro_stats["actual_k1"]
                k2 = retro_stats["actual_k2"]
                h1 = retro_stats["hits_k1"]
                h2 = retro_stats["hits_k2"]
                p1 = retro_stats["prec_k1"] * 100
                p2 = retro_stats["prec_k2"] * 100
                add_h = retro_stats["additional_hits"]

                retro_table_df = pd.DataFrame([
                    {
                        t("retro_col_cohort", lang): t("retro_top_10_label", lang),
                        t("retro_col_k", lang): k1,
                        t("retro_col_hits", lang): h1,
                        t("retro_col_precision", lang): f"{p1:.1f}% ({h1}/{k1})" if k1 > 0 else "N/A",
                    },
                    {
                        t("retro_col_cohort", lang): t("retro_top_20_label", lang),
                        t("retro_col_k", lang): k2,
                        t("retro_col_hits", lang): h2,
                        t("retro_col_precision", lang): f"{p2:.1f}% ({h2}/{k2})" if k2 > 0 else "N/A",
                    },
                ])
                st.table(retro_table_df)

                st.markdown(
                    f"""
                    <div style="font-size: 0.85rem; line-height: 1.45; margin-bottom: 0.5rem; color: {'#E2E8F0' if is_dark else '#334155'};">
                        {t("retro_expansion_summary", lang, additional=add_h, hits_10=h1, hits_20=h2, p10=p1, p20=p2, k1=k1, k2=k2)}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.caption(t("retro_disclaimer", lang))
                st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # TAB 2: Encounter Clinical Profile & Attribution Deep-Dive
    # -------------------------------------------------------------------------
    with tab_detail:
        st.markdown(
            f"""
            <div class="keel-card">
                <div class="keel-card-title">{t("card_profile_title", lang)}</div>
                <div class="keel-card-subtitle">{t("card_profile_subtitle", lang)}</div>
            """,
            unsafe_allow_html=True,
        )

        # Encounter selector (pseudonymous #HF-XXXX IDs remain untranslated)
        available_labels = capacity_queue["encounter_label"].tolist()
        selected_label = st.selectbox(
            t("select_encounter_label", lang),
            options=available_labels,
            index=0,
            help=t("select_encounter_help", lang),
        )

        match = capacity_queue[capacity_queue["encounter_label"] == selected_label]
        if not match.empty:
            selected_row = match.iloc[0]
        else:
            selected_row = df_scored[df_scored["encounter_label"] == selected_label].iloc[0]

        selected_score = float(selected_row["predicted_score"])
        selected_tier = assign_score_tier(selected_score)

        # Profile Overview Badges
        pcol1, pcol2, pcol3, pcol4 = st.columns(4)
        with pcol1:
            st.metric(t("col_encounter_id", lang), selected_label)
        with pcol2:
            st.metric(t("metric_pred_score", lang), f"{selected_score*100:.1f}%")
        with pcol3:
            if is_dark:
                badge_color = "#F87171" if selected_tier == "Higher Score" else ("#FBBF24" if selected_tier == "Moderate Score" else "#34D399")
            else:
                badge_color = "#DC2626" if selected_tier == "Higher Score" else ("#D97706" if selected_tier == "Moderate Score" else "#059669")
            translated_tier_label = translate_tier(selected_tier, lang)
            st.markdown(
                f"**{t('metric_classification', lang)}**<br><span style='color: {badge_color}; font-size: 1.15rem; font-weight: 700;'>{translated_tier_label}</span>",
                unsafe_allow_html=True,
            )
        with pcol4:
            st.metric(t("metric_primary_driver", lang), translate_driver_label(selected_row["top_driver"], lang))

        # Cautious Risk-Tier Boundary Review Indicator (Threshold-proximity heuristic only)
        MARGIN = 0.03  # Documented ±3% score margin around cutoffs (0.40 and 0.70)
        is_near_high = abs(selected_score - HIGH_RISK_THRESHOLD) <= MARGIN
        is_near_mod = abs(selected_score - MEDIUM_RISK_THRESHOLD) <= MARGIN
        if is_near_high or is_near_mod:
            near_cutoff = HIGH_RISK_THRESHOLD if is_near_high else MEDIUM_RISK_THRESHOLD
            st.markdown(
                f"""
                <div style="margin-top: 0.6rem; margin-bottom: 0.6rem; padding: 0.5rem 0.85rem;
                            background-color: {'rgba(245, 158, 11, 0.15)' if is_dark else '#FFFBEB'};
                            border-left: 4px solid #F59E0B; border-radius: 4px; font-size: 0.82rem;
                            color: {'#FCD34D' if is_dark else '#92400E'};">
                    <strong>{t('boundary_indicator_near', lang, score=selected_score*100, margin=MARGIN*100, cutoff=near_cutoff)}</strong><br>
                    <span style="font-size: 0.75rem; color: {'#CBD5E1' if is_dark else '#78350F'};">
                        {t('boundary_indicator_help', lang)}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("---")

        # Retrieve original features for this encounter directly from df_scored
        num_cols, cat_cols, _ = get_feature_manifest(include_discharge_disposition=False)
        feature_cols = num_cols + cat_cols
        single_encounter_df = df_scored.loc[[selected_row.name], feature_cols]

        pos_factors, neg_factors, intercept_val = compute_local_explanation(
            pipeline=pipeline,
            encounter_row_features=single_encounter_df,
            top_n=6,
            lang=lang,
        )

        # Generate deterministic, rule-based clinical decision-support summary in selected language
        patient_summary = generate_patient_summary(
            selected_row=selected_row,
            selected_score=selected_score,
            selected_tier=selected_tier,
            pos_factors=pos_factors,
            neg_factors=neg_factors,
            lang=lang,
        )

        # ---------------------------------------------------------------------
        # Patient Summary Card (Deterministic Clinical Decision Support)
        # ---------------------------------------------------------------------
        factors_html = "".join(f"<li>{factor}</li>" for factor in patient_summary["key_factors"])
        summary_card_html = f"""
        <div class="patient-summary-box">
            <div class="patient-summary-header">
                <span>📋</span>
                <span>{t("summary_box_header", lang)}</span>
            </div>
            <div class="patient-summary-overview">
                {patient_summary["overview"]}
            </div>
            <div class="patient-summary-factors-title">{t("summary_box_factors_title", lang)}</div>
            <ul class="patient-summary-factors-list">
                {factors_html}
            </ul>
            <div class="patient-summary-followup">
                <strong>{t("summary_box_followup_label", lang)}</strong> {patient_summary["follow_up"]}
            </div>
            <div class="patient-summary-disclaimer">
                {patient_summary["disclaimer"]}
            </div>
        </div>
        """
        st.markdown(summary_card_html, unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # Patient Data-Quality & Record Completeness Notice
        # ---------------------------------------------------------------------
        dq_flags = check_patient_data_quality(selected_row, lang=lang)
        if dq_flags:
            warnings_html = "".join(f"<li><strong>{w['type']}:</strong> {w['text']}</li>" for w in dq_flags)
            st.markdown(
                f"""
                <div style="background-color: {'rgba(245, 158, 11, 0.12)' if is_dark else '#FFFBEB'};
                            border-left: 4px solid #F59E0B; padding: 0.75rem 1rem; border-radius: 6px; margin: 1rem 0;">
                    <div style="font-weight: 700; font-size: 0.9rem; color: {'#FBBF24' if is_dark else '#B45309'}; margin-bottom: 0.35rem;">
                        ⚠️ {t('dq_title', lang)} ({len(dq_flags)})
                    </div>
                    <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.85rem; color: {'#E2E8F0' if is_dark else '#1E293B'};">
                        {warnings_html}
                    </ul>
                    <div style="font-size: 0.75rem; color: {'#94A3B8' if is_dark else '#64748B'}; margin-top: 0.4rem;">
                        {t('dq_disclaimer', lang)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div style="background-color: {'rgba(16, 185, 129, 0.10)' if is_dark else '#ECFDF5'};
                            border-left: 4px solid #10B981; padding: 0.65rem 1rem; border-radius: 6px; margin: 1rem 0;
                            font-size: 0.85rem; color: {'#A7F3D0' if is_dark else '#065F46'};">
                    {t('dq_clean', lang)}
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("---")

        # Clinical Data Profile (3 Columns)
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"##### {t('prof_demographics_title', lang)}")
            st.write(f"- **{t('prof_age_bracket', lang)}**: `{selected_row['age_group']}`")
            st.write(f"- **{t('prof_gender', lang)}**: `{selected_row['gender']}`")
            st.write(f"- **{t('prof_race', lang)}**: `{selected_row['race_display']}`")
            st.write(f"- **{t('prof_adm_type', lang)}**: `{selected_row['admission_type_id']}`")
            st.write(f"- **{t('prof_adm_source', lang)}**: `{selected_row['admission_source_id']}`")

        with c2:
            st.markdown(f"##### {t('prof_utilization_title', lang)}")
            st.write(f"- **{t('prof_stay_days', lang)}**: `{selected_row['length_of_stay']} {t('days_suffix', lang)}`")
            st.write(f"- **{t('prof_prior_adm', lang)}**: `{selected_row['num_inpatient']}`")
            st.write(f"- **{t('prof_prior_er', lang)}**: `{selected_row['num_emergency']}`")
            st.write(f"- **{t('prof_prior_op', lang)}**: `{selected_row['num_outpatient']}`")
            st.write(f"- **{t('prof_lab_tests', lang)}**: `{selected_row['num_lab_procedures']}`")
            st.write(f"- **{t('prof_med_count', lang)}**: `{selected_row['num_medications']}`")

        with c3:
            st.markdown(f"##### {t('prof_glycemic_title', lang)}")
            st.write(f"- **{t('prof_a1c', lang)}**: `{selected_row['a1c_result_display']}`")
            st.write(f"- **{t('prof_glucose', lang)}**: `{selected_row['max_glu_serum_display']}`")
            st.write(f"- **{t('prof_insulin', lang)}**: `{selected_row['insulin']}`")
            st.write(f"- **{t('prof_med_chg', lang)}**: `{selected_row['change']}`")
            st.write(f"- **{t('prof_dm_med', lang)}**: `{selected_row['diabetes_med']}`")
            st.write(f"- **{t('prof_primary_diag', lang)}**: `{selected_row['primary_diag']}`")

        st.markdown("---")

        # Mathematical Feature Attribution (Local Explanation)
        attr_hcol1, attr_hcol2 = st.columns([2.5, 1])
        with attr_hcol1:
            st.markdown(f"#### {t('attribution_section_title', lang)}")
        with attr_hcol2:
            view_attribution = render_chart_data_toggle(key="toggle_view_attribution", lang=lang)

        st.caption(t("attribution_caption", lang))

        exp_col1, exp_col2 = st.columns(2)

        with exp_col1:
            pos_hcol1, pos_hcol2 = st.columns([1.8, 1.2])
            with pos_hcol1:
                st.markdown(t("pos_drivers_title", lang))
            with pos_hcol2:
                view_pos = render_chart_data_toggle(key="toggle_view_pos", lang=lang)

            show_pos_data = (view_attribution == "data") or (view_pos == "data")
            if pos_factors:
                if show_pos_data:
                    pos_table = pd.DataFrame([
                        {
                            t("col_factor", lang): f["clinical_name"],
                            t("col_impact", lang): f"+{f['contribution']:.3f}",
                            t("col_feature_id", lang): f["raw_feature"],
                        }
                        for f in pos_factors
                    ])
                    st.dataframe(pos_table, use_container_width=True, hide_index=True, height=200)
                else:
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
                        .properties(height=200)
                    )
                    pos_chart = apply_chart_theme(pos_chart, is_dark=is_dark)
                    st.altair_chart(pos_chart, use_container_width=True, theme=None)
            else:
                st.info(t("pos_empty_state", lang))

        with exp_col2:
            neg_hcol1, neg_hcol2 = st.columns([1.8, 1.2])
            with neg_hcol1:
                st.markdown(t("neg_drivers_title", lang))
            with neg_hcol2:
                view_neg = render_chart_data_toggle(key="toggle_view_neg", lang=lang)

            show_neg_data = (view_attribution == "data") or (view_neg == "data")
            if neg_factors:
                if show_neg_data:
                    neg_table = pd.DataFrame([
                        {
                            t("col_factor", lang): f["clinical_name"],
                            t("col_impact", lang): f"{f['contribution']:.3f}",
                            t("col_feature_id", lang): f["raw_feature"],
                        }
                        for f in neg_factors
                    ])
                    st.dataframe(neg_table, use_container_width=True, hide_index=True, height=200)
                else:
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
                        .properties(height=200)
                    )
                    neg_chart = apply_chart_theme(neg_chart, is_dark=is_dark)
                    st.altair_chart(neg_chart, use_container_width=True, theme=None)
            else:
                st.info(t("neg_empty_state", lang))

        st.caption(f"{t('intercept_caption', lang, val=intercept_val)}")
        st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # TAB 3: Cohort Diagnostics & Model Metrics
    # -------------------------------------------------------------------------
    with tab_diagnostics:
        st.markdown(
            f"""
            <div class="keel-card">
                <div class="keel-card-title">{t("card_diagnostics_title", lang)}</div>
                <div class="keel-card-subtitle">{t("card_diagnostics_subtitle", lang)}</div>
            """,
            unsafe_allow_html=True,
        )

        dcol1, dcol2 = st.columns(2)

        with dcol1:
            st.markdown(t("diagnostics_metrics_title", lang))
            if metrics:
                metrics_table = pd.DataFrame([
                    {"Metric": t("metric_name_roc_auc", lang), "Value": f"{metrics.get('roc_auc', 0):.4f}"},
                    {"Metric": t("metric_name_pr_auc", lang), "Value": f"{metrics.get('pr_auc', 0):.4f} ({t('metric_desc_pr_auc', lang)})"},
                    {"Metric": t("metric_name_recall", lang), "Value": f"{metrics.get('recall', 0)*100:.1f}% {t('metric_desc_recall', lang)}"},
                    {"Metric": t("metric_name_precision", lang), "Value": f"{metrics.get('precision', 0)*100:.1f}%"},
                    {"Metric": t("metric_name_f1", lang), "Value": f"{metrics.get('f1_score', 0):.4f}"},
                    {"Metric": t("metric_name_specificity", lang), "Value": f"{metrics.get('specificity', 0)*100:.1f}%"},
                    {"Metric": t("metric_name_accuracy", lang), "Value": f"{metrics.get('accuracy', 0)*100:.1f}% ({t('metric_desc_accuracy', lang)})"},
                ]).rename(columns={"Metric": t("col_metric", lang), "Value": t("col_value", lang)})
                st.table(metrics_table)

                cm = metrics.get("confusion_matrix", {})
                if cm:
                    st.markdown(t("diagnostics_cm_title", lang))
                    cm_df = pd.DataFrame({
                        t("cm_pred_no", lang): [cm.get("true_negatives", 0), cm.get("false_negatives", 0)],
                        t("cm_pred_yes", lang): [cm.get("false_positives", 0), cm.get("true_positives", 0)],
                    }, index=[t("cm_act_no", lang), t("cm_act_yes", lang)])
                    st.table(cm_df)

        with dcol2:
            st.markdown(t("diagnostics_safeguards_title", lang))
            st.markdown(t("diagnostics_safeguards_text", lang))

            st.markdown(t("diagnostics_limitations_title", lang))
            st.markdown(t("diagnostics_limitations_text", lang))

        st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # TAB 4: New Patient Encounter Prediction
    # -------------------------------------------------------------------------
    with tab_predict:
        from src.app.new_patient_prediction import render_new_patient_tab
        render_new_patient_tab(
            pipeline=pipeline,
            high_threshold=high_threshold,
            mod_threshold=mod_threshold,
            is_dark=is_dark,
            lang=lang,
        )


if __name__ == "__main__":
    main()
