"""
Keel Health - Multilingual Translations Module
Supports: English (default), हिन्दी (Hindi), ಕನ್ನಡ (Kannada)

Provides centralized translations for user interface text, clinical domain labels,
model feature descriptions, diagnosis categories, and individualized patient summaries.
"""

from typing import Any, Dict, List, Optional

# Supported language codes / display names
LANGUAGES = ["English", "हिन्दी", "ಕನ್ನಡ"]

# UI Strings Dictionary
UI_STRINGS: Dict[str, Dict[str, str]] = {
    # Page Config & Header
    "page_title": {
        "English": "Keel Health | Inpatient Risk Prioritization",
        "हिन्दी": "कील हेल्थ | अस्पताल पुनः भर्ती जोखिम प्राथमिकता",
        "ಕನ್ನಡ": "ಕೀಲ್ ಹೆಲ್ತ್ | ಒಳರೋಗಿ ಮರುದಾಖಲಾತಿ ಅಪಾಯದ ಆದ್ಯತೆ",
    },
    "badge_tag": {
        "English": "● PREDICTIVE RISK ENGINE",
        "हिन्दी": "● पूर्वानुमानित जोखिम इंजन",
        "ಕನ್ನಡ": "● ಮುನ್ಸೂಚಕ ಅಪಾಯದ ಎಂಜಿನ್",
    },
    "header_title": {
        "English": "Inpatient Risk Prioritization",
        "हिन्दी": "अस्पताल पुनः भर्ती जोखिम प्राथमिकता",
        "ಕನ್ನಡ": "ಒಳರೋಗಿ ಮರುದಾಖಲಾತಿ ಅಪಾಯದ ಆದ್ಯತೆ",
    },
    "header_subtitle": {
        "English": "Keel Health · Early Readmission Risk and Follow-up Prioritization (HackFest 2026)",
        "हिन्दी": "कील हेल्थ · प्रारंभिक पुनः भर्ती जोखिम और अनुवर्ती प्राथमिकता (हैकफ़ेस्ट 2026)",
        "ಕನ್ನಡ": "ಕೀಲ್ ಹೆಲ್ತ್ · ಆರಂಭಿಕ ಮರುದಾಖಲಾತಿ ಅಪಾಯ ಮತ್ತು ಮುಂದಿನ ಆರೈಕೆ ಆದ್ಯತೆ (ಹ್ಯಾಕ್‌ಫೆಸ್ಟ್ 2026)",
    },
    "header_auc_label": {
        "English": "Model ROC-AUC",
        "हिन्दी": "मॉडल ROC-AUC",
        "ಕನ್ನಡ": "ಮಾದರಿ ROC-AUC",
    },
    "header_capacity_label": {
        "English": "Outreach Queue Capacity",
        "हिन्दी": "आउटरीच कतार क्षमता",
        "ಕನ್ನಡ": "ಔಟ್‌ರೀಚ್ ಸರದಿಯ ಸಾಮರ್ಥ್ಯ",
    },
    "patients_suffix": {
        "English": "Patients",
        "हिन्दी": "मरीज़",
        "ಕನ್ನಡ": "ರೋಗಿಗಳು",
    },
    "disclaimer_banner": {
        "English": (
            "<strong>⚠️ RESEARCH PROTOTYPE NOTICE:</strong> Keel Health is an algorithmic research and workflow feasibility "
            "prototype developed using historical clinical encounter records. It is <strong>NOT a clinically validated medical "
            "device or diagnostic system</strong>. Predicted scores represent experimental statistical association estimates, "
            "not clinical prognosis or certainty. Do not use for clinical diagnostic or acute treatment decisions."
        ),
        "हिन्दी": (
            "<strong>⚠️ शोध प्रोटोटाइप सूचना:</strong> कील हेल्थ ऐतिहासिक क्लिनिकल एनकाउंटर रिकॉर्ड का उपयोग करके विकसित एक "
            "एल्गोरिथम अनुसंधान और वर्कफ़्लो प्रोटोटाइप है। यह <strong>चिकित्सीय रूप से मान्य मेडिकल उपकरण या नैदानिक प्रणाली नहीं है</strong>। "
            "अनुमानित स्कोर प्रयोगात्मक सांख्यिकीय संबंध अनुमान हैं, क्लिनिकल निदान या निश्चितता नहीं। इसका उपयोग नैदानिक या तीव्र उपचार निर्णयों के लिए न करें।"
        ),
        "ಕನ್ನಡ": (
            "<strong>⚠️ ಸಂಶೋಧನಾ ಮಾದರಿ ಸೂಚನೆ:</strong> ಕೀಲ್ ಹೆಲ್ತ್ ಐತಿಹಾಸಿಕ ಕ್ಲಿನಿಕಲ್ ದಾಖಲೆಗಳನ್ನು ಬಳಸಿ ಅಭಿವೃದ್ಧಿಪಡಿಸಲಾದ "
            "ಅಲ್ಗಾರಿದಮಿಕ್ ಸಂಶೋಧನಾ ಮತ್ತು ಕಾರ್ಯಸಾಧ್ಯತಾ ಮಾದರಿಯಾಗಿದೆ. ಇದು <strong>ವೈದ್ಯಕೀಯವಾಗಿ ಪ್ರಮಾಣೀಕರಿಸಿದ ಸಾಧನ ಅಥವಾ ರೋಗನಿರ್ಣಯ ವ್ಯವಸ್ಥೆಯಲ್ಲ</strong>. "
            "ಅಂದಾಜು ಸ್ಕೋರ್‌ಗಳು ಪ್ರಾಯೋಗಿಕ ಸಂಖ್ಯಾಶಾಸ್ತ್ರೀಯ ಸಂಬಂಧಗಳಾಗಿದ್ದು, ಕ್ಲಿನಿಕಲ್ ರೋಗನಿರ್ಣಯ ಅಥವಾ ಖಚಿತತೆಯಲ್ಲ. ಚಿಕಿತ್ಸಾ ನಿರ್ಧಾರಗಳಿಗಾಗಿ ಇದನ್ನು ಬಳಸಬೇಡಿ."
        ),
    },

    # Sidebar: Theme & Language Controls
    "sidebar_theme_title": {
        "English": "🎨 Display Theme",
        "हिन्दी": "🎨 डिस्प्ले थीम",
        "ಕನ್ನಡ": "🎨 ಪ್ರದರ್ಶನ ಥೀಮ್",
    },
    "theme_radio_label": {
        "English": "Select Dashboard Theme",
        "हिन्दी": "डैशबोर्ड थीम चुनें",
        "ಕನ್ನಡ": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ ಥೀಮ್ ಆಯ್ಕೆಮಾಡಿ",
    },
    "theme_light": {
        "English": "Light Mode",
        "हिन्दी": "लाइट मोड",
        "ಕನ್ನಡ": "ಲೈಟ್ ಮೋಡ್",
    },
    "theme_dark": {
        "English": "Dark Mode",
        "हिन्दी": "डार्क मोड",
        "ಕನ್ನಡ": "ಡಾರ್ಕ್ ಮೋಡ್",
    },
    "theme_help": {
        "English": "Toggle between Light Mode and Dark Mode across the entire dashboard.",
        "हिन्दी": "पूरे डैशबोर्ड में लाइट मोड और डार्क मोड के बीच स्विच करें।",
        "ಕನ್ನಡ": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್‌ನಲ್ಲಿ ಲೈಟ್ ಮೋಡ್ ಮತ್ತು ಡಾರ್ಕ್ ಮೋಡ್ ನಡುವೆ ಬದಲಿಸಿ.",
    },
    "sidebar_lang_title": {
        "English": "🌐 Language / भाषा / ಭಾಷೆ",
        "हिन्दी": "🌐 भाषा / Language / ಭಾಷೆ",
        "ಕನ್ನಡ": "🌐 ಭಾಷೆ / Language / भाषा",
    },
    "lang_help": {
        "English": "Select display language across the entire dashboard.",
        "हिन्दी": "पूरे डैशबोर्ड में प्रदर्शन भाषा चुनें।",
        "ಕನ್ನಡ": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್‌ನಲ್ಲಿ ಪ್ರದರ್ಶನ ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
    },
    "sidebar_controls_title": {
        "English": "⚙️ Outreach & Model Controls",
        "हिन्दी": "⚙️ आउटरीच और मॉडल नियंत्रण",
        "ಕನ್ನಡ": "⚙️ ಔಟ್‌ರೀಚ್ ಮತ್ತು ಮಾದರಿ ನಿಯಂತ್ರಣಗಳು",
    },
    "capacity_section_title": {
        "English": "1. Follow-up Capacity Prioritization",
        "हिन्दी": "1. अनुवर्ती क्षमता प्राथमिकता",
        "ಕನ್ನಡ": "1. ಮುಂದಿನ ಆರೈಕೆ ಸಾಮರ್ಥ್ಯದ ಆದ್ಯತೆ",
    },
    "capacity_slider_label": {
        "English": "Daily Coordinator Outreach Capacity (Encounters)",
        "हिन्दी": "दैनिक समन्वयक आउटरीच क्षमता (एनकाउंटर)",
        "ಕನ್ನಡ": "ದೈನಂದಿನ ಸಂಯೋಜಕರ ಔಟ್‌ರೀಚ್ ಸಾಮರ್ಥ್ಯ (ದಾಖಲಾತಿಗಳು)",
    },
    "capacity_slider_help": {
        "English": "Simulates hospital capacity constraints (e.g. nurse care-coordinator telephone calls or transitional clinic slots).",
        "हिन्दी": "अस्पताल क्षमता बाधाओं का अनुकरण करता है (उदा. नर्स देखभाल-समन्वयक फोन कॉल या क्लीनिक स्लॉट)।",
        "ಕನ್ನಡ": "ಆಸ್ಪತ್ರೆಯ ಸಾಮರ್ಥ್ಯದ ಮಿತಿಗಳನ್ನು ಅನುಕರಿಸುತ್ತದೆ (ಉದಾ. ನರ್ಸ್ ಕೇರ್-ಕೋಆರ್ಡಿನೇಟರ್ ಫೋನ್ ಕರೆಗಳು ಅಥವಾ ಕ್ಲಿನಿಕ್ ಸ್ಲಾಟ್‌ಗಳು).",
    },
    "capacity_caption": {
        "English": "ℹ️ *Demonstration of capacity-aware triage under finite clinical resources. Not a clinical treatment recommendation.*",
        "हिन्दी": "ℹ️ *सीमित नैदानिक संसाधनों के तहत क्षमता-जागरूक प्राथमिकता का प्रदर्शन। चिकित्सीय उपचार सिफारिश नहीं।*",
        "ಕನ್ನಡ": "ℹ️ *ಸೀಮಿತ ಕ್ಲಿನಿಕಲ್ ಸಂಪನ್ಮೂಲಗಳಲ್ಲಿ ಸಾಮರ್ಥ್ಯ-ಆಧಾರಿತ ಆದ್ಯತೆಯ ಪ್ರದರ್ಶನ. ವೈದ್ಯಕೀಯ ಚಿಕಿತ್ಸಾ ಶಿಫಾರಸಲ್ಲ.*",
    },
    "thresholds_section_title": {
        "English": "2. Model Score Thresholds",
        "हिन्दी": "2. मॉडल स्कोर थ्रेशोल्ड",
        "ಕನ್ನಡ": "2. ಮಾದರಿ ಸ್ಕೋರ್ ಮಿತಿಗಳು",
    },
    "thresholds_caption": {
        "English": "Configure experimental model-score cutoff tiers. These are statistical prediction thresholds, **not clinically validated risk bounds**.",
        "हिन्दी": "प्रायोगिक मॉडल-स्कोर कटऑफ स्तर कॉन्फ़िगर करें। ये सांख्यिकीय थ्रेशोल्ड हैं, **चिकित्सीय रूप से मान्य जोखिम सीमाएं नहीं**।",
        "ಕನ್ನಡ": "ಪ್ರಾಯೋಗಿಕ ಮಾದರಿ-ಸ್ಕೋರ್ ಕಟ್‌ಆಫ್ ಹಂತಗಳನ್ನು ಹೊಂದಿಸಿ. ಇವು ಸಂಖ್ಯಾಶಾಸ್ತ್ರೀಯ ಮಿತಿಗಳಾಗಿದ್ದು, **ವೈದ್ಯಕೀಯವಾಗಿ ಪ್ರಮಾಣೀಕರಿಸಿದ ಅಪಾಯದ ಮಿತಿಗಳಲ್ಲ**.",
    },
    "high_threshold_label": {
        "English": "Higher Model-Score Threshold",
        "हिन्दी": "उच्च मॉडल-स्कोर थ्रेशोल्ड",
        "ಕನ್ನಡ": "ಹೆಚ್ಚಿನ ಮಾದರಿ-ಸ್ಕೋರ್ ಮಿತಿ",
    },
    "high_threshold_help": {
        "English": "Encounters with predicted readmission score at or above this threshold.",
        "हिन्दी": "इस थ्रेशोल्ड पर या उससे अधिक अनुमानित पुनः भर्ती स्कोर वाले एनकाउंटर।",
        "ಕನ್ನಡ": "ಈ ಮಿತಿಯಲ್ಲಿ ಅಥವಾ ಅದಕ್ಕಿಂತ ಹೆಚ್ಚಿನ ಅಂದಾಜು ಮರುದಾಖಲಾತಿ ಸ್ಕೋರ್ ಹೊಂದಿರುವ ದಾಖಲಾತಿಗಳು.",
    },
    "mod_threshold_label": {
        "English": "Moderate Model-Score Threshold",
        "हिन्दी": "मध्यम मॉडल-स्कोर थ्रेशोल्ड",
        "ಕನ್ನಡ": "ಮಧ್ಯಮ ಮಾದರಿ-ಸ್ಕೋರ್ ಮಿತಿ",
    },
    "mod_threshold_help": {
        "English": "Encounters with predicted readmission score between moderate and higher thresholds.",
        "हिन्दी": "मध्यम और उच्च थ्रेशोल्ड के बीच अनुमानित पुनः भर्ती स्कोर वाले एनकाउंटर।",
        "ಕನ್ನಡ": "ಮಧ್ಯಮ ಮತ್ತು ಹೆಚ್ಚಿನ ಮಿತಿಗಳ ನಡುವಿನ ಅಂದಾಜು ಮರುದಾಖಲಾತಿ ಸ್ಕೋರ್ ಹೊಂದಿರುವ ದಾಖಲಾತಿಗಳು.",
    },
    "filters_section_title": {
        "English": "3. Cohort Filters",
        "हिन्दी": "3. कोहोर्ट फ़िल्टर",
        "ಕನ್ನಡ": "3. ಗುಂಪಿನ ಫಿಲ್ಟರ್‌ಗಳು",
    },
    "age_filter_label": {
        "English": "Filter by Age Group",
        "हिन्दी": "आयु वर्ग के अनुसार फ़िल्टर करें",
        "ಕನ್ನಡ": "ವಯಸ್ಸಿನ ಗುಂಪಿನ ಪ್ರಕಾರ ಫಿಲ್ಟರ್ ಮಾಡಿ",
    },
    "age_filter_help": {
        "English": "Leave blank to view all age brackets.",
        "हिन्दी": "सभी आयु वर्ग देखने के लिए खाली छोड़ें।",
        "ಕನ್ನಡ": "ಎಲ್ಲಾ ವಯೋಮಿತಿಗಳನ್ನು ನೋಡಲು ಖಾಲಿ ಬಿಡಿ.",
    },
    "governance_title": {
        "English": "📋 Model Governance Metadata",
        "हिन्दी": "📋 मॉडल प्रशासन मेटाडेटा",
        "ಕನ್ನಡ": "📋 ಮಾದರಿ ಆಡಳಿತ ಮೆಟಾಡೇಟಾ",
    },
    "governance_model_label": {
        "English": "Model",
        "हिन्दी": "मॉडल",
        "ಕನ್ನಡ": "ಮಾದರಿ",
    },
    "governance_model_val": {
        "English": "Logistic Regression (Balanced)",
        "हिन्दी": "लॉजिस्टिक रिग्रेशन (संतुलित)",
        "ಕನ್ನಡ": "ಲಾಜಿಸ್ಟಿಕ್ ರಿಗ್ರೆಷನ್ (ಸಮತೋಲಿತ)",
    },
    "gov_roc_auc": {
        "English": "Test ROC-AUC",
        "हिन्दी": "परीक्षण ROC-AUC",
        "ಕನ್ನಡ": "ಪರೀಕ್ಷಾ ROC-AUC",
    },
    "gov_pr_auc": {
        "English": "Test PR-AUC",
        "हिन्दी": "परीक्षण PR-AUC",
        "ಕನ್ನಡ": "ಪರೀಕ್ಷಾ PR-AUC",
    },
    "gov_recall": {
        "English": "Sensitivity (Recall)",
        "हिन्दी": "संवेदनशीलता (रिकॉल)",
        "ಕನ್ನಡ": "ಸೂಕ್ಷ್ಮತೆ (ಮರುಪಡೆಯುವಿಕೆ)",
    },
    "gov_precision": {
        "English": "Precision",
        "हिन्दी": "सटीकता (प्रिसिजन)",
        "ಕನ್ನಡ": "ನಿಖರತೆ",
    },
    "gov_random_state": {
        "English": "Random State",
        "हिन्दी": "रैंडम स्टेट",
        "ಕನ್ನಡ": "ಯಾದೃಚ್ಛಿಕ ಸ್ಥಿತಿ",
    },
    "governance_caption": {
        "English": "Historical EHR data: UCI Diabetes 130-US Hospitals (1999–2008). Terminal encounters (expired/hospice) excluded.",
        "हिन्दी": "ऐतिहासिक EHR डेटा: UCI डायबिटीज 130-US अस्पताल (1999–2008)। अंतिम एनकाउंटर (मृतक/हॉस्पिस) बाहर रखे गए।",
        "ಕನ್ನಡ": "ಐತಿಹಾಸಿಕ EHR ಡೇಟಾ: UCI ಡಯಾಬಿಟಿಸ್ 130-US ಆಸ್ಪತ್ರೆಗಳು (1999–2008). ಮೃತ/ಹಾಸ್ಪೈಸ್ ದಾಖಲಾತಿಗಳನ್ನು ಹೊರಗಿಡಲಾಗಿದೆ.",
    },

    # Top KPI Metric Cards
    "kpi_filtered_title": {
        "English": "FILTERED ENCOUNTERS",
        "हिन्दी": "फ़िल्टर किए गए एनकाउंटर",
        "ಕನ್ನಡ": "ಫಿಲ್ಟರ್ ಮಾಡಿದ ದಾಖಲಾತಿಗಳು",
    },
    "kpi_eligible_title": {
        "English": "ELIGIBLE ENCOUNTERS",
        "हिन्दी": "योग्य एनकाउंटर",
        "ಕನ್ನಡ": "ಅರ್ಹ ದಾಖಲಾತಿಗಳು",
    },
    "kpi_eligible_sub": {
        "English": "Surviving diabetic cohort",
        "हिन्दी": "जीवित मधुमेह समूह",
        "ಕನ್ನಡ": "ಬದುಕುಳಿದ ಮಧುಮೇಹ ರೋಗಿಗಳ ಗುಂಪು",
    },
    "kpi_of": {
        "English": "of",
        "हिन्दी": "कुल",
        "ಕನ್ನಡ": "ಒಟ್ಟು",
    },
    "kpi_eligible_short": {
        "English": "eligible",
        "हिन्दी": "योग्य में से",
        "ಕನ್ನಡ": "ಅರ್ಹರಲ್ಲಿ",
    },
    "kpi_high_title": {
        "English": "HIGHER-SCORE TIER (≥{threshold:.2f})",
        "हिन्दी": "उच्च-स्कोर श्रेणी (≥{threshold:.2f})",
        "ಕನ್ನಡ": "ಹೆಚ್ಚಿನ-ಸ್ಕೋರ್ ಶ್ರೇಣಿ (≥{threshold:.2f})",
    },
    "kpi_high_sub": {
        "English": "Top priority candidates",
        "हिन्दी": "सर्वोच्च प्राथमिकता वाले मरीज़",
        "ಕನ್ನಡ": "ಅತ್ಯಂತ ಆದ್ಯತೆಯ ರೋಗಿಗಳು",
    },
    "kpi_mod_title": {
        "English": "MODERATE-SCORE TIER (≥{mod:.2f} to <{high:.2f})",
        "हिन्दी": "मध्यम-स्कोर श्रेणी (≥{mod:.2f} से <{high:.2f})",
        "ಕನ್ನಡ": "ಮಧ್ಯಮ-ಸ್ಕೋರ್ ಶ್ರೇಣಿ (≥{mod:.2f} ರಿಂದ <{high:.2f})",
    },
    "kpi_mod_sub": {
        "English": "Secondary follow-up cohort",
        "हिन्दी": "द्वितीयक अनुवर्ती समूह",
        "ಕನ್ನಡ": "ದ್ವಿತೀಯ ಹಂತದ ಆರೈಕೆ ಗುಂಪು",
    },
    "kpi_low_title": {
        "English": "LOWER-SCORE TIER (<{threshold:.2f})",
        "हिन्दी": "निम्न-स्कोर श्रेणी (<{threshold:.2f})",
        "ಕನ್ನಡ": "ಕಡಿಮೆ-ಸ್ಕೋರ್ ಶ್ರೇಣಿ (<{threshold:.2f})",
    },
    "kpi_low_sub": {
        "English": "Routine primary care follow-up",
        "हिन्दी": "नियमित प्राथमिक देखभाल",
        "ಕನ್ನಡ": "ವಾಡಿಕೆಯ ಪ್ರಾಥಮಿಕ ಆರೈಕೆ",
    },

    # Main Tabs
    "tab_queue_title": {
        "English": "📋 High-Priority Outreach Queue",
        "हिन्दी": "📋 उच्च-प्राथमिकता आउटरीच कतार",
        "ಕನ್ನಡ": "📋 ಹೆಚ್ಚಿನ ಆದ್ಯತೆಯ ಔಟ್‌ರೀಚ್ ಸರದಿ",
    },
    "tab_detail_title": {
        "English": "🔍 Encounter Clinical Profile & Attribution",
        "हिन्दी": "🔍 एनकाउंटर नैदानिक प्रोफ़ाइल और विशेषता",
        "ಕನ್ನಡ": "🔍 ದಾಖಲಾತಿ ಕ್ಲಿನಿಕಲ್ ವಿವರ ಮತ್ತು ಕೊಡುಗೆ",
    },
    "tab_diagnostics_title": {
        "English": "📊 Model Metrics & Cohort Diagnostics",
        "हिन्दी": "📊 मॉडल मेट्रिक्स और कोहोर्ट डायग्नोस्टिक्स",
        "ಕನ್ನಡ": "📊 ಮಾದರಿ ಮಾಪನಗಳು ಮತ್ತು ಗುಂಪಿನ ವಿಶ್ಲೇಷಣೆ",
    },

    # Tab 1: Left Column (Model Variables & Distribution)
    "card_variables_title": {
        "English": "Risk Model Variables",
        "हिन्दी": "जोखिम मॉडल चर",
        "ಕನ್ನಡ": "ಅಪಾಯ ಮಾದರಿಯ ಪ್ರಮುಖ ಅಂಶಗಳು",
    },
    "card_variables_subtitle": {
        "English": "Factor weights currently leveraged by the baseline predictive algorithm.",
        "हिन्दी": "बेसलाइन पूर्वानुमान एल्गोरिदम द्वारा उपयोग किए जाने वाले कारक भार।",
        "ಕನ್ನಡ": "ಮೂಲ ಮುನ್ಸೂಚನೆ ಅಲ್ಗಾರಿದಮ್ ಬಳಸುವ ಪ್ರಭಾವಕ ತೂಕಗಳು.",
    },
    "chart_variables_xaxis": {
        "English": "Relative Predictive Weight (Index)",
        "हिन्दी": "सापेक्ष भविष्यसूचक भार (इंडेक्स)",
        "ಕನ್ನಡ": "ಸಾಪೇಕ್ಷ ಮುನ್ಸೂಚನೆ ತೂಕ (ಸೂಚ್ಯಂಕ)",
    },
    "col_clinical_domain": {
        "English": "Clinical Domain",
        "हिन्दी": "नैदानिक डोमेन",
        "ಕನ್ನಡ": "ಕ್ಲಿನಿಕಲ್ ವಿಭಾಗ",
    },
    "col_relative_influence": {
        "English": "Relative Influence",
        "हिन्दी": "सापेक्ष प्रभाव",
        "ಕನ್ನಡ": "ಸಾಪೇಕ್ಷ ಪ್ರಭಾವ",
    },
    "chart_variables_caption": {
        "English": "ℹ️ *Derived dynamically from baseline Logistic Regression standardized coefficients.*",
        "हिन्दी": "ℹ️ *लॉजिस्टिक रिग्रेशन मानकीकृत गुणांकों से गतिशील रूप से प्राप्त।*",
        "ಕನ್ನಡ": "ℹ️ *ಲಾಜಿಸ್ಟಿಕ್ ರಿಗ್ರೆಷನ್ ಗುಣಾಂಕಗಳಿಂದ ಪಡೆಯಲಾಗಿದೆ.*",
    },
    "hist_title": {
        "English": "📈 Risk Score Distribution",
        "हिन्दी": "📈 जोखिम स्कोर वितरण",
        "ಕನ್ನಡ": "📈 ಅಪಾಯದ ಸ್ಕೋರ್ ವಿತರಣೆ",
    },
    "hist_xaxis": {
        "English": "Predicted Score Probability",
        "हिन्दी": "अनुमानित स्कोर संभावना",
        "ಕನ್ನಡ": "ಅಂದಾಜು ಸ್ಕೋರ್ ಸಂಭವನೀಯತೆ",
    },
    "hist_yaxis": {
        "English": "Encounter Count",
        "हिन्दी": "एनकाउंटर संख्या",
        "ಕನ್ನಡ": "ದಾಖಲಾತಿಗಳ ಸಂಖ್ಯೆ",
    },
    "hist_tt_start": {
        "English": "Range Start",
        "हिन्दी": "प्रारंभिक सीमा",
        "ಕನ್ನಡ": "ಆರಂಭಿಕ ಮಿತಿ",
    },
    "hist_tt_end": {
        "English": "Range End",
        "हिन्दी": "अंतिम सीमा",
        "ಕನ್ನಡ": "ಅಂತಿಮ ಮಿತಿ",
    },
    "hist_tt_count": {
        "English": "Encounter Count",
        "हिन्दी": "एनकाउंटर संख्या",
        "ಕನ್ನಡ": "ದಾಖಲಾತಿಗಳ ಸಂಖ್ಯೆ",
    },
    "cohort_mean_score": {
        "English": "Cohort mean score",
        "हिन्दी": "कोहोर्ट औसत स्कोर",
        "ಕನ್ನಡ": "ಗುಂಪಿನ ಸರಾಸರಿ ಸ್ಕೋರ್",
    },
    "cohort_median_score": {
        "English": "Median",
        "हिन्दी": "माध्यिका",
        "ಕನ್ನಡ": "ಮಧ್ಯಮಾಂಕ",
    },

    # Tab 1: Right Column (Outreach Queue Table)
    "card_queue_title": {
        "English": "High-Priority Outreach Queue",
        "हिन्दी": "उच्च-प्राथमिकता आउटरीच कतार",
        "ಕನ್ನಡ": "ಹೆಚ್ಚಿನ ಆದ್ಯತೆಯ ಔಟ್‌ರೀಚ್ ಸರದಿ",
    },
    "card_queue_subtitle": {
        "English": "Displaying top {count} encounters ranked by model readmission score.",
        "हिन्दी": "मॉडल पुनः भर्ती स्कोर द्वारा रैंक किए गए शीर्ष {count} एनकाउंटर प्रदर्शित हैं।",
        "ಕನ್ನಡ": "ಮಾದರಿ ಮರುದಾಖಲಾತಿ ಸ್ಕೋರ್‌ನಿಂದ ಶ್ರೇಣೀಕರಿಸಲಾದ ಅಗ್ರ {count} ದಾಖಲಾತಿಗಳನ್ನು ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತಿದೆ.",
    },
    "capacity_slots_label": {
        "English": "Capacity: {capacity} Slots",
        "हिन्दी": "क्षमता: {capacity} स्लॉट",
        "ಕನ್ನಡ": "ಸಾಮರ್ಥ್ಯ: {capacity} ಸ್ಲಾಟ್‌ಗಳು",
    },
    "col_rank": {
        "English": "Rank",
        "हिन्दी": "रैंक",
        "ಕನ್ನಡ": "ಶ್ರೇಣಿ",
    },
    "col_encounter_id": {
        "English": "Encounter ID",
        "हिन्दी": "एनकाउंटर आईडी",
        "ಕನ್ನಡ": "ದಾಖಲಾತಿ ಐಡಿ",
    },
    "col_score_pct": {
        "English": "Score (%)",
        "हिन्दी": "स्कोर (%)",
        "ಕನ್ನಡ": "ಸ್ಕೋರ್ (%)",
    },
    "col_model_tier": {
        "English": "Model Tier",
        "हिन्दी": "मॉडल श्रेणी",
        "ಕನ್ನಡ": "ಮಾದರಿ ಶ್ರೇಣಿ",
    },
    "col_primary_driver": {
        "English": "Primary Driver",
        "हिन्दी": "प्राथमिक कारक",
        "ಕನ್ನಡ": "ಮುಖ್ಯ ಪ್ರಭಾವಕ",
    },
    "col_age_group": {
        "English": "Age Group",
        "हिन्दी": "आयु वर्ग",
        "ಕನ್ನಡ": "ವಯಸ್ಸಿನ ಗುಂಪು",
    },
    "col_stay_days": {
        "English": "Stay (Days)",
        "हिन्दी": "अवधि (दिन)",
        "ಕನ್ನಡ": "ವಾಸ್ತವ್ಯ (ದಿನಗಳು)",
    },
    "col_prior_admissions": {
        "English": "Prior Admissions",
        "हिन्दी": "पूर्व दाखिले",
        "ಕನ್ನಡ": "ಹಿಂದಿನ ದಾಖಲಾತಿಗಳು",
    },
    "queue_caption": {
        "English": (
            "💡 *Pseudonymous identifiers (#HF-XXXX) prevent direct patient identification. "
            "Select any encounter in Tab 2 to inspect non-identifying features and mathematical attribution.*"
        ),
        "हिन्दी": (
            "💡 *छद्म पहचानकर्ता (#HF-XXXX) प्रत्यक्ष रोगी पहचान को रोकते हैं। "
            "गैर-पहचान योग्य विशेषताओं और गणितीय विशेषता का निरीक्षण करने के लिए टैब 2 में किसी भी एनकाउंटर का चयन करें।*"
        ),
        "ಕನ್ನಡ": (
            "💡 *ಗುಪ್ತ ಗುರುತುಗಳು (#HF-XXXX) ರೋಗಿಯ ನೇರ ಗುರುತಿಸುವಿಕೆಯನ್ನು ತಡೆಯುತ್ತವೆ. "
            "ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಲು ಟ್ಯಾಬ್ 2 ರಲ್ಲಿ ಯಾವುದೇ ದಾಖಲಾತಿಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.*"
        ),
    },

    # Tab 2: Encounter Clinical Profile & Attribution
    "card_profile_title": {
        "English": "Encounter Clinical Profile & Feature Attribution",
        "हिन्दी": "एनकाउंटर नैदानिक प्रोफ़ाइल और विशेषता",
        "ಕನ್ನಡ": "ದಾಖಲಾತಿ ಕ್ಲಿನಿಕಲ್ ವಿವರ ಮತ್ತು ಕೊಡುಗೆ",
    },
    "card_profile_subtitle": {
        "English": (
            "Inspect non-identifying encounter characteristics and examine the exact mathematical contributions "
            "to the baseline Logistic Regression prediction."
        ),
        "हिन्दी": (
            "गैर-पहचान योग्य एनकाउंटर विशेषताओं का निरीक्षण करें और लॉजिस्टिक रिग्रेशन भविष्यवाणी में सटीक गणितीय योगदान की जांच करें।"
        ),
        "ಕನ್ನಡ": (
            "ದಾಖಲಾತಿಯ ಕ್ಲಿನಿಕಲ್ ಗುಣಲಕ್ಷಣಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ಲಾಜಿಸ್ಟಿಕ್ ರಿಗ್ರೆಷನ್ ಭವಿಷ್ಯವಾಣಿಗೆ ನಿಖರವಾದ ಗಣಿತದ ಕೊಡುಗೆಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ."
        ),
    },
    "select_encounter_label": {
        "English": "Select Encounter from Outreach Queue:",
        "हिन्दी": "आउटरीच कतार से एनकाउंटर चुनें:",
        "ಕನ್ನಡ": "ಔಟ್‌ರೀಚ್ ಸರದಿಯಿಂದ ದಾಖಲಾತಿಯನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
    },
    "select_encounter_help": {
        "English": "Choose an encounter to audit its clinical profile and model driver breakdown.",
        "हिन्दी": "नैदानिक प्रोफ़ाइल और मॉडल ड्राइवर विश्लेषण के लिए एनकाउंटर चुनें।",
        "ಕನ್ನಡ": "ಕ್ಲಿನಿಕಲ್ ವಿವರ ಮತ್ತು ಮಾದರಿ ಪ್ರಭಾವಕ ವಿಶ್ಲೇಷಣೆಗಾಗಿ ದಾಖಲಾತಿಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
    },
    "metric_pred_score": {
        "English": "Predicted Readmission Score",
        "हिन्दी": "अनुमानित पुनः भर्ती स्कोर",
        "ಕನ್ನಡ": "ಅಂದಾಜು ಮರುದಾಖಲಾತಿ ಸ್ಕೋರ್",
    },
    "metric_classification": {
        "English": "Score Classification",
        "हिन्दी": "स्कोर वर्गीकरण",
        "ಕನ್ನಡ": "ಸ್ಕೋರ್ ವರ್ಗೀಕರಣ",
    },
    "metric_primary_driver": {
        "English": "Primary Driver",
        "हिन्दी": "प्राथमिक कारक",
        "ಕನ್ನಡ": "ಮುಖ್ಯ ಪ್ರಭಾವಕ",
    },

    # Summary Box Header
    "summary_box_header": {
        "English": "Patient Summary & Clinical Context",
        "हिन्दी": "रोगी सारांश और नैदानिक संदर्भ",
        "ಕನ್ನಡ": "ರೋಗಿಯ ಸಾರಾಂಶ ಮತ್ತು ಕ್ಲಿನಿಕಲ್ ಸಂದರ್ಭ",
    },
    "summary_box_factors_title": {
        "English": "Key Model Drivers & Recorded Context",
        "हिन्दी": "प्रमुख मॉडल चालक और दर्ज संदर्भ",
        "ಕನ್ನಡ": "ಪ್ರಮುಖ ಮಾದರಿ ಪ್ರಭಾವಕಗಳು ಮತ್ತು ದಾಖಲಿತ ಸಂದರ್ಭ",
    },
    "summary_box_followup_label": {
        "English": "Transitional Care Consideration:",
        "हिन्दी": "संक्रमणकालीन देखभाल विचार:",
        "ಕನ್ನಡ": "ಮುಂದಿನ ಆರೈಕೆ ಪರಿಶೀಲನೆ:",
    },

    # Profile Columns 1, 2, 3
    "prof_demographics_title": {
        "English": "👤 Demographics & Entry",
        "हिन्दी": "👤 जनसांख्यिकी और प्रवेश",
        "ಕನ್ನಡ": "👤 ಜನಸಂಖ್ಯಾಶಾಸ್ತ್ರ ಮತ್ತು ಪ್ರವೇಶ",
    },
    "prof_age_bracket": {
        "English": "Age Bracket",
        "हिन्दी": "आयु वर्ग",
        "ಕನ್ನಡ": "ವಯಸ್ಸಿನ ವರ್ಗ",
    },
    "prof_gender": {
        "English": "Gender",
        "हिन्दी": "लिंग",
        "ಕನ್ನಡ": "ಲಿಂಗ",
    },
    "prof_race": {
        "English": "Race",
        "हिन्दी": "जातीयता/मूल",
        "ಕನ್ನಡ": "ಜನಾಂಗ",
    },
    "prof_adm_type": {
        "English": "Admission Type ID",
        "हिन्दी": "दाखिला प्रकार आईडी",
        "ಕನ್ನಡ": "ದಾಖಲಾತಿ ಪ್ರಕಾರದ ಐಡಿ",
    },
    "prof_adm_source": {
        "English": "Admission Source ID",
        "हिन्दी": "दाखिला स्रोत आईडी",
        "ಕನ್ನಡ": "ದಾಖಲಾತಿ ಮೂಲದ ಐಡಿ",
    },
    "prof_utilization_title": {
        "English": "🏥 Hospital Utilization",
        "हिन्दी": "🏥 अस्पताल उपयोग",
        "ಕನ್ನಡ": "🏥 ಆಸ್ಪತ್ರೆ ಬಳಕೆ",
    },
    "prof_stay_days": {
        "English": "Length of Stay",
        "हिन्दी": "अस्पताल अवधि",
        "ಕನ್ನಡ": "ವಾಸ್ತವ್ಯದ ಅವಧಿ",
    },
    "prof_prior_adm": {
        "English": "Prior Admissions",
        "हिन्दी": "पूर्व दाखिले",
        "ಕನ್ನಡ": "ಹಿಂದಿನ ದಾಖಲಾತಿಗಳು",
    },
    "prof_prior_er": {
        "English": "Prior ER Visits (1 yr)",
        "हिन्दी": "पूर्व आपातकालीन दौरे (1 वर्ष)",
        "ಕನ್ನಡ": "ಹಿಂದಿನ ತುರ್ತು ಭೇಟಿಗಳು (1 ವರ್ಷ)",
    },
    "prof_prior_op": {
        "English": "Prior Outpatient Visits",
        "हिन्दी": "पूर्व बाह्यरोगी दौरे",
        "ಕನ್ನಡ": "ಹಿಂದಿನ ಹೊರರೋಗಿ ಭೇಟಿಗಳು",
    },
    "prof_lab_tests": {
        "English": "Lab Tests Ordered",
        "हिन्दी": "लैब परीक्षण आदेशित",
        "ಕನ್ನಡ": "ಮಾಡಲಾದ ಲ್ಯಾಬ್ ಪರೀಕ್ಷೆಗಳು",
    },
    "prof_med_count": {
        "English": "Distinct Medications",
        "हिन्दी": "निर्धारित दवाएं",
        "ಕನ್ನಡ": "ನಿಗದಿತ ಔಷಧಿಗಳ ಸಂಖ್ಯೆ",
    },
    "days_suffix": {
        "English": "days",
        "हिन्दी": "दिन",
        "ಕನ್ನಡ": "ದಿನಗಳು",
    },
    "prof_glycemic_title": {
        "English": "🧪 Glycemic & Medication Status",
        "हिन्दी": "🧪 ग्लूकोज और दवा स्थिति",
        "ಕನ್ನಡ": "🧪 ಗ್ಲೈಸೆಮಿಕ್ ಮತ್ತು ಔಷಧಿ ಸ್ಥಿತಿ",
    },
    "prof_a1c": {
        "English": "HbA1c Lab Result",
        "हिन्दी": "HbA1c लैब परिणाम",
        "ಕನ್ನಡ": "HbA1c ಲ್ಯಾಬ್ ಫಲಿತಾಂಶ",
    },
    "prof_glucose": {
        "English": "Max Glucose Serum",
        "हिन्दी": "अधिकतम सीरम ग्लूकोज",
        "ಕನ್ನಡ": "ಗರಿಷ್ಠ ಸೀರಮ್ ಗ್ಲೂಕೋಸ್",
    },
    "prof_insulin": {
        "English": "Insulin Status",
        "हिन्दी": "इंसुलिन स्थिति",
        "ಕನ್ನಡ": "ಇನ್ಸುಲಿನ್ ಸ್ಥಿತಿ",
    },
    "prof_med_chg": {
        "English": "Medication Changed",
        "हिन्दी": "दवा में बदलाव",
        "ಕನ್ನಡ": "ಔಷಧಿಯಲ್ಲಿ ಬದಲಾವಣೆ",
    },
    "prof_dm_med": {
        "English": "Diabetes Med Prescribed",
        "हिन्दी": "मधुमेह दवा निर्धारित",
        "ಕನ್ನಡ": "ಮಧುಮೇಹ ಔಷಧಿ ನೀಡಲಾಗಿದೆಯೇ",
    },
    "prof_primary_diag": {
        "English": "Primary ICD-9 Code",
        "हिन्दी": "प्राथमिक ICD-9 कोड",
        "ಕನ್ನಡ": "ಪ್ರಾಥಮಿಕ ICD-9 ಕೋಡ್",
    },

    # Attribution Charts
    "attribution_section_title": {
        "English": "🔬 Mathematical Model Attribution (Log-Odds Contributions)",
        "हिन्दी": "🔬 गणितीय मॉडल विशेषता (लॉग-ऑड्स योगदान)",
        "ಕನ್ನಡ": "🔬 ಗಣಿತ ಮಾದರಿ ಕೊಡುಗೆ (ಲಾಗ್-ಆಡ್ಸ್ ಕೊಡುಗೆಗಳು)",
    },
    "attribution_caption": {
        "English": (
            "For this Logistic Regression model, log-odds are linear: $\\text{logit}(p) = \\beta_0 + \\sum \\beta_i x_i$. "
            "Bars indicate the exact mathematical coefficient contributions $(\\beta_i \\cdot x_i)$ of this encounter's preprocessed features to the model's linear score. "
            "Negative contributions lower this model's score. **These represent observational statistical associations in historical data, not causal medical effects.**"
        ),
        "हिन्दी": (
            "इस लॉजिस्टिक रिग्रेशन मॉडल के लिए, लॉग-ऑड्स रैखिक हैं: $\\text{logit}(p) = \\beta_0 + \\sum \\beta_i x_i$। "
            "बार मॉडल के रैखिक स्कोर में इस एनकाउंटर की पूर्व-संसाधित विशेषताओं के सटीक गणितीय गुणांक योगदान $(\\beta_i \\cdot x_i)$ को दर्शाते हैं। "
            "नकारात्मक योगदान इस मॉडल के स्कोर को कम करते हैं। **ये ऐतिहासिक डेटा में अवलोकनात्मक सांख्यिकीय संबंधों का प्रतिनिधित्व करते हैं, चिकित्सीय कार्य-कारण का नहीं।**"
        ),
        "ಕನ್ನಡ": (
            "ಈ ಲಾಜಿಸ್ಟಿಕ್ ರಿಗ್ರೆಷನ್ ಮಾದರಿಗೆ, ಲಾಗ್-ಆಡ್ಸ್ ರೇಖೀಯವಾಗಿದೆ: $\\text{logit}(p) = \\beta_0 + \\sum \\beta_i x_i$. "
            "ಗ್ರಾಫ್‌ಗಳು ಮಾದರಿಯ ರೇಖೀಯ ಸ್ಕೋರಿಗೆ ಈ ದಾಖಲಾತಿಯ ಪೂರ್ವ-ಸಂಸ್ಕರಿಸಿದ ವೈಶಿಷ್ಟ್ಯಗಳ ನಿಖರವಾದ ಗಣಿತದ ಗುಣಾಂಕ ಕೊಡುಗೆಗಳನ್ನು $(\\beta_i \\cdot x_i)$ ಸೂಚಿಸುತ್ತವೆ. "
            "ಋಣಾತ್ಮಕ ಕೊಡುಗೆಗಳು ಈ ಮಾದರಿಯ ಸ್ಕೋರ್ ಅನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತವೆ. **ಇವು ಐತಿಹಾಸಿಕ ಡೇಟಾದಲ್ಲಿನ ವೀಕ್ಷಣಾ ಸಂಖ್ಯಾಶಾಸ್ತ್ರೀಯ ಸಂಬಂಧಗಳನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತವೆ, ವೈದ್ಯಕೀಯ ಕಾರಣಗಳನ್ನಲ್ಲ.**"
        ),
    },
    "pos_drivers_title": {
        "English": "##### 🔺 Top Risk-Increasing Drivers $(\\beta_i x_i > 0)$",
        "हिन्दी": "##### 🔺 शीर्ष जोखिम बढ़ाने वाले कारक $(\\beta_i x_i > 0)$",
        "ಕನ್ನಡ": "##### 🔺 ಅಪಾಯ ಹೆಚ್ಚಿಸುವ ಪ್ರಮುಖ ಅಂಶಗಳು $(\\beta_i x_i > 0)$",
    },
    "pos_chart_xaxis": {
        "English": "Positive Log-Odds Contribution",
        "हिन्दी": "सकारात्मक लॉग-ऑड्स योगदान",
        "ಕನ್ನಡ": "ಧನಾತ್ಮಕ ಲಾಗ್-ಆಡ್ಸ್ ಕೊಡುಗೆ",
    },
    "pos_empty_state": {
        "English": "No significant positive risk drivers identified for this encounter.",
        "हिन्दी": "इस एनकाउंटर के लिए कोई महत्वपूर्ण सकारात्मक जोखिम कारक नहीं पाया गया।",
        "ಕನ್ನಡ": "ಈ ದಾಖಲಾತಿಗೆ ಯಾವುದೇ ಪ್ರಮುಖ ಧನಾತ್ಮಕ ಅಪಾಯದ ಅಂಶಗಳು ಕಂಡುಬಂದಿಲ್ಲ.",
    },
    "neg_drivers_title": {
        "English": "##### 🔻 Top Score-Lowering Factors $(\\beta_i x_i < 0)$",
        "हिन्दी": "##### 🔻 शीर्ष स्कोर घटाने वाले कारक $(\\beta_i x_i < 0)$",
        "ಕನ್ನಡ": "##### 🔻 ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುವ ಪ್ರಮುಖ ಅಂಶಗಳು $(\\beta_i x_i < 0)$",
    },
    "neg_chart_xaxis": {
        "English": "Score-Lowering Log-Odds Contribution $(\\beta_i x_i < 0)$",
        "हिन्दी": "स्कोर घटाने वाला लॉग-ऑड्स योगदान $(\\beta_i x_i < 0)$",
        "ಕನ್ನಡ": "ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುವ ಲಾಗ್-ಆಡ್ಸ್ ಕೊಡುಗೆ $(\\beta_i x_i < 0)$",
    },
    "neg_empty_state": {
        "English": "No significant score-lowering factors identified for this encounter.",
        "हिन्दी": "इस एनकाउंटर के लिए कोई महत्वपूर्ण स्कोर घटाने वाला कारक नहीं पाया गया।",
        "ಕನ್ನಡ": "ಈ ದಾಖಲಾತಿಗೆ ಯಾವುದೇ ಪ್ರಮುಖ ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುವ ಅಂಶಗಳು ಕಂಡುಬಂದಿಲ್ಲ.",
    },
    "intercept_caption": {
        "English": "Base model intercept $(\\beta_0)$: `{val:.3f}`",
        "हिन्दी": "बेस मॉडल इंटरसेप्ट $(\\beta_0)$: `{val:.3f}`",
        "ಕನ್ನಡ": "ಮೂಲ ಮಾದರಿಯ ಇಂಟರ್‌ಸೆಪ್ಟ್ $(\\beta_0)$: `{val:.3f}`",
    },

    # Graph / Data View Toggle & Table Headers
    "btn_graph": {
        "English": "Graph",
        "हिन्दी": "ग्राफ",
        "ಕನ್ನಡ": "ಗ್ರಾಫ್",
    },
    "btn_data": {
        "English": "Data",
        "हिन्दी": "डेटा",
        "ಕನ್ನಡ": "ಡೇಟಾ",
    },
    "lbl_view_mode": {
        "English": "View Mode",
        "हिन्दी": "दृश्य मोड",
        "ಕನ್ನಡ": "ವೀಕ್ಷಣೆ ಮೋಡ್",
    },
    "hist_col_range": {
        "English": "Score Range",
        "हिन्दी": "स्कोर सीमा",
        "ಕನ್ನಡ": "ಸ್ಕೋರ್ ಶ್ರೇಣಿ",
    },
    "hist_col_count": {
        "English": "Encounters",
        "हिन्दी": "एनकाउंटर संख्या",
        "ಕನ್ನಡ": "ದಾಖಲಾತಿಗಳ ಸಂಖ್ಯೆ",
    },
    "hist_col_pct": {
        "English": "Percentage",
        "हिन्दी": "प्रतिशत",
        "ಕನ್ನಡ": "ಶೇಕಡಾವಾರು",
    },
    "col_factor": {
        "English": "Clinical Factor",
        "हिन्दी": "नैदानिक कारक",
        "ಕನ್ನಡ": "ಕ್ಲಿನಿಕಲ್ ಅಂಶ",
    },
    "col_impact": {
        "English": "Log-Odds Impact (βᵢ xᵢ)",
        "हिन्दी": "लॉग-ऑड्स प्रभाव (βᵢ xᵢ)",
        "ಕನ್ನಡ": "ಲಾಗ್-ಆಡ್ಸ್ ಪ್ರಭಾವ (βᵢ xᵢ)",
    },
    "col_feature_id": {
        "English": "Model Feature",
        "हिन्दी": "मॉडल विशेषता",
        "ಕನ್ನಡ": "ಮಾದರಿ ವೈಶಿಷ್ಟ್ಯ",
    },

    # Patient Data-Quality Notice
    "dq_title": {
        "English": "Patient Data-Quality & Record Completeness Notice",
        "हिन्दी": "रोगी डेटा-गुणवत्ता और रिकॉर्ड पूर्णता सूचना",
        "ಕನ್ನಡ": "ರೋಗಿ ಡೇಟಾ-ಗುಣಮಟ್ಟ ಮತ್ತು ದಾಖಲೆಯ ಸಂಪೂರ್ಣತೆಯ ಸೂಚನೆ",
    },
    "dq_clean": {
        "English": "✅ No data-quality anomalies detected by basic baseline checks (HbA1c, primary diagnosis, and acute utilization bounds). Note: Basic heuristic checks do not guarantee clinical completeness.",
        "हिन्दी": "✅ बुनियादी आधारभूत जांचों (HbA1c, प्राथमिक निदान, और तीव्र उपयोग सीमाओं) द्वारा कोई डेटा-गुणवत्ता विसंगति नहीं पाई गई। नोट: बुनियादी हेयूरिस्टिक जांच नैदानिक पूर्णता की गारंटी नहीं देती है।",
        "ಕನ್ನಡ": "✅ ಮೂಲಭೂತ ತಪಾಸಣೆಗಳಿಂದ (HbA1c, ಪ್ರಾಥಮಿಕ ರೋಗನಿರ್ಣಯ, ಮತ್ತು ತೀವ್ರ ಬಳಕೆಯ ಮಿತಿಗಳು) ಯಾವುದೇ ಡೇಟಾ ಗುಣಮಟ್ಟದ ದೋಷಗಳು ಕಂಡುಬಂದಿಲ್ಲ. ಸೂಚನೆ: ಮೂಲಭೂತ ನಿಯಮ ತಪಾಸಣೆಗಳು ವೈದ್ಯಕೀಯ ಸಂಪೂರ್ಣತೆಯನ್ನು ಖಚಿತಪಡಿಸುವುದಿಲ್ಲ.",
    },
    "dq_disclaimer": {
        "English": "Heuristic data-quality check for demo review; does not constitute automated clinical validation or error certification.",
        "हिन्दी": "डेमो समीक्षा के लिए हेयूरिस्टिक डेटा-गुणवत्ता जांच; यह स्वचालित नैदानिक सत्यापन या त्रुटि प्रमाणीकरण नहीं है।",
        "ಕನ್ನಡ": "ಡೆಮೊ ಪರಿಶೀಲನೆಗಾಗಿ ನಿಯಮ-ಆಧಾರಿತ ಡೇಟಾ ಗುಣಮಟ್ಟದ ತಪಾಸಣೆ; ಇದು ಸ್ವಯಂಚಾಲಿತ ವೈದ್ಯಕೀಯ ಮೌಲ್ಯೀಕರಣವನ್ನು ಪ್ರತಿನಿಧಿಸುವುದಿಲ್ಲ.",
    },
    "dq_type_missing_lab": {
        "English": "Missing Clinical Record",
        "हिन्दी": "लापता नैदानिक रिकॉर्ड",
        "ಕನ್ನಡ": "ದಾಖಲಾಗದ ಕ್ಲಿನಿಕಲ್ ದಾಖಲೆ",
    },
    "dq_missing_a1c": {
        "English": "HbA1c glycemic control test was not documented during this hospitalization.",
        "हिन्दी": "इस अस्पताल में भर्ती के दौरान HbA1c ग्लाइसेमिक नियंत्रण परीक्षण दर्ज नहीं किया गया था।",
        "ಕನ್ನಡ": "ಈ ಆಸ್ಪತ್ರೆ ದಾಖಲಾತಿಯ ಸಮಯದಲ್ಲಿ HbA1c ಗ್ಲೈಸೆಮಿಕ್ ನಿಯಂತ್ರಣ ಪರೀಕ್ಷೆಯನ್ನು ದಾಖಲಿಸಲಾಗಿಲ್ಲ.",
    },
    "dq_type_missing_diag": {
        "English": "Missing Clinical Record",
        "हिन्दी": "लापता नैदानिक रिकॉर्ड",
        "ಕನ್ನಡ": "ದಾಖಲಾಗದ ಕ್ಲಿನಿಕಲ್ ದಾಖಲೆ",
    },
    "dq_missing_diag": {
        "English": "Primary admission diagnosis code is unrecorded ('?').",
        "हिन्दी": "प्राथमिक प्रवेश निदान कोड दर्ज नहीं है ('?')।",
        "ಕನ್ನಡ": "ಪ್ರಾಥಮಿಕ ದಾಖಲಾತಿ ರೋಗನಿರ್ಣಯ ಕೋಡ್ ದಾಖಲಾಗಿಲ್ಲ ('?').",
    },
    "dq_type_unusual_util": {
        "English": "Unusual value; review record",
        "हिन्दी": "असामान्य मान; रिकॉर्ड की समीक्षा करें",
        "ಕನ್ನಡ": "ಅಸಾಮಾನ್ಯ ಮೌಲ್ಯ; ದಾಖಲೆಯನ್ನು ಪರಿಶೀಲಿಸಿ",
    },
    "dq_unusual_util": {
        "English": "Unusual acute utilization ({inpatient} prior admissions, {emergency} ER visits in past year).",
        "हिन्दी": "असामान्य तीव्र उपयोग (पिछले वर्ष में {inpatient} पूर्व दाखिले, {emergency} आपातकालीन दौरे)।",
        "ಕನ್ನಡ": "ಅಸಾಮಾನ್ಯ ತೀವ್ರ ಬಳಕೆ (ಕಳೆದ ವರ್ಷದಲ್ಲಿ {inpatient} ಹಿಂದಿನ ದಾಖಲಾತಿಗಳು, {emergency} ತುರ್ತು ಭೇಟಿಗಳು).",
    },
    "dq_type_unusual_stay": {
        "English": "Unusual value; review record",
        "हिन्दी": "असामान्य मान; रिकॉर्ड की समीक्षा करें",
        "ಕನ್ನಡ": "ಅಸಾಮಾನ್ಯ ಮೌಲ್ಯ; ದಾಖಲೆಯನ್ನು ಪರಿಶೀಲಿಸಿ",
    },
    "dq_unusual_stay": {
        "English": "Unusual hospital stay duration ({days} days; dataset ceiling is 14 days).",
        "हिन्दी": "असामान्य अस्पताल प्रवास अवधि ({days} दिन; डेटासेट की अधिकतम सीमा 14 दिन है)।",
        "ಕನ್ನಡ": "ಅಸಾಮಾನ್ಯ ಆಸ್ಪತ್ರೆ ವಾಸ್ತವ್ಯದ ಅವಧಿ ({days} ದಿನಗಳು; ಡೇಟಾಸೆಟ್ ಗರಿಷ್ಠ ಮಿತಿ 14 ದಿನಗಳು).",
    },
    "dq_type_unusual_meds": {
        "English": "Unusual value; review record",
        "हिन्दी": "असामान्य मान; रिकॉर्ड की समीक्षा करें",
        "ಕನ್ನಡ": "ಅಸಾಮಾನ್ಯ ಮೌಲ್ಯ; ದಾಖಲೆಯನ್ನು ಪರಿಶೀಲಿಸಿ",
    },
    "dq_unusual_meds": {
        "English": "Unusual medication count ({meds} medications administered).",
        "हिन्दी": "असामान्य दवा मात्रा ({meds} दवाएं दी गईं)।",
        "ಕನ್ನಡ": "ಅಸಾಮಾನ್ಯ ಔಷಧಿ ಪ್ರಮಾಣ ({meds} ಔಷಧಿಗಳನ್ನು ನೀಡಲಾಗಿದೆ).",
    },

    # Risk-Tier Boundary Indicator
    "boundary_indicator_near": {
        "English": "⚠️ Near risk-tier boundary ({score:.1f}% is within ±{margin:.1f}% of {cutoff:.2f} cutoff)",
        "हिन्दी": "⚠️ जोखिम-टियर सीमा के निकट ({score:.1f}% कटऑफ {cutoff:.2f} के ±{margin:.1f}% के भीतर है)",
        "ಕನ್ನಡ": "⚠️ ಅಪಾಯದ ಹಂತದ ಗಡಿಯ ಸಮೀಪ ({score:.1f}% ಕಟ್‌ಆಫ್ {cutoff:.2f} ರ ±{margin:.1f}% ಒಳಗೆ ಇದೆ)",
    },
    "boundary_indicator_help": {
        "English": "Threshold-proximity heuristic: This encounter's estimated score is close to a triage cutoff (0.40 or 0.70). This is a simple boundary proximity indicator, NOT a measure of statistical uncertainty, confidence interval, or calibration.",
        "हिन्दी": "सीमा-निकटता हेयूरिस्टिक: इस एनकाउंटर का अनुमानित स्कोर ट्राइएज कटऑफ (0.40 या 0.70) के करीब है। यह केवल एक सीमा-निकटता हेयूरिस्टिक है, सांख्यिकीय अनिश्चितता अनुमान, विश्वास अंतराल या अंशांकन मीट्रिक नहीं है।",
        "ಕನ್ನಡ": "ಮಿತಿ-ಸಮೀಪದ ನಿಯಮ: ಈ ದಾಖಲಾತಿಯ ಅಂದಾಜು ಸ್ಕೋರ್ ವರ್ಗೀಕರಣದ ಕಟ್‌ಆಫ್ (0.40 ಅಥವಾ 0.70) ಹತ್ತಿರದಲ್ಲಿದೆ. ಇದು ಕೇವಲ ಮಿತಿ-ಸಾಮೀಪ್ಯ ನಿಯಮವಾಗಿದೆ, ಸಂಖ್ಯಾಶಾಸ್ತ್ರೀಯ ಅನಿಶ್ಚಿತತೆ, ವಿಶ್ವಾಸಾರ್ಹತೆಯ ಮಧ್ಯಂತರ ಅಥವಾ ಮಾಪನಾಂಕ ನಿರ್ಣಯವಲ್ಲ.",
    },
    "boundary_indicator_comfortable": {
        "English": "Score is comfortably within tier bounds",
        "हिन्दी": "स्कोर टियर सीमाओं के भीतर सुरक्षित रूप से स्थित है",
        "ಕನ್ನಡ": "ಸ್ಕೋರ್ ಹಂತದ ಮಿತಿಗಳ ಒಳಗೆ ಸಮರ್ಪಕವಾಗಿದೆ",
    },

    # Retrospective Top-10 vs Top-20 Capacity Simulation
    "retro_title": {
        "English": "📊 Retrospective Capacity Simulation: Top 10 vs. Top 20 (Historical Records)",
        "हिन्दी": "📊 पूर्वव्यापी क्षमता सिमुलेशन: शीर्ष 10 बनाम शीर्ष 20 (ऐतिहासिक रिकॉर्ड)",
        "ಕನ್ನಡ": "📊 ಹಿಂದಿನ ಸಾಮರ್ಥ್ಯ ಸಿಮ್ಯುಲೇಶನ್: ಅಗ್ರ 10 ವಿರುದ್ಧ ಅಗ್ರ 20 (ಐತಿಹಾಸಿಕ ದಾಖಲೆಗಳು)",
    },
    "retro_subtitle": {
        "English": "Retrospective evaluation on historical dataset records (<30d readmissions). This section reflects historical data evaluation only, NOT prospective clinical performance.",
        "हिन्दी": "ऐतिहासिक डेटासेट रिकॉर्ड (<30 दिन पुनः भर्ती) पर पूर्वव्यापी मूल्यांकन। यह अनुभाग केवल ऐतिहासिक डेटा मूल्यांकन को दर्शाता है, संभावित नैदानिक प्रदर्शन को नहीं।",
        "ಕನ್ನಡ": "ಐತಿಹಾಸಿಕ ಡೇಟಾಸೆಟ್ ದಾಖಲೆಗಳ (<30 ದಿನಗಳ ಮರುದಾಖಲಾತಿಗಳು) ಮೇಲಿನ ಹಿಂದಿನ ಮೌಲ್ಯಮಾಪನ. ಈ ವಿಭಾಗವು ಕೇವಲ ಐತಿಹಾಸಿಕ ಡೇಟಾ ಮೌಲ್ಯಮಾಪನವನ್ನು ಪ್ರತಿಬಿಂಬಿಸುತ್ತದೆ, ಭವಿಷ್ಯದ ವೈದ್ಯಕೀಯ ಫಲಿತಾಂಶವನ್ನಲ್ಲ.",
    },
    "retro_col_cohort": {
        "English": "Outreach Cohort",
        "हिन्दी": "आउटरीच समूह",
        "ಕನ್ನಡ": "ಔಟ್‌ರೀಚ್ ಗುಂಪು",
    },
    "retro_col_k": {
        "English": "Capacity (K)",
        "हिन्दी": "क्षमता (K)",
        "ಕನ್ನಡ": "ಸಾಮರ್ಥ್ಯ (K)",
    },
    "retro_col_hits": {
        "English": "Historical Early Readmissions (<30d)",
        "हिन्दी": "ऐतिहासिक प्रारंभिक पुनः भर्तियां (<30 दिन)",
        "ಕನ್ನಡ": "ಐತಿಹಾಸಿಕ ಆರಂಭಿಕ ಮರುದಾಖಲಾತಿಗಳು (<30 ದಿನ)",
    },
    "retro_col_precision": {
        "English": "Precision@K (Historical Readmissions / K)",
        "हिन्दी": "Precision@K (ऐतिहासिक पुनः भर्तियां / K)",
        "ಕನ್ನಡ": "Precision@K (ಐತಿಹಾಸಿಕ ಮರುದಾಖಲಾತಿಗಳು / K)",
    },
    "retro_top_10_label": {
        "English": "Top 10 Encounters",
        "हिन्दी": "शीर्ष 10 एनकाउंटर",
        "ಕನ್ನಡ": "ಅಗ್ರ 10 ದಾಖಲಾತಿಗಳು",
    },
    "retro_top_20_label": {
        "English": "Top 20 Encounters",
        "हिन्दी": "शीर्ष 20 एनकाउंटर",
        "ಕನ್ನಡ": "ಅಗ್ರ 20 ದಾಖಲಾತಿಗಳು",
    },
    "retro_expansion_summary": {
        "English": "Expanding outreach from Top 10 to Top 20 encounters identifies **{additional} additional** historical early readmissions (from {hits_10} to {hits_20}). Precision@10: **{p10:.1f}%** ({hits_10}/{k1}) → Precision@20: **{p20:.1f}%** ({hits_20}/{k2}).",
        "हिन्दी": "आउटरीच को शीर्ष 10 से शीर्ष 20 एनकाउंटर तक विस्तारित करने पर **{additional} अतिरिक्त** ऐतिहासिक प्रारंभिक पुनः भर्तियों की पहचान होती है ({hits_10} से {hits_20})। Precision@10: **{p10:.1f}%** ({hits_10}/{k1}) → Precision@20: **{p20:.1f}%** ({hits_20}/{k2})।",
        "ಕನ್ನಡ": "ಔಟ್‌ರೀಚ್ ಅನ್ನು ಅಗ್ರ 10 ರಿಂದ ಅಗ್ರ 20 ದಾಖಲಾತಿಗಳಿಗೆ ವಿಸ್ತರಿಸುವುದರಿಂದ **{additional} ಹೆಚ್ಚುವರಿ** ಐತಿಹಾಸಿಕ ಆರಂಭಿಕ ಮರುದಾಖಲಾತಿಗಳನ್ನು ಗುರುತಿಸುತ್ತದೆ ({hits_10} ರಿಂದ {hits_20})। Precision@10: **{p10:.1f}%** ({hits_10}/{k1}) → Precision@20: **{p20:.1f}%** ({hits_20}/{k2}).",
    },
    "retro_disclaimer": {
        "English": "⚠️ Retrospective evaluation on historical records. Precision@K is defined as historical early readmissions (<30d) divided by K. In live prospective clinical care, future readmissions are unknown at discharge.",
        "हिन्दी": "⚠️ ऐतिहासिक रिकॉर्ड पर पूर्वव्यापी मूल्यांकन। Precision@K को ऐतिहासिक प्रारंभिक पुनः भर्ती (<30 दिन) को K से विभाजित करके परिभाषित किया गया है। वास्तविक संभावित नैदानिक देखभाल में, डिस्चार्ज के समय भविष्य की पुनः भर्तियां अज्ञात होती हैं।",
        "ಕನ್ನಡ": "⚠️ ಐತಿಹಾಸಿಕ ದಾಖಲೆಗಳ ಮೇಲಿನ ಹಿಂದಿನ ಮೌಲ್ಯಮಾಪನ. Precision@K ಅನ್ನು ಐತಿಹಾಸಿಕ ಆರಂಭಿಕ ಮರುದಾಖಲಾತಿಗಳನ್ನು (<30 ದಿನ) K ನಿಂದ ಭಾಗಿಸಿ ವ್ಯಾಖ್ಯಾನಿಸಲಾಗಿದೆ. ಭವಿಷ್ಯದ ನೈಜ ವೈದ್ಯಕೀಯ ಆರೈಕೆಯಲ್ಲಿ, ಡಿಸ್ಚಾರ್ಜ್ ಸಮಯದಲ್ಲಿ ಭವಿಷ್ಯದ ಮರುದಾಖಲಾತಿಗಳು ತಿಳಿದಿರುವುದಿಲ್ಲ.",
    },


    # Tab 3: Model Diagnostics & Cohort Provenance
    "card_diagnostics_title": {
        "English": "Model Diagnostics & Cohort Provenance",
        "हिन्दी": "मॉडल डायग्नोस्टिक्स और कोहोर्ट उत्पत्ति",
        "ಕನ್ನಡ": "ಮಾದರಿ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ಗುಂಪಿನ ಮೂಲ",
    },
    "card_diagnostics_subtitle": {
        "English": "Evaluated on out-of-fold patient encounters using strict patient-grouped cross-validation.",
        "हिन्दी": "सख्त रोगी-समूहीकृत क्रॉस-सत्यापन का उपयोग करके आउट-ऑफ-फ़ोल्ड रोगी एनकाउंटर पर मूल्यांकन किया गया।",
        "ಕನ್ನಡ": "ಕಟ್ಟುನಿಟ್ಟಾದ ರೋಗಿ-ಗುಂಪು ಕ್ರಾಸ್-ವ್ಯಾಲಿಡೇಶನ್ ಬಳಸಿ ಮೌಲ್ಯಮಾಪನ ಮಾಡಲಾಗಿದೆ.",
    },
    "diagnostics_metrics_title": {
        "English": "##### 📊 Out-of-Fold Evaluation Metrics (Test Set)",
        "हिन्दी": "##### 📊 आउट-ऑफ-फ़ोल्ड मूल्यांकन मेट्रिक्स (टेस्ट सेट)",
        "ಕನ್ನಡ": "##### 📊 ಔಟ್-ಆಫ್-ಫೋಲ್ಡ್ ಮೌಲ್ಯಮಾಪನ ಮಾಪನಗಳು (ಪರೀಕ್ಷಾ ಗುಂಪು)",
    },
    "col_metric": {
        "English": "Metric",
        "हिन्दी": "मापदंड",
        "ಕನ್ನಡ": "ಮಾಪನ",
    },
    "col_value": {
        "English": "Value",
        "हिन्दी": "मान",
        "ಕನ್ನಡ": "ಮೌಲ್ಯ",
    },
    "metric_name_roc_auc": {
        "English": "ROC-AUC (Discrimination)",
        "हिन्दी": "ROC-AUC (भेदभाव क्षमता)",
        "ಕನ್ನಡ": "ROC-AUC (ವಿಭಜನಾ ಸಾಮರ್ಥ್ಯ)",
    },
    "metric_name_pr_auc": {
        "English": "PR-AUC (Average Precision)",
        "हिन्दी": "PR-AUC (औसत प्रिसिजन)",
        "ಕನ್ನಡ": "PR-AUC (ಸರಾಸರಿ ನಿಖರತೆ)",
    },
    "metric_desc_pr_auc": {
        "English": "Base prevalence: ~0.112",
        "हिन्दी": "मूल व्यापकता: ~0.112",
        "ಕನ್ನಡ": "ಮೂಲ ಪ್ರಮಾಣ: ~0.112",
    },
    "metric_name_recall": {
        "English": "Recall / Sensitivity",
        "हिन्दी": "रिकॉल / संवेदनशीलता",
        "ಕನ್ನಡ": "ಮರುಪಡೆಯುವಿಕೆ / ಸೂಕ್ಷ್ಮತೆ",
    },
    "metric_desc_recall": {
        "English": "of 30d readmissions detected",
        "हिन्दी": "30-दिन पुनः भर्ती का पता लगाया गया",
        "ಕನ್ನಡ": "30 ದಿನಗಳ ಮರುದಾಖಲಾತಿಗಳನ್ನು ಪತ್ತೆಹಚ್ಚಲಾಗಿದೆ",
    },
    "metric_name_precision": {
        "English": "Precision (PPV)",
        "हिन्दी": "प्रिसिजन (PPV)",
        "ಕನ್ನಡ": "ನಿಖರತೆ (PPV)",
    },
    "metric_name_f1": {
        "English": "F1-Score",
        "हिन्दी": "F1-स्कोर",
        "ಕನ್ನಡ": "F1-ಸ್ಕೋರ್",
    },
    "metric_name_specificity": {
        "English": "Specificity (TNR)",
        "हिन्दी": "विशिष्टता (TNR)",
        "ಕನ್ನಡ": "ವಿಶಿಷ್ಟತೆ (TNR)",
    },
    "metric_name_accuracy": {
        "English": "Accuracy (Reference Only)",
        "हिन्दी": "सटीकता / एक्यूरेसी (केवल संदर्भ)",
        "ಕನ್ನಡ": "ನಿಖರತೆ (ಕೇವಲ ಉಲ್ಲೇಖಕ್ಕಾಗಿ)",
    },
    "metric_desc_accuracy": {
        "English": "uninformative under 89% imbalance",
        "हिन्दी": "89% असंतुलन के तहत गैर-सूचनात्मक",
        "ಕನ್ನಡ": "89% ಅಸಮತೋಲನದಲ್ಲಿ ಅಪ್ರಸ್ತುತ",
    },
    "diagnostics_cm_title": {
        "English": "##### 🔲 Test Confusion Matrix",
        "हिन्दी": "##### 🔲 परीक्षण कन्फ्यूजन मैट्रिक्स",
        "ಕನ್ನಡ": "##### 🔲 ಪರೀಕ್ಷಾ ಕನ್‌ಫ್ಯೂಷನ್ ಮ್ಯಾಟ್ರಿಕ್ಸ್",
    },
    "cm_pred_no": {
        "English": "Predicted: No Readmit",
        "हिन्दी": "अनुमानित: पुनः भर्ती नहीं",
        "ಕನ್ನಡ": "ಅಂದಾಜು: ಮರುದಾಖಲಾತಿ ಇಲ್ಲ",
    },
    "cm_pred_yes": {
        "English": "Predicted: Readmission (<30d)",
        "हिन्दी": "अनुमानित: पुनः भर्ती (<30 दिन)",
        "ಕನ್ನಡ": "ಅಂದಾಜು: ಮರುದಾಖಲಾತಿ (<30 ದಿನ)",
    },
    "cm_act_no": {
        "English": "Actual: No Readmission",
        "हिन्दी": "वास्तविक: पुनः भर्ती नहीं",
        "ಕನ್ನಡ": "ನೈಜ: ಮರುದಾಖಲಾತಿ ಇಲ್ಲ",
    },
    "cm_act_yes": {
        "English": "Actual: Readmission (<30d)",
        "हिन्दी": "वास्तविक: पुनः भर्ती (<30 दिन)",
        "ಕನ್ನಡ": "ನೈಜ: ಮರುದಾಖಲಾತಿ (<30 ದಿನ)",
    },
    "diagnostics_safeguards_title": {
        "English": "##### 🛡️ Clinical Leakage Safeguards",
        "हिन्दी": "##### 🛡️ क्लिनिकल डेटा लीकेज सुरक्षा उपाय",
        "ಕನ್ನಡ": "##### 🛡️ ಕ್ಲಿನಿಕಲ್ ಡೇಟಾ ಸೋರಿಕೆ ತಡೆಗಟ್ಟುವ ಕ್ರಮಗಳು",
    },
    "diagnostics_safeguards_text": {
        "English": """
1. **Patient Leakage Prevention**: Encounters were split using `GroupShuffleSplit` on `patient_nbr`. All encounters for a patient reside strictly in either train or test, ensuring 0 patient overlap.
2. **Terminal Encounters Dropped**: 2,423 encounters where patients expired in the hospital or were discharged to hospice were excluded because readmission is clinically impossible for deceased patients.
3. **Timing Leakage Avoided**: `discharge_disposition_id` is excluded from the primary baseline features because discharge disposition is only finalized at discharge and reflects care interventions already prescribed.
4. **No Direct Identifiers**: `encounter_id` and `patient_nbr` are strictly excluded from model features and from the dashboard UI.
""",
        "हिन्दी": """
1. **रोगी डेटा लीकेज रोकथाम**: `patient_nbr` पर `GroupShuffleSplit` का उपयोग करके एनकाउंटर को विभाजित किया गया। किसी रोगी के सभी एनकाउंटर केवल ट्रेन या टेस्ट में रहते हैं, जिससे 0 रोगी ओवरलैप सुनिश्चित होता है।
2. **अंतिम एनकाउंटर हटाए गए**: 2,423 एनकाउंटर जहां रोगियों की मृत्यु हो गई या हॉस्पिस भेजा गया, उन्हें बाहर रखा गया क्योंकि मृत रोगियों के लिए पुनः भर्ती असंभव है।
3. **समय लीकेज से बचाव**: `discharge_disposition_id` को प्राथमिक बेसलाइन सुविधाओं से बाहर रखा गया है क्योंकि डिस्चार्ज स्थिति केवल डिस्चार्ज के समय अंतिम होती है।
4. **कोई प्रत्यक्ष पहचानकर्ता नहीं**: `encounter_id` और `patient_nbr` को मॉडल सुविधाओं और डैशबोर्ड यूआई से पूरी तरह बाहर रखा गया है।
""",
        "ಕನ್ನಡ": """
1. **ರೋಗಿ ಡೇಟಾ ಸೋರಿಕೆ ತಡೆಗಟ್ಟುವಿಕೆ**: `patient_nbr` ಆಧಾರದ ಮೇಲೆ `GroupShuffleSplit` ಬಳಸಿ ಡೇಟಾವನ್ನು ವಿಭಜಿಸಲಾಗಿದೆ. ಒಬ್ಬ ರೋಗಿಯ ಎಲ್ಲಾ ದಾಖಲಾತಿಗಳು ಕೇವಲ ಟ್ರೈನ್ ಅಥವಾ ಟೆಸ್ಟ್‌ನಲ್ಲಿರುತ್ತವೆ, ಇದರಿಂದ 0 ರೋಗಿ ಓವರ್‌ಲ್ಯಾಪ್ ಖಚಿತವಾಗುತ್ತದೆ.
2. **ಅಂತ್ಯದ ದಾಖಲಾತಿಗಳನ್ನು ಕೈಬಿಡಲಾಗಿದೆ**: ಆಸ್ಪತ್ರೆಯಲ್ಲಿ ಮೃತಪಟ್ಟ ಅಥವಾ ಹಾಸ್ಪೈಸ್‌ಗೆ ಕಳುಹಿಸಲಾದ 2,423 ದಾಖಲಾತಿಗಳನ್ನು ಹೊರಗಿಡಲಾಗಿದೆ ಏಕೆಂದರೆ ಮೃತ ರೋಗಿಗಳಿಗೆ ಮರುದಾಖಲಾತಿ ಅಸಾಧ್ಯ.
3. **ಸಮಯದ ಸೋರಿಕೆ ತಡೆಗಟ್ಟುವಿಕೆ**: `discharge_disposition_id` ಅನ್ನು ಮುಂಚಿತವಾಗಿಯೇ ಹೊರಗಿಡಲಾಗಿದೆ ಏಕೆಂದರೆ ಇದು ಡಿಸ್ಚಾರ್ಜ್ ಸಮಯದಲ್ಲಿ ಮಾತ್ರ ಅಂತಿಮಗೊಳ್ಳುತ್ತದೆ.
4. **ಯಾವುದೇ ನೇರ ಗುರುತುಗಳಿಲ್ಲ**: `encounter_id` ಮತ್ತು `patient_nbr` ಅನ್ನು ಮಾಡೆಲ್ ವೈಶಿಷ್ಟ್ಯಗಳು ಮತ್ತು ಡ್ಯಾಶ್‌ಬೋರ್ಡ್‌ನಿಂದ ಸಂಪೂರ್ಣವಾಗಿ ಹೊರಗಿಡಲಾಗಿದೆ.
""",
    },
    "diagnostics_limitations_title": {
        "English": "##### ⚠️ Methodological Limitations",
        "हिन्दी": "##### ⚠️ पद्धतिगत सीमाएं",
        "ಕನ್ನಡ": "##### ⚠️ ಪದ್ಧತಿಯ ಮಿತಿಗಳು",
    },
    "diagnostics_limitations_text": {
        "English": """
- **Tabular EHR Constraints**: Historical billing dataset lacks continuous physiological vitals, social determinants of health (SDOH), and post-discharge outpatient adherence.
- **Moderate Discrimination**: An ROC-AUC of ~0.64 is standard for historical single-encounter EHR data; risk prioritization must be used in a tiered triage capacity rather than hard binary decision-making.
- **Correlation vs. Causation**: Feature contributions reflect observational statistical associations, not causal therapeutic targets.
""",
        "हिन्दी": """
- **सारणीबद्ध EHR सीमाएं**: ऐतिहासिक बिलिंग डेटासेट में निरंतर शारीरिक महत्वपूर्ण लक्षण (वाइटल्स), स्वास्थ्य के सामाजिक निर्धारक (SDOH), और डिस्चार्ज के बाद बाह्यरोगी अनुपालन का अभाव है।
- **मध्यम भेदभाव क्षमता**: ऐतिहासिक एकल-एनकाउंटर EHR डेटा के लिए ~0.64 का ROC-AUC मानक है; जोखिम प्राथमिकता का उपयोग कठोर द्विआधारी निर्णय के बजाय स्तरीय प्राथमिकता क्षमता में किया जाना चाहिए।
- **सहसंबंध बनाम कार्य-कारण**: फीचर योगदान केवल सांख्यिकीय संबंध दर्शाते हैं, प्रत्यक्ष चिकित्सीय कारण नहीं।
""",
        "ಕನ್ನಡ": """
- **ಇಎಚ್‌ಆರ್ ಮಿತಿಗಳು**: ಐತಿಹಾಸಿಕ ಬಿಲ್ಲಿಂಗ್ ಡೇಟಾಸೆಟ್‌ನಲ್ಲಿ ನಿರಂತರ ಶಾರೀರಿಕ ಲಕ್ಷಣಗಳು (ವೈಟಲ್ಸ್), ಆರೋಗ್ಯದ ಸಾಮಾಜಿಕ ಅಂಶಗಳು (SDOH) ಮತ್ತು ಡಿಸ್ಚಾರ್ಜ್ ನಂತರದ ಹೊರರೋಗಿ ಪಾಲನೆಯ ವಿವರಗಳಿಲ್ಲ.
- **ಮಧ್ಯಮ ಮಟ್ಟದ ಸಾಮರ್ಥ್ಯ**: ಐತಿಹಾಸಿಕ ಡೇಟಾಗೆ ~0.64 ROC-AUC ಪ್ರಮಾಣಿತವಾಗಿದೆ; ಅಪಾಯದ ಆದ್ಯತೆಯನ್ನು ಹಂತವಾರು ವಿಂಗಡಣೆಗೆ ಮಾತ್ರ ಬಳಸಬೇಕು, ಕಡ್ಡಾಯ ನಿರ್ಧಾರಗಳಿಗೆ ಅಲ್ಲ.
- **ಸಂಬಂಧ ಮತ್ತು ಕಾರಣ**: ಅಂಶಗಳ ಕೊಡುಗೆಯು ಕೇವಲ ಸಂಖ್ಯಾಶಾಸ್ತ್ರೀಯ ಸಂಬಂಧವನ್ನು ಪ್ರತಿಬಿಂಬಿಸುತ್ತದೆ, ನೇರ ವೈದ್ಯಕೀಯ ಕಾರಣವಲ್ಲ.
""",
    },

    # Errors & System Messages
    "err_model_not_found": {
        "English": (
            "⚠️ Trained model artifact not found!\n\n"
            "Please ensure `models/saved/baseline_logistic_regression.joblib` exists. "
            "You can generate it by running: `python src/models/train_model.py`."
        ),
        "हिन्दी": (
            "⚠️ प्रशिक्षित मॉडल आर्टिफ़ैक्ट नहीं मिला!\n\n"
            "कृपया सुनिश्चित करें कि `models/saved/baseline_logistic_regression.joblib` मौजूद है। "
            "आप इसे चलाकर उत्पन्न कर सकते हैं: `python src/models/train_model.py`।"
        ),
        "ಕನ್ನಡ": (
            "⚠️ ತರಬೇತಿ ಪಡೆದ ಮಾದರಿ ಕಡತ ಕಂಡುಬಂದಿಲ್ಲ!\n\n"
            "ದಯವಿಟ್ಟು `models/saved/baseline_logistic_regression.joblib` ಅಸ್ತಿತ್ವದಲ್ಲಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ. "
            "ನೀವು ಇದನ್ನು ಚಲಾಯಿಸಿ ರಚಿಸಬಹುದು: `python src/models/train_model.py`."
        ),
    },

    # Tab 4: New Patient Prediction Feature
    "tab_predict_title": {
        "English": "➕ New Patient Prediction",
        "हिन्दी": "➕ नया रोगी जोखिम पूर्वानुमान",
        "ಕನ್ನಡ": "➕ ಹೊಸ ರೋಗಿಯ ಅಪಾಯದ ಮುನ್ಸೂಚನೆ",
    },
    "np_header_title": {
        "English": "New Patient Encounter Prediction",
        "हिन्दी": "नया रोगी एनकाउंटर जोखिम पूर्वानुमान",
        "ಕನ್ನಡ": "ಹೊಸ ರೋಗಿಯ ದಾಖಲಾತಿ ಅಪಾಯದ ಮುನ್ಸೂಚನೆ",
    },
    "np_header_subtitle": {
        "English": "Interactive clinical decision-support calculator for estimating 30-day readmission risk on individual encounters",
        "हिन्दी": "व्यक्तिगत एनकाउंटर पर 30-दिवसीय पुनः भर्ती जोखिम का अनुमान लगाने के लिए इंटरैक्टिव नैदानिक निर्णय-समर्थन कैलकुलेटर",
        "ಕನ್ನಡ": "ವೈಯಕ್ತಿಕ ದಾಖಲಾತಿಗಳಲ್ಲಿ 30 ದಿನಗಳ ಮರುದಾಖಲಾತಿ ಅಪಾಯವನ್ನು ಅಂದಾಜಿಸಲು ಸಂವಾದಾತ್ಮಕ ಕ್ಲಿನಿಕಲ್ ನಿರ್ಧಾರ-ಬೆಂಬಲ ಕ್ಯಾಲ್ಕುಲೇಟರ್",
    },
    "np_badge_prototype": {
        "English": "DECISION SUPPORT PROTOTYPE",
        "हिन्दी": "निर्णय समर्थन प्रोटोटाइप",
        "ಕನ್ನಡ": "ನಿರ್ಧಾರ ಬೆಂಬಲ ಮಾದರಿ",
    },
    "np_disclaimer_title": {
        "English": "Clinical Prototype & Fictional Data Notice",
        "हिन्दी": "नैदानिक प्रोटोटाइप और काल्पनिक डेटा सूचना",
        "ಕನ್ನಡ": "ಕ್ಲಿನಿಕಲ್ ಮಾದರಿ ಮತ್ತು ಕಾಲ್ಪನಿಕ ಡೇಟಾ ಸೂಚನೆ",
    },
    "np_disclaimer_text": {
        "English": "All pre-configured profiles are fictional scenarios designed for workflow feasibility demonstration. Model predictions are statistical research estimates from the baseline model and do not constitute clinical diagnoses or medical advice.",
        "हिन्दी": "सभी पूर्व-कॉन्फ़िगर की गई प्रोफ़ाइल वर्कफ़्लो व्यवहार्यता प्रदर्शन के लिए डिज़ाइन किए गए काल्पनिक परिदृश्य हैं। मॉडल पूर्वानुमान बेसलाइन मॉडल से सांख्यिकीय शोध अनुमान हैं और नैदानिक निदान या चिकित्सा सलाह नहीं हैं।",
        "ಕನ್ನಡ": "ಎಲ್ಲಾ ಮೊದಲೇ ಸಂರಚಿಸಲಾದ ವಿವರಗಳು ಕಾರ್ಯಪ್ರವಾಹದ ಪ್ರದರ್ಶನಕ್ಕಾಗಿ ವಿನ್ಯಾಸಗೊಳಿಸಲಾದ ಕಾಲ್ಪನಿಕ ಸನ್ನಿವೇಶಗಳಾಗಿವೆ. ಮಾದರಿ ಮುನ್ಸೂಚನೆಗಳು ಸಂಖ್ಯಾಶಾಸ್ತ್ರೀಯ ಸಂಶೋಧನಾ ಅಂದಾಜುಗಳಾಗಿದ್ದು, ಕ್ಲಿನಿಕಲ್ ರೋಗನಿರ್ಣಯ ಅಥವಾ ವೈದ್ಯಕೀಯ ಸಲಹೆಯಲ್ಲ.",
    },
    "np_profile_select_title": {
        "English": "Load Fictional Scenario Profile",
        "हिन्दी": "काल्पनिक परिदृश्य प्रोफ़ाइल लोड करें",
        "ಕನ್ನಡ": "ಕಾಲ್ಪನಿಕ ಸನ್ನಿವೇಶದ ವಿವರವನ್ನು ಲೋಡ್ ಮಾಡಿ",
    },
    "np_profile_select_caption": {
        "English": "Select a pre-populated clinical case to test different utilization histories, missing documentation, or stay characteristics.",
        "हिन्दी": "विभिन्न उपयोग इतिहास, अनुपलब्ध दस्तावेज़, या अस्पताल ठहराव विशेषताओं का परीक्षण करने के लिए पूर्व-भरी नैदानिक केस चुनें।",
        "ಕನ್ನಡ": "ವಿವಿಧ ಬಳಕೆಯ ಇತಿಹಾಸ, ದಾಖಲೆಗಳ ಕೊರತೆ ಅಥವಾ ಆಸ್ಪತ್ರೆ ವಾಸ್ತವ್ಯದ ಲಕ್ಷಣಗಳನ್ನು ಪರೀಕ್ಷಿಸಲು ಮೊದಲೇ ಭರ್ತಿ ಮಾಡಿದ ಕ್ಲಿನಿಕಲ್ ವಿವರವನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
    },
    "np_profile_dropdown_label": {
        "English": "Sample Profile",
        "हिन्दी": "नमूना प्रोफ़ाइल",
        "ಕನ್ನಡ": "ಮಾದರಿ ವಿವರ",
    },
    "np_btn_load_profile": {
        "English": "Load Profile",
        "हिन्दी": "प्रोफ़ाइल लोड करें",
        "ಕನ್ನಡ": "ವಿವರ ಲೋಡ್ ಮಾಡಿ",
    },
    "np_sec_demographics": {
        "English": "Patient Demographics & Admission Context",
        "हिन्दी": "रोगी जनसांख्यिकी और दाखिला संदर्भ",
        "ಕನ್ನಡ": "ರೋಗಿಯ ಜನಸಂಖ್ಯಾಶಾಸ್ತ್ರ ಮತ್ತು ದಾಖಲಾತಿ ಸಂದರ್ಭ",
    },
    "np_sec_utilization": {
        "English": "Hospital Stay & Prior Utilization History",
        "हिन्दी": "अस्पताल अवधि और पूर्व उपयोग इतिहास",
        "ಕನ್ನಡ": "ಆಸ್ಪತ್ರೆ ವಾಸ್ತವ್ಯ ಮತ್ತು ಹಿಂದಿನ ಬಳಕೆಯ ಇತಿಹಾಸ",
    },
    "np_sec_diagnoses": {
        "English": "Clinical Diagnostic Codes (ICD-9)",
        "हिन्दी": "नैदानिक डायग्नोस्टिक कोड (ICD-9)",
        "ಕನ್ನಡ": "ಕ್ಲಿನಿಕಲ್ ಡಯಾಗ್ನೋಸ್ಟಿಕ್ ಕೋಡ್‌ಗಳು (ICD-9)",
    },
    "np_sec_glycemic": {
        "English": "Glycemic Markers & Regimen Adjustments",
        "हिन्दी": "ग्लाइसेमिक मार्कर और दवा व्यवस्था समायोजन",
        "ಕನ್ನಡ": "ಗ್ಲೈಸೆಮಿಕ್ ಗುರುತುಗಳು ಮತ್ತು ಔಷಧಿ ಹೊಂದಾಣಿಕೆಗಳು",
    },
    "np_sec_medications": {
        "English": "Primary Antidiabetic Regimen",
        "हिन्दी": "प्राथमिक एंटीडायबिटिक दवाएं",
        "ಕನ್ನಡ": "ಪ್ರಾಥಮಿಕ ಮಧುಮೇಹ ವಿರೋಧಿ ಔಷಧಿಗಳು",
    },
    "np_more_meds_expander": {
        "English": "Additional Specialized Antidiabetic Agents (14 meds)",
        "हिन्दी": "अतिरिक्त विशिष्ट एंटीडायबिटिक दवाएं (14 दवाएं)",
        "ಕನ್ನಡ": "ಹೆಚ್ಚುವರಿ ವಿಶೇಷ ಮಧುಮೇಹ ವಿರೋಧಿ ಔಷಧಿಗಳು (14 ಔಷಧಿಗಳು)",
    },
    "np_btn_predict": {
        "English": "Calculate Readmission Risk",
        "हिन्दी": "पुनः भर्ती जोखिम की गणना करें",
        "ಕನ್ನಡ": "ಮರುದಾಖಲಾತಿ ಅಪಾಯವನ್ನು ಲೆಕ್ಕಹಾಕಿ",
    },
    "np_validation_error": {
        "English": "Form validation failed. Please check your inputs and try again.",
        "हिन्दी": "फ़ॉर्म सत्यापन विफल रहा। कृपया अपने इनपुट की जाँच करें और पुनः प्रयास करें।",
        "ಕನ್ನಡ": "ಫಾರ್ಮ್ ಮೌಲ್ಯಮಾಪನ ವಿಫಲವಾಗಿದೆ. ದಯವಿಟ್ಟು ನಿಮ್ಮ ನಮೂದುಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ.",
    },
    "np_results_title": {
        "English": "Prediction & Attribution Results",
        "हिन्दी": "पूर्वानुमान और विशेषता परिणाम",
        "ಕನ್ನಡ": "ಮುನ್ಸೂಚನೆ ಮತ್ತು ಕೊಡುಗೆ ಫಲಿತಾಂಶಗಳು",
    },
    "np_results_subtitle": {
        "English": "Individualized risk score estimate and linear feature contributions from fitted baseline model",
        "हिन्दी": "फिट किए गए बेसलाइन मॉडल से व्यक्तिगत जोखिम स्कोर अनुमान और रैखिक विशेषता योगदान",
        "ಕನ್ನಡ": "ತರಬೇತಿ ಪಡೆದ ಮಾದರಿಯಿಂದ ವೈಯಕ್ತಿಕ ಅಪಾಯದ ಸ್ಕೋರ್ ಅಂದಾಜು ಮತ್ತು ರೇಖೀಯ ಕೊಡುಗೆಗಳು",
    },
    "np_margin_label": {
        "English": "Decision Boundary Proximity",
        "हिन्दी": "निर्णय सीमा निकटता",
        "ಕನ್ನಡ": "ನಿರ್ಧಾರದ ಗಡಿಯ ಸಾಮೀಪ್ಯ",
    },
    "np_scenario_brief_label": {
        "English": "Scenario Brief:",
        "हिन्दी": "परिदृश्य संक्षेप:",
        "ಕನ್ನಡ": "ಸನ್ನಿವೇಶದ ಸಾರಾಂಶ:",
    },
    # Fictional Sample Profiles Metadata (English, Hindi, Kannada)
    "prof_name_high_risk_geriatric": {
        "English": "High-Risk Geriatric (Frequent Admissions & Insulin Instability)",
        "हिन्दी": "उच्च जोखिम वाले वृद्ध रोगी (बार-बार दाखिले और इंसुलिन अस्थिरता)",
        "ಕನ್ನಡ": "ಹೆಚ್ಚಿನ ಅಪಾಯದ ವೃದ್ಧ ರೋಗಿ (ಪದೇ ಪದೇ ದಾಖಲಾತಿಗಳು ಮತ್ತು ಇನ್ಸುಲಿನ್ ಅಸ್ಥಿರತೆ)",
    },
    "prof_badge_high_risk_geriatric": {
        "English": "🚨 Higher Risk / Frequent Inpatient",
        "हिन्दी": "🚨 उच्च जोखिम / बार-बार अस्पताल भर्ती",
        "ಕನ್ನಡ": "🚨 ಹೆಚ್ಚಿನ ಅಪಾಯ / ಪದೇ ಪದೇ ಆಸ್ಪತ್ರೆ ದಾಖಲಾತಿ",
    },
    "prof_desc_high_risk_geriatric": {
        "English": "Fictional 82-year-old patient admitted through the ER with acute decompensated Heart Failure, 3 prior hospitalizations in the past year, marked hyperglycemia (A1C > 8, Glucose > 300), and upward insulin titration during the 8-day admission.",
        "हिन्दी": "काल्पनिक 82 वर्षीय रोगी को तीव्र हार्ट फेल्योर के साथ आपातकालीन कक्ष के माध्यम से भर्ती कराया गया, पिछले वर्ष में 3 पूर्व अस्पताल दाखिले, अत्यधिक हाइपरग्लाइसेमिया (A1C > 8, ग्लूकोज > 300), और 8-दिवसीय ठहराव के दौरान इंसुलिन में वृद्धि।",
        "ಕನ್ನಡ": "ತೀವ್ರ ಹೃದಯ ವೈಫಲ್ಯದೊಂದಿಗೆ ತುರ್ತು ವಿಭಾಗದ ಮೂಲಕ ದಾಖಲಾದ ಕಾಲ್ಪನಿಕ 82 ವರ್ಷದ ರೋಗಿ, ಕಳೆದ ವರ್ಷದಲ್ಲಿ 3 ಹಿಂದಿನ ಆಸ್ಪತ್ರೆ ದಾಖಲಾತಿಗಳು, ತೀವ್ರ ಹೈಪರ್‌ಗ್ಲೈಸೆಮಿಯಾ (A1C > 8, ಗ್ಲೂಕೋಸ್ > 300), ಮತ್ತು 8 ದಿನಗಳ ವಾಸ್ತವ್ಯದಲ್ಲಿ ಇನ್ಸುಲಿನ್ ಹೆಚ್ಚಳ.",
    },
    "prof_name_moderate_risk_surgical": {
        "English": "Moderate-Risk Post-Surgical (Regimen Adjusted)",
        "हिन्दी": "मध्यम जोखिम वाले सर्जरी उपरांत रोगी (दवा व्यवस्था समायोजित)",
        "ಕನ್ನಡ": "ಮಧ್ಯಮ ಅಪಾಯದ ಶಸ್ತ್ರಚಿಕಿತ್ಸಾ ನಂತರದ ರೋಗಿ (ಔಷಧಿ ಹೊಂದಾಣಿಕೆ ಮಾಡಲಾಗಿದೆ)",
    },
    "prof_badge_moderate_risk_surgical": {
        "English": "⚠️ Moderate Risk / Regimen Adjustment",
        "हिन्दी": "⚠️ मध्यम जोखिम / दवा समायोजन",
        "ಕನ್ನಡ": "⚠️ ಮಧ್ಯಮ ಅಪಾಯ / ಔಷಧಿ ಹೊಂದಾಣಿಕೆ",
    },
    "prof_desc_moderate_risk_surgical": {
        "English": "Fictional 56-year-old patient admitted urgently for acute diverticular/GI condition, stayed 4 days with moderate lab testing, diabetic regimen adjusted with downward metformin titration, and 1 prior hospital stay in the past year.",
        "हिन्दी": "काल्पनिक 56 वर्षीय रोगी को तीव्र जठरांत्र (GI) स्थिति के लिए तत्काल भर्ती कराया गया, मध्यम प्रयोगशाला परीक्षणों के साथ 4 दिन ठहराव, मेटफॉर्मिन खुराक में कमी के साथ मधुमेह दवा व्यवस्था समायोजित, और पिछले वर्ष में 1 पूर्व अस्पताल दाखिला।",
        "ಕನ್ನಡ": "ತೀವ್ರ ಜಠರಗರುಳಿನ (GI) ಸಮಸ್ಯೆಗೆ ತಕ್ಷಣ ದಾಖಲಾದ ಕಾಲ್ಪನಿಕ 56 ವರ್ಷದ ರೋಗಿ, ಮಧ್ಯಮ ಮಟ್ಟದ ಲ್ಯಾಬ್ ಪರೀಕ್ಷೆಗಳೊಂದಿಗೆ 4 ದಿನ ವಾಸ್ತವ್ಯ, ಮೆಟ್‌ಫಾರ್ಮಿನ್ ಕಡಿಮೆ ಮಾಡುವ ಮೂಲಕ ಮಧುಮೇಹ ಔಷಧಿ ಹೊಂದಾಣಿಕೆ, ಮತ್ತು ಕಳೆದ ವರ್ಷದಲ್ಲಿ 1 ಹಿಂದಿನ ಆಸ್ಪತ್ರೆ ದಾಖಲಾತಿ.",
    },
    "prof_name_lower_risk_young_adult": {
        "English": "Lower-Risk Young Adult (First Admission & Stable Oral Regimen)",
        "हिन्दी": "निम्न जोखिम वाले युवा वयस्क (पहला दाखिला और स्थिर मौखिक दवा)",
        "ಕನ್ನಡ": "ಕಡಿಮೆ ಅಪಾಯದ ಯುವ ವಯಸ್ಕ (ಮೊದಲ ದಾಖಲಾತಿ ಮತ್ತು ಸ್ಥಿರ ಮೌಖಿಕ ಔಷಧಿ)",
    },
    "prof_badge_lower_risk_young_adult": {
        "English": "✅ Lower Risk / First Admission",
        "हिन्दी": "✅ निम्न जोखिम / पहला दाखिला",
        "ಕನ್ನಡ": "✅ ಕಡಿಮೆ ಅಪಾಯ / ಮೊದಲ ದಾಖಲಾತಿ",
    },
    "prof_desc_lower_risk_young_adult": {
        "English": "Fictional 34-year-old patient admitted electively for orthopedic arthroscopy with zero prior acute hospitalizations or ER visits, normal glycemic lab markers, and stable single-agent metformin therapy.",
        "हिन्दी": "काल्पनिक 34 वर्षीय रोगी को आर्थोपेडिक आर्थ्रोस्कोपी के लिए ऐच्छिक रूप से भर्ती कराया गया, शून्य पूर्व तीव्र अस्पताल दाखिले या ER दौरे, सामान्य ग्लाइसेमिक लैब मार्कर, और स्थिर एकल-एजेंट मेटफॉर्मिन थेरेपी।",
        "ಕನ್ನಡ": "ಆರ್ಥೋಪೆಡಿಕ್ ಆರ್ಥ್ರೋಸ್ಕೋಪಿಗಾಗಿ ಯೋಜಿತವಾಗಿ ದಾಖಲಾದ ಕಾಲ್ಪನಿಕ 34 ವರ್ಷದ ರೋಗಿ, ಯಾವುದೇ ಹಿಂದಿನ ಆಸ್ಪತ್ರೆ ದಾಖಲಾತಿ ಅಥವಾ ತುರ್ತು ಭೇಟಿಗಳಿಲ್ಲ, ಸಾಮಾನ್ಯ ಗ್ಲೈಸೆಮಿಕ್ ಲ್ಯಾಬ್ ಮೌಲ್ಯಗಳು, ಮತ್ತು ಸ್ಥಿರ ಏಕ-ಔಷಧಿ ಮೆಟ್‌ಫಾರ್ಮಿನ್ ಚಿಕಿತ್ಸೆ.",
    },
    "prof_name_missing_data_edge_case": {
        "English": "Missing Diagnostic Code & Unperformed Lab Tests (Documentation Edge Case)",
        "हिन्दी": "अनुपलब्ध डायग्नोस्टिक कोड और अप्रदर्शित लैब टेस्ट (दस्तावेज़ीकरण एज केस)",
        "ಕನ್ನಡ": "ದಾಖಲಾಗದ ರೋಗನಿರ್ಣಯ ಕೋಡ್ ಮತ್ತು ಮಾಡದ ಲ್ಯಾಬ್ ಪರೀಕ್ಷೆಗಳು (ದಾಖಲೆಗಳ ಕೊರತೆಯ ಪ್ರಕರಣ)",
    },
    "prof_badge_missing_data_edge_case": {
        "English": "⚠️ Safety Edge Case / Incomplete Data",
        "हिन्दी": "⚠️ सुरक्षा एज केस / अपूर्ण डेटा",
        "ಕನ್ನಡ": "⚠️ ಸುರಕ್ಷತಾ ಪ್ರಕರಣ / ಅಪೂರ್ಣ ಡೇಟಾ",
    },
    "prof_desc_missing_data_edge_case": {
        "English": "Fictional 64-year-old male with unrecorded primary diagnosis billing code ('?'), unperformed HbA1c and fasting glucose tests, and unknown race. Verifies graceful handling of missing clinical records without crashing.",
        "हिन्दी": "काल्पनिक 64 वर्षीय पुरुष रोगी जिसका प्राथमिक निदान बिलिंग कोड दर्ज नहीं है ('?'), HbA1c और फास्टिंग ग्लूकोज परीक्षण नहीं किए गए, और अज्ञात नस्ल। बिना क्रैश हुए लापता नैदानिक रिकॉर्ड्स के सुरक्षित प्रबंधन की पुष्टि करता है।",
        "ಕನ್ನಡ": "ದಾಖಲಾಗದ ಪ್ರಾಥಮಿಕ ರೋಗನಿರ್ಣಯ ಬಿಲ್ಲಿಂಗ್ ಕೋಡ್ ('?'), ಮಾಡದ HbA1c ಮತ್ತು ಉಪವಾಸದ ಗ್ಲೂಕೋಸ್ ಪರೀಕ್ಷೆಗಳು, ಮತ್ತು ಅಜ್ಞಾತ ಜನಾಂಗ ಹೊಂದಿರುವ ಕಾಲ್ಪನಿಕ 64 ವರ್ಷದ ಪುರುಷ ರೋಗಿ. ಸಿಸ್ಟಮ್ ಕ್ರ್ಯಾಶ್ ಆಗದೆ ಅಪೂರ್ಣ ದಾಖಲೆಗಳನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ನಿರ್ವಹಿಸುವುದನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ.",
    },
    "prof_name_extended_stay_polypharmacy": {
        "English": "Extended Stay (13 Days) with Extreme Polypharmacy (42 Meds)",
        "हिन्दी": "विस्तारित ठहराव (13 दिन) और अत्यधिक पॉलीफार्मेसी (42 दवाएं)",
        "ಕನ್ನಡ": "ದೀರ್ಘಾವಧಿ ವಾಸ್ತವ್ಯ (13 ದಿನಗಳು) ಮತ್ತು ಅತಿಯಾದ ಪಾಲಿಫಾರ್ಮಸಿ (42 ಔಷಧಿಗಳು)",
    },
    "prof_badge_extended_stay_polypharmacy": {
        "English": "🚨 Higher Risk / Polypharmacy & Stay",
        "हिन्दी": "🚨 उच्च जोखिम / पॉलीफार्मेसी और ठहराव",
        "ಕನ್ನಡ": "🚨 ಹೆಚ್ಚಿನ ಅಪಾಯ / ಪಾಲಿಫಾರ್ಮಸಿ ಮತ್ತು ವಾಸ್ತವ್ಯ",
    },
    "prof_desc_extended_stay_polypharmacy": {
        "English": "Fictional 85-year-old patient transferred from another hospital with complex respiratory infection, prolonged hospital stay of 13 days (near 14-day truncation limit), and 42 active medications triggering extreme polypharmacy warnings.",
        "हिन्दी": "काल्पनिक 85 वर्षीय रोगी को जटिल श्वसन संक्रमण के साथ दूसरे अस्पताल से स्थानांतरित किया गया, 13 दिनों का लंबा अस्पताल ठहराव (14-दिवसीय सीमा के निकट), और अत्यधिक पॉलीफार्मेसी चेतावनियों को ट्रिगर करने वाली 42 सक्रिय दवाएं।",
        "ಕನ್ನಡ": "ಸಂಕೀರ್ಣ ಉಸಿರಾಟದ ಸೋಂಕಿನೊಂದಿಗೆ ಮತ್ತೊಂದು ಆಸ್ಪತ್ರೆಯಿಂದ ವರ್ಗಾವಣೆಯಾದ ಕಾಲ್ಪನಿಕ 85 ವರ್ಷದ ರೋಗಿ, 13 ದಿನಗಳ ದೀರ್ಘಾವಧಿ ವಾಸ್ತವ್ಯ (14 ದಿನಗಳ ಮಿತಿಯ ಹತ್ತಿರ), ಮತ್ತು ತೀವ್ರ ಪಾಲಿಫಾರ್ಮಸಿ ಎಚ್ಚರಿಕೆಗಳನ್ನು ಪ್ರಚೋದಿಸುವ 42 ಸಕ್ರಿಯ ಔಷಧಿಗಳು.",
    },
    "prof_name_frequent_er_respiratory": {
        "English": "Frequent ER Utilization with Chronic COPD (Non-Insulin Managed)",
        "हिन्दी": "क्रोनिक सीओपीडी के साथ बार-बार ER उपयोग (गैर-इंसुलिन प्रबंधित)",
        "ಕನ್ನಡ": "ದೀರ್ಘಕಾಲದ COPD ಯೊಂದಿಗೆ ಆಗಾಗ್ಗೆ ತುರ್ತು ವಿಭಾಗ ಬಳಕೆ (ಇನ್ಸುಲಿನ್ ರಹಿತ ನಿರ್ವಹಣೆ)",
    },
    "prof_badge_frequent_er_respiratory": {
        "English": "⚠️ Moderate to High / ER Utilizer",
        "हिन्दी": "⚠️ मध्यम से उच्च / ER उपयोगकर्ता",
        "ಕನ್ನಡ": "⚠️ ಮಧ್ಯಮದಿಂದ ಹೆಚ್ಚಿನ / ತುರ್ತು ಬಳಕೆದಾರ",
    },
    "prof_desc_frequent_er_respiratory": {
        "English": "Fictional 74-year-old patient presenting via ER with acute COPD exacerbation, 3 prior ER visits in the past year but 0 inpatient admissions, managed with oral sulfonylurea without insulin, with elevated A1C (> 8).",
        "हिन्दी": "काल्पनिक 74 वर्षीय रोगी जो तीव्र सीओपीडी स्थिति के साथ ER के माध्यम से आया, पिछले वर्ष में 3 पूर्व ER दौरे लेकिन 0 इनपेशेंट दाखिले, इंसुलिन के बिना मौखिक सल्फोनील्यूरिया के साथ प्रबंधित, और बढ़ा हुआ A1C (> 8)।",
        "ಕನ್ನಡ": "ತೀವ್ರ COPD ಉಲ್ಬಣದೊಂದಿಗೆ ತುರ್ತು ವಿಭಾಗದ ಮೂಲಕ ಬಂದ ಕಾಲ್ಪನಿಕ 74 ವರ್ಷದ ರೋಗಿ, ಕಳೆದ ವರ್ಷದಲ್ಲಿ 3 ಹಿಂದಿನ ತುರ್ತು ಭೇಟಿಗಳು ಆದರೆ 0 ಆಸ್ಪತ್ರೆ ದಾಖಲಾತಿಗಳು, ಇನ್ಸುಲಿನ್ ಇಲ್ಲದೆ ಮೌಖಿಕ ಸಲ್ಫೋನಿಲ್ಯೂರಿಯಾದೊಂದಿಗೆ ನಿರ್ವಹಿಸಲಾಗಿದೆ, ಮತ್ತು ಹೆಚ್ಚಿನ A1C (> 8).",
    },

    # Form Fields, Input Help & Labels
    "np_sec_diagnoses_caption": {
        "English": "Enter standard 3-digit ICD-9 codes (e.g. 428=Heart Failure, 250=Diabetes, 486=Pneumonia, 530=Digestive, ?=Missing).",
        "हिन्दी": "मानक 3-अंकीय ICD-9 कोड दर्ज करें (उदा. 428=हार्ट फेल्योर, 250=मधुमेह, 486=निमोनिया, 530=पाचन, ?=अनुपलब्ध)।",
        "ಕನ್ನಡ": "ಪ್ರಮಾಣಿತ 3-ಅಂಕಿಯ ICD-9 ಕೋಡ್‌ಗಳನ್ನು ನಮೂದಿಸಿ (ಉದಾ. 428=ಹೃದಯ ವೈಫಲ್ಯ, 250=ಮಧುಮೇಹ, 486=ನ್ಯುಮೋನಿಯಾ, 530=ಜೀರ್ಣಾಂಗ, ?=ದಾಖಲಾಗಿಲ್ಲ).",
    },
    "np_diag_1_label": {
        "English": "Primary ICD-9 (`diag_1`)",
        "हिन्दी": "प्राथमिक ICD-9 (`diag_1`)",
        "ಕನ್ನಡ": "ಪ್ರಾಥಮಿಕ ICD-9 (`diag_1`)",
    },
    "np_diag_2_label": {
        "English": "Secondary ICD-9 (`diag_2`)",
        "हिन्दी": "द्वितीयक ICD-9 (`diag_2`)",
        "ಕನ್ನಡ": "ದ್ವಿತೀಯಕ ICD-9 (`diag_2`)",
    },
    "np_diag_3_label": {
        "English": "Tertiary ICD-9 (`diag_3`)",
        "हिन्दी": "तृतीयक ICD-9 (`diag_3`)",
        "ಕನ್ನಡ": "ತೃತೀಯಕ ICD-9 (`diag_3`)",
    },
    "np_num_procedures": {
        "English": "Diagnostic Procedures (0-6)",
        "हिन्दी": "डायग्नोस्टिक प्रक्रियाएं (0-6)",
        "ಕನ್ನಡ": "ಡಯಾಗ್ನೋಸ್ಟಿಕ್ ಪ್ರಕ್ರಿಯೆಗಳು (0-6)",
    },
    "np_num_diagnoses": {
        "English": "Documented Diagnoses (1-16)",
        "हिन्दी": "दर्ज किए गए निदान (1-16)",
        "ಕನ್ನಡ": "ದಾಖಲಾದ ರೋಗನಿರ್ಣಯಗಳು (1-16)",
    },
    "np_med_ch_desc": {
        "English": "Ch - Medication Adjusted",
        "हिन्दी": "Ch - दवा व्यवस्था में बदलाव",
        "ಕನ್ನಡ": "Ch - ಔಷಧಿಯಲ್ಲಿ ಬದಲಾವಣೆ",
    },
    "np_med_no_desc": {
        "English": "No - No Dosage Change",
        "हिन्दी": "No - खुराक में कोई बदलाव नहीं",
        "ಕನ್ನಡ": "No - ಡೋಸ್‌ನಲ್ಲಿ ಯಾವುದೇ ಬದಲಾವಣೆ ಇಲ್ಲ",
    },

    # Admission Types
    "adm_type_1": {
        "English": "1 - Emergency",
        "हिन्दी": "1 - आपातकालीन (Emergency)",
        "ಕನ್ನಡ": "1 - ತುರ್ತು (Emergency)",
    },
    "adm_type_2": {
        "English": "2 - Urgent",
        "हिन्दी": "2 - तात्कालिक (Urgent)",
        "ಕನ್ನಡ": "2 - ತಕ್ಷಣದ (Urgent)",
    },
    "adm_type_3": {
        "English": "3 - Elective",
        "हिन्दी": "3 - ऐच्छिक (Elective)",
        "ಕನ್ನಡ": "3 - ಪೂರ್ವಯೋಜಿತ (Elective)",
    },
    "adm_type_4": {
        "English": "4 - Newborn",
        "हिन्दी": "4 - नवजात (Newborn)",
        "ಕನ್ನಡ": "4 - ನವಜಾತ ಶಿಶು (Newborn)",
    },
    "adm_type_5": {
        "English": "5 - Not Available",
        "हिन्दी": "5 - अनुपलब्ध (Not Available)",
        "ಕನ್ನಡ": "5 - ಲಭ್ಯವಿಲ್ಲ (Not Available)",
    },
    "adm_type_6": {
        "English": "6 - NULL / Unrecorded",
        "हिन्दी": "6 - दर्ज नहीं (NULL / Unrecorded)",
        "ಕನ್ನಡ": "6 - ದಾಖಲಾಗಿಲ್ಲ (NULL / Unrecorded)",
    },
    "adm_type_7": {
        "English": "7 - Trauma Center",
        "हिन्दी": "7 - ट्रॉमा सेंटर (Trauma Center)",
        "ಕನ್ನಡ": "7 - ಟ್ರಾಮಾ ಸೆಂಟರ್ (Trauma Center)",
    },
    "adm_type_8": {
        "English": "8 - Not Mapped",
        "हिन्दी": "8 - गैर-मैप किया गया (Not Mapped)",
        "ಕನ್ನಡ": "8 - ಮ್ಯಾಪ್ ಮಾಡಿಲ್ಲ (Not Mapped)",
    },

    # Admission Sources
    "adm_src_7": {
        "English": "7 - Emergency Room",
        "हिन्दी": "7 - आपातकालीन कक्ष (ER)",
        "ಕನ್ನಡ": "7 - ತುರ್ತು ವಿಭಾಗ (ER)",
    },
    "adm_src_1": {
        "English": "1 - Physician Referral",
        "हिन्दी": "1 - चिकित्सक रेफरल",
        "ಕನ್ನಡ": "1 - ವೈದ್ಯರ ಶಿಫಾರಸು",
    },
    "adm_src_2": {
        "English": "2 - Clinic Referral",
        "हिन्दी": "2 - क्लिनिक रेफरल",
        "ಕನ್ನಡ": "2 - ಕ್ಲಿನಿಕ್ ಶಿಫಾರಸು",
    },
    "adm_src_3": {
        "English": "3 - HMO Referral",
        "हिन्दी": "3 - HMO रेफरल",
        "ಕನ್ನಡ": "3 - HMO ಶಿಫಾರಸು",
    },
    "adm_src_4": {
        "English": "4 - Transfer from Hospital",
        "हिन्दी": "4 - अस्पताल से स्थानांतरण",
        "ಕನ್ನಡ": "4 - ಆಸ್ಪತ್ರೆಯಿಂದ ವರ್ಗಾವಣೆ",
    },
    "adm_src_5": {
        "English": "5 - Transfer from SNF",
        "हिन्दी": "5 - SNF से स्थानांतरण",
        "ಕನ್ನಡ": "5 - SNF ನಿಂದ ವರ್ಗಾವಣೆ",
    },
    "adm_src_6": {
        "English": "6 - Transfer from Other Facility",
        "हिन्दी": "6 - अन्य सुविधा से स्थानांतरण",
        "ಕನ್ನಡ": "6 - ಇತರ ಸೌಲಭ್ಯದಿಂದ ವರ್ಗಾವಣೆ",
    },
    "adm_src_10": {
        "English": "10 - Critical Access Hospital",
        "हिन्दी": "10 - क्रिटिकल एक्सेस अस्पताल",
        "ಕನ್ನಡ": "10 - ಕ್ರಿಟಿಕಲ್ ಆಕ್ಸೆಸ್ ಆಸ್ಪತ್ರೆ",
    },
    "adm_src_20": {
        "English": "20 - Not Mapped",
        "हिन्दी": "20 - गैर-मैप किया गया",
        "ಕನ್ನಡ": "20 - ಮ್ಯಾಪ್ ಮಾಡಿಲ್ಲ",
    },

    # Medication Options
    "med_opt_no": {
        "English": "No",
        "हिन्दी": "नहीं (No)",
        "ಕನ್ನಡ": "ಇಲ್ಲ (No)",
    },
    "med_opt_steady": {
        "English": "Steady",
        "हिन्दी": "स्थिर (Steady)",
        "ಕನ್ನಡ": "ಸ್ಥಿರ (Steady)",
    },
    "med_opt_up": {
        "English": "Up",
        "हिन्दी": "बढ़ा (Up)",
        "ಕನ್ನಡ": "ಹೆಚ್ಚು (Up)",
    },
    "med_opt_down": {
        "English": "Down",
        "हिन्दी": "घटा (Down)",
        "ಕನ್ನಡ": "ಕಡಿಮೆ (Down)",
    },

    # Result Labels & Advisories
    "np_raw_logit_prob": {
        "English": "Raw logit prob: {val:.4f}",
        "हिन्दी": "कच्ची लॉजिट संभावना: {val:.4f}",
        "ಕನ್ನಡ": "ಮೂಲ ಲಾಗಿಟ್ ಸಂಭವನೀಯತೆ: {val:.4f}",
    },
    "np_thresholds_label": {
        "English": "Thresholds: High ≥ {high:.2f} · Mod ≥ {mod:.2f}",
        "हिन्दी": "सीमाएं: उच्च ≥ {high:.2f} · मध्यम ≥ {mod:.2f}",
        "ಕನ್ನಡ": "ಮಿತಿಗಳು: ಹೆಚ್ಚಿನ ≥ {high:.2f} · ಮಧ್ಯಮ ≥ {mod:.2f}",
    },
    "np_doc_notice": {
        "English": "Documentation Notice",
        "हिन्दी": "दस्तावेज़ीकरण सूचना",
        "ಕನ್ನಡ": "ದಾಖಲೆಗಳ ಸೂಚನೆ",
    },
    "np_adv_missing_diag": {
        "English": "Primary diagnosis ICD-9 code is unrecorded. Categorized as 'Missing' per standard benchmark rules.",
        "हिन्दी": "प्राथमिक निदान ICD-9 कोड दर्ज नहीं है। मानक बेंचमार्क नियमों के अनुसार 'अनुपलब्ध' के रूप में वर्गीकृत।",
        "ಕನ್ನಡ": "ಪ್ರಾಥಮಿಕ ರೋಗನಿರ್ಣಯ ICD-9 ಕೋಡ್ ದಾಖಲಾಗಿಲ್ಲ. ಪ್ರಮಾಣಿತ ಮಾನದಂಡಗಳ ಪ್ರಕಾರ 'ದಾಖಲಾಗಿಲ್ಲ' ಎಂದು ವರ್ಗೀಕರಿಸಲಾಗಿದೆ.",
    },
    "np_adv_missing_a1c": {
        "English": "HbA1c laboratory assessment was not recorded during this encounter.",
        "हिन्दी": "इस एनकाउंटर के दौरान HbA1c प्रयोगशाला परीक्षण दर्ज नहीं किया गया था।",
        "ಕನ್ನಡ": "ಈ ದಾಖಲಾತಿಯ ಸಮಯದಲ್ಲಿ HbA1c ಪ್ರಯೋಗಾಲಯ ಪರೀಕ್ಷೆಯನ್ನು ದಾಖಲಿಸಲಾಗಿಲ್ಲ.",
    },
    "np_adv_missing_glu": {
        "English": "Fasting serum glucose test was not recorded during this encounter.",
        "हिन्दी": "इस एनकाउंटर के दौरान फास्टिंग सीरम ग्लूकोज परीक्षण दर्ज नहीं किया गया था।",
        "ಕನ್ನಡ": "ಈ ದಾಖಲಾತಿಯ ಸಮಯದಲ್ಲಿ ಉಪವಾಸದ ಸೀರಮ್ ಗ್ಲೂಕೋಸ್ ಪರೀಕ್ಷೆಯನ್ನು ದಾಖಲಿಸಲಾಗಿಲ್ಲ.",
    },
    "why_this_risk_score": {
        "English": "Why this risk score?",
        "हिन्दी": "यह जोखिम स्कोर क्यों?",
        "ಕನ್ನಡ": "ಈ ಅಪಾಯದ ಸ್ಕೋರ್ ಏಕೆ?",
    },
    "factors_pushing_higher": {
        "English": "Factors pushing the model's score higher",
        "हिन्दी": "मॉडल के स्कोर को बढ़ाने वाले कारक",
        "ಕನ್ನಡ": "ಮಾದರಿಯ ಸ್ಕೋರ್ ಅನ್ನು ಹೆಚ್ಚಿಸುವ ಅಂಶಗಳು",
    },
    "factors_pushing_lower": {
        "English": "Factors pushing the model's score lower",
        "हिन्दी": "मॉडल के स्कोर को घटाने वाले कारक",
        "ಕನ್ನಡ": "ಮಾದರಿಯ ಸ್ಕೋರ್ ಅನ್ನು ಕಡಿಮೆ ಮಾಡುವ ಅಂಶಗಳು",
    },
    "attribution_unavailable": {
        "English": "Patient-specific feature attribution is currently unavailable for this calculation. The mathematical log-odds decomposition could not be mapped to the model's input features.",
        "हिन्दी": "इस गणना के लिए रोगी-विशिष्ट विशेषता स्पष्टीकरण वर्तमान में अनुपलब्ध है।",
        "ಕನ್ನಡ": "ಈ ಲೆಕ್ಕಾಚಾರಕ್ಕೆ ರೋಗಿ-ನಿರ್ದಿಷ್ಟ ವೈಶಿಷ್ಟ್ಯದ ಕೊಡುಗೆ ಪ್ರಸ್ತುತ ಲಭ್ಯವಿಲ್ಲ.",
    },
}

# Tiers Translation
TIER_TRANSLATIONS = {
    "Higher Score": {
        "English": "Higher Score",
        "हिन्दी": "उच्च स्कोर",
        "ಕನ್ನಡ": "ಹೆಚ್ಚಿನ ಸ್ಕೋರ್",
    },
    "Moderate Score": {
        "English": "Moderate Score",
        "हिन्दी": "मध्यम स्कोर",
        "ಕನ್ನಡ": "ಮಧ್ಯಮ ಸ್ಕೋರ್",
    },
    "Lower Score": {
        "English": "Lower Score",
        "हिन्दी": "निम्न स्कोर",
        "ಕನ್ನಡ": "ಕಡಿಮೆ ಸ್ಕೋರ್",
    },
}

# Feature Manifest Translations (for mathematical attribution and domain charts)
CLINICAL_DOMAINS_TRANSLATION = {
    # Exact categories used in compute_domain_importance
    "Age & Demographics": {
        "English": "Age & Demographics",
        "हिन्दी": "आयु और जनसांख्यिकी",
        "ಕನ್ನಡ": "ವಯಸ್ಸು ಮತ್ತು ಜನಸಂಖ್ಯಾಶಾಸ್ತ್ರ",
    },
    "Medication Adjustments": {
        "English": "Medication Adjustments",
        "हिन्दी": "दवा समायोजन",
        "ಕನ್ನಡ": "ಔಷಧಿ ಹೊಂದಾಣಿಕೆಗಳು",
    },
    "Clinical Comorbidities": {
        "English": "Clinical Comorbidities",
        "हिन्दी": "नैदानिक सह-रुग्णताएं",
        "ಕನ್ನಡ": "ಕ್ಲಿನಿಕಲ್ ಸಹ-ಕಾಯಿಲೆಗಳು",
    },
    "Past Utilization (Inpatient/ER)": {
        "English": "Past Utilization (Inpatient/ER)",
        "हिन्दी": "पूर्व अस्पताल उपयोग (भर्ती/आपातकालीन)",
        "ಕನ್ನಡ": "ಹಿಂದಿನ ಆಸ್ಪತ್ರೆ ಬಳಕೆ (ದಾಖಲಾತಿ/ತುರ್ತು)",
    },
    "Diagnostic Testing Volume": {
        "English": "Diagnostic Testing Volume",
        "हिन्दी": "नैदानिक परीक्षण मात्रा",
        "ಕನ್ನಡ": "ರೋಗನಿರ್ಣಯ ಪರೀಕ್ಷೆಗಳ ಪ್ರಮಾಣ",
    },
    "Inpatient Stay Duration": {
        "English": "Inpatient Stay Duration",
        "हिन्दी": "अस्पताल प्रवास की अवधि",
        "ಕನ್ನಡ": "ಆಸ್ಪತ್ರೆ ವಾಸ್ತವ್ಯದ ಅವಧಿ",
    },
    # Additional domains for feature manifests
    "Prior Inpatient Utilization": {
        "English": "Prior Inpatient Utilization",
        "हिन्दी": "पूर्व अस्पताल भर्ती",
        "ಕನ್ನಡ": "ಹಿಂದಿನ ಆಸ್ಪತ್ರೆ ದಾಖಲಾತಿ",
    },
    "Emergency Department Visits": {
        "English": "Emergency Department Visits",
        "हिन्दी": "आपातकालीन विभाग दौरे",
        "ಕನ್ನಡ": "ತುರ್ತು ಚಿಕಿತ್ಸಾ ಭೇಟಿಗಳು",
    },
    "Inpatient Procedures": {
        "English": "Inpatient Procedures",
        "हिन्दी": "भर्ती प्रक्रियाएं",
        "ಕನ್ನಡ": "ಒಳರೋಗಿ ಚಿಕಿತ್ಸಾ ವಿಧಾನಗಳು",
    },
    "Hospital Length of Stay": {
        "English": "Hospital Length of Stay",
        "हिन्दी": "अस्पताल में रहने की अवधि",
        "ಕನ್ನಡ": "ಆಸ್ಪತ್ರೆಯಲ್ಲಿ ವಾಸ್ತವ್ಯದ ಅವಧಿ",
    },
    "Outpatient Clinic History": {
        "English": "Outpatient Clinic History",
        "हिन्दी": "बाह्यरोगी क्लिनिक इतिहास",
        "ಕನ್ನಡ": "ಹೊರರೋಗಿ ಕ್ಲಿನಿಕ್ ಇತಿಹಾಸ",
    },
    "Medication Count / Complexity": {
        "English": "Medication Count / Complexity",
        "हिन्दी": "दवाओं की संख्या / जटिलता",
        "ಕನ್ನಡ": "ಔಷಧಿಗಳ ಸಂಖ್ಯೆ / ಸಂಕೀರ್ಣತೆ",
    },
    "Age Demographic": {
        "English": "Age Demographic",
        "हिन्दी": "आयु जनसांख्यिकी",
        "ಕನ್ನಡ": "ವಯಸ್ಸಿನ ವರ್ಗ",
    },
    "Diagnostic Morbidity Burden": {
        "English": "Diagnostic Morbidity Burden",
        "हिन्दी": "निदान सह-रुग्णता भार",
        "ಕನ್ನಡ": "ರೋಗನಿರ್ಣಯದ ತೀವ್ರತೆ",
    },
    "Glycemic Regimen Status": {
        "English": "Glycemic Regimen Status",
        "हिन्दी": "ग्लूकोज नियंत्रण स्थिति",
        "ಕನ್ನಡ": "ಗ್ಲೈಸೆಮಿಕ್ ಚಿಕಿತ್ಸಾ ಸ್ಥಿತಿ",
    },
}

FEATURE_TRANSLATIONS = {
    "number_inpatient": {
        "English": "Prior Admissions",
        "हिन्दी": "पूर्व दाखिले",
        "ಕನ್ನಡ": "ಹಿಂದಿನ ದಾಖಲಾತಿಗಳು",
    },
    "number_emergency": {
        "English": "Prior Emergency Room Visits (Past Year)",
        "हिन्दी": "पूर्व आपातकालीन दौरे (पिछला वर्ष)",
        "ಕನ್ನಡ": "ಹಿಂದಿನ ತುರ್ತು ಭೇಟಿಗಳು (ಕಳೆದ ವರ್ಷ)",
    },
    "number_outpatient": {
        "English": "Prior Outpatient Clinic Visits (Past Year)",
        "हिन्दी": "पूर्व बाह्यरोगी क्लिनिक दौरे (पिछला वर्ष)",
        "ಕನ್ನಡ": "ಹಿಂದಿನ ಹೊರರೋಗಿ ಭೇಟಿಗಳು (ಕಳೆದ ವರ್ಷ)",
    },
    "time_in_hospital": {
        "English": "Length of Inpatient Stay (Days)",
        "हिन्दी": "अस्पताल में रहने की अवधि (दिन)",
        "ಕನ್ನಡ": "ಆಸ್ಪತ್ರೆ ವಾಸ್ತವ್ಯದ ಅವಧಿ (ದಿನಗಳು)",
    },
    "num_medications": {
        "English": "Medication Count / Polypharmacy",
        "हिन्दी": "दवाओं की संख्या / पॉलीफार्मेसी",
        "ಕನ್ನಡ": "ಔಷಧಿಗಳ ಸಂಖ್ಯೆ / ಬಹು-ಔಷಧಿಗಳು",
    },
    "num_lab_procedures": {
        "English": "Total Laboratory Tests Performed",
        "हिन्दी": "कुल आयोजित लैब परीक्षण",
        "ಕನ್ನಡ": "ಮಾಡಲಾದ ಒಟ್ಟು ಲ್ಯಾಬ್ ಪರೀಕ್ಷೆಗಳು",
    },
    "num_procedures": {
        "English": "Inpatient Diagnostic / Operative Procedures",
        "हिन्दी": "भर्ती नैदानिक / शल्य प्रक्रियाएं",
        "ಕನ್ನಡ": "ಒಳರೋಗಿ ರೋಗನಿರ್ಣಯ / ಶಸ್ತ್ರಚಿಕಿತ್ಸಾ ವಿಧಾನಗಳು",
    },
    "number_diagnoses": {
        "English": "Multi-Morbidity Burden (Diagnoses Entered)",
        "हिन्दी": "सह-रुग्णता भार (दर्ज निदान)",
        "ಕನ್ನಡ": "ಬಹು-ಕಾಯಿಲೆಗಳ ತೀವ್ರತೆ (ದಾಖಲಾದ ರೋಗನಿರ್ಣಯಗಳು)",
    },
    "diag_1_Circulatory": {
        "English": "Primary Diagnosis: Circulatory / Cardiovascular",
        "हिन्दी": "प्राथमिक निदान: परिसंचरण / हृदय रोग",
        "ಕನ್ನಡ": "ಪ್ರಾಥಮಿಕ ರೋಗನಿರ್ಣಯ: ರಕ್ತಪರಿಚಲನೆ / ಹೃದ್ರೋಗ",
    },
    "diag_1_Respiratory": {
        "English": "Primary Diagnosis: Respiratory Illness",
        "हिन्दी": "प्राथमिक निदान: श्वसन रोग",
        "ಕನ್ನಡ": "ಪ್ರಾಥಮಿಕ ರೋಗನಿರ್ಣಯ: ಉಸಿರಾಟದ ಕಾಯಿಲೆ",
    },
    "diag_1_Digestive": {
        "English": "Primary Diagnosis: Digestive Disease",
        "हिन्दी": "प्राथमिक निदान: पाचन तंत्र विकार",
        "ಕನ್ನಡ": "ಪ್ರಾಥಮಿಕ ರೋಗನಿರ್ಣಯ: ಜೀರ್ಣಾಂಗ ಸಂಬಂಧಿ ಕಾಯಿಲೆ",
    },
    "diag_1_Diabetes": {
        "English": "Primary Diagnosis: Diabetes Mellitus",
        "हिन्दी": "प्राथमिक निदान: मधुमेह (डायबिटीज)",
        "ಕನ್ನಡ": "ಪ್ರಾಥಮಿಕ ರೋಗನಿರ್ಣಯ: ಮಧುಮೇಹ",
    },
    "diag_1_Missing": {
        "English": "Primary Diagnosis: Uncoded / Emergency Presentation",
        "हिन्दी": "प्राथमिक निदान: अनिर्धारित / आपातकालीन",
        "ಕನ್ನಡ": "ಪ್ರಾಥಮಿಕ ರೋಗನಿರ್ಣಯ: ಅನಿರ್ದಿಷ್ಟ / ತುರ್ತು ಪ್ರವೇಶ",
    },
    "admission_source_id_7": {
        "English": "Admission Source: Emergency Department",
        "हिन्दी": "प्रवेश स्रोत: आपातकालीन विभाग",
        "ಕನ್ನಡ": "ದಾಖಲಾತಿ ಮೂಲ: ತುರ್ತು ಚಿಕಿತ್ಸಾ ವಿಭಾಗ",
    },
    "admission_source_id_1": {
        "English": "Admission Source: Physician Referral",
        "हिन्दी": "प्रवेश स्रोत: चिकित्सक रेफरल",
        "ಕನ್ನಡ": "ದಾಖಲಾತಿ ಮೂಲ: ವೈದ್ಯರ ಶಿಫಾರಸು",
    },
    "admission_source_id_3": {
        "English": "Admission Source: HMO Referral",
        "हिन्दी": "प्रवेश स्रोत: HMO रेफरल",
        "ಕನ್ನಡ": "ದಾಖಲಾತಿ ಮೂಲ: HMO ಶಿಫಾರಸು",
    },
    "admission_type_id_1": {
        "English": "Admission Type: Emergency",
        "हिन्दी": "प्रवेश प्रकार: आपातकालीन",
        "ಕನ್ನಡ": "ದಾಖಲಾತಿ ಪ್ರಕಾರ: ತುರ್ತು",
    },
    "admission_type_id_2": {
        "English": "Admission Type: Urgent",
        "हिन्दी": "प्रवेश प्रकार: तत्काल/अत्यावश्यक",
        "ಕನ್ನಡ": "ದಾಖಲಾತಿ ಪ್ರಕಾರ: ತ್ವರಿತ/ಅತ್ಯಾವಶ್ಯಕ",
    },
    "admission_type_id_3": {
        "English": "Admission Type: Elective",
        "हिन्दी": "प्रवेश प्रकार: नियोजित (इलेक्टिव)",
        "ಕನ್ನಡ": "ದಾಖಲಾತಿ ಪ್ರಕಾರ: ಯೋಜಿತ (ಐಚ್ಛಿಕ)",
    },
    "insulin_Up": {
        "English": "Insulin Therapy: Dosage Escalated during Stay",
        "हिन्दी": "इंसुलिन थेरेपी: रहने के दौरान खुराक बढ़ाई गई",
        "ಕನ್ನಡ": "ಇನ್ಸುಲಿನ್ ಚಿಕಿತ್ಸೆ: ವಾಸ್ತವ್ಯದ ಸಮಯದಲ್ಲಿ ಡೋಸ್ ಹೆಚ್ಚಿಸಲಾಗಿದೆ",
    },
    "insulin_Down": {
        "English": "Insulin Therapy: Dosage Reduced during Stay",
        "हिन्दी": "इंसुलिन थेरेपी: रहने के दौरान खुराक घटाई गई",
        "ಕನ್ನಡ": "ಇನ್ಸುಲಿನ್ ಚಿಕಿತ್ಸೆ: ವಾಸ್ತವ್ಯದ ಸಮಯದಲ್ಲಿ ಡೋಸ್ ಕಡಿಮೆ ಮಾಡಲಾಗಿದೆ",
    },
    "insulin_Steady": {
        "English": "Insulin Therapy: Maintained Stable",
        "हिन्दी": "इंसुलिन थेरेपी: स्थिर रखी गई",
        "ಕನ್ನಡ": "ಇನ್ಸುಲಿನ್ ಚಿಕಿತ್ಸೆ: ಸ್ಥಿರವಾಗಿರಿಸಲಾಗಿದೆ",
    },
    "change_Ch": {
        "English": "Diabetic Medication Regimen Modified",
        "हिन्दी": "मधुमेह दवा व्यवस्था संशोधित",
        "ಕನ್ನಡ": "ಮಧುಮೇಹ ಔಷಧಿ ನಿಯಮಾವಳಿ ಬದಲಾಯಿಸಲಾಗಿದೆ",
    },
    "diabetesMed_Yes": {
        "English": "Prescribed Active Diabetes Medication",
        "हिन्दी": "सक्रिय मधुमेह दवा निर्धारित",
        "ಕನ್ನಡ": "ಸಕ್ರಿಯ ಮಧುಮೇಹ ಔಷಧಿ ನಿಗದಿಪಡಿಸಲಾಗಿದೆ",
    },
    "diabetesMed_No": {
        "English": "No Diabetes Medication Prescribed",
        "हिन्दी": "कोई मधुमेह दवा निर्धारित नहीं",
        "ಕನ್ನಡ": "ಯಾವುದೇ ಮಧುಮೇಹ ಔಷಧಿ ನಿಗದಿಪಡಿಸಿಲ್ಲ",
    },
    "A1Cresult_>8": {
        "English": "Elevated HbA1c (>8%)",
        "हिन्दी": "उच्च HbA1c (>8%)",
        "ಕನ್ನಡ": "ಹೆಚ್ಚಿನ HbA1c (>8%)",
    },
    "A1Cresult_Norm": {
        "English": "Normal HbA1c Level",
        "हिन्दी": "सामान्य HbA1c स्तर",
        "ಕನ್ನಡ": "ಸಾಮಾನ್ಯ HbA1c ಮಟ್ಟ",
    },
    "max_glu_serum_>300": {
        "English": "Acute Blood Glucose Surge (>300 mg/dL)",
        "हिन्दी": "तीव्र रक्त शर्करा वृद्धि (>300 mg/dL)",
        "ಕನ್ನಡ": "ತೀವ್ರ ರಕ್ತದ ಗ್ಲೂಕೋಸ್ ಹೆಚ್ಚಳ (>300 mg/dL)",
    },
    "repaglinide_Up": {
        "English": "Repaglinide Dose Escalated",
        "हिन्दी": "रेपाग्लिनाइड खुराक बढ़ाई गई",
        "ಕನ್ನಡ": "ರೆಪಾಗ್ಲಿನೈಡ್ ಡೋಸ್ ಹೆಚ್ಚಿಸಲಾಗಿದೆ",
    },
    "acarbose_Up": {
        "English": "Acarbose Dose Escalated",
        "हिन्दी": "एकार्बोस खुराक बढ़ाई गई",
        "ಕನ್ನಡ": "ಅಕಾರ್ಬೋಸ್ ಡೋಸ್ ಹೆಚ್ಚಿಸಲಾಗಿದೆ",
    },
}

DIAG_CATEGORY_TRANSLATIONS = {
    "Circulatory / cardiovascular condition": {
        "English": "Circulatory / cardiovascular condition",
        "हिन्दी": "परिसंचरण / हृदय रोग",
        "ಕನ್ನಡ": "ರಕ್ತಪರಿಚಲನೆ / ಹೃದ್ರೋಗ",
    },
    "Respiratory condition": {
        "English": "Respiratory condition",
        "हिन्दी": "श्वसन रोग",
        "ಕನ್ನಡ": "ಉಸಿರಾಟದ ಕಾಯಿಲೆ",
    },
    "Digestive condition": {
        "English": "Digestive condition",
        "हिन्दी": "पाचन तंत्र विकार",
        "ಕನ್ನಡ": "ಜೀರ್ಣಾಂಗ ಸಂಬಂಧಿ ಕಾಯಿಲೆ",
    },
    "Diabetes mellitus": {
        "English": "Diabetes mellitus",
        "हिन्दी": "मधुमेह (डायबिटीज)",
        "ಕನ್ನಡ": "ಮಧುಮೇಹ",
    },
    "Injury / trauma": {
        "English": "Injury / trauma",
        "हिन्दी": "चोट / आघात",
        "ಕನ್ನಡ": "ಗಾಯ / ಆಘಾತ",
    },
    "Musculoskeletal condition": {
        "English": "Musculoskeletal condition",
        "हिन्दी": "हड्डी / जोड़ रोग",
        "ಕನ್ನಡ": "ಮೂಳೆ ಮತ್ತು ಸ್ನಾಯು ಸಂಬಂಧಿ ಕಾಯಿಲೆ",
    },
    "Genitourinary condition": {
        "English": "Genitourinary condition",
        "हिन्दी": "मूत्र एवं जननांग रोग",
        "ಕನ್ನಡ": "ಮೂತ್ರಪಿಂಡ ಮತ್ತು ಜನನಾಂಗ ರೋಗ",
    },
    "Neoplasm / oncology": {
        "English": "Neoplasm / oncology",
        "हिन्दी": "रसौली / ऑन्कोलॉजी",
        "ಕನ್ನಡ": "ಗೆಡ್ಡೆ / ಕ್ಯಾನ್ಸರ್ ಸಂಬಂಧಿ",
    },
    "Supplemental / external factor code": {
        "English": "Supplemental / external factor code",
        "हिन्दी": "पूरक / बाहरी कारक कोड",
        "ಕನ್ನಡ": "ಪೂರಕ / ಬಾಹ್ಯ ಅಂಶ ಕೋಡ್",
    },
    "Not documented in billing records": {
        "English": "Not documented in billing records",
        "हिन्दी": "बिलिंग रिकॉर्ड में दर्ज नहीं",
        "ಕನ್ನಡ": "ಬಿಲ್ಲಿಂಗ್ ದಾಖಲೆಗಳಲ್ಲಿ ನಮೂದಿಸಿಲ್ಲ",
    },
}

# -----------------------------------------------------------------------------
# Patient Summary Templates & Components
# -----------------------------------------------------------------------------

SUMMARY_TIER_INTRO = {
    "highest_tier": {
        "English": "This encounter received an estimated model prioritization score of <strong>{score_pct}%</strong> (<strong>{tier}</strong>), placing it in the highest tier of prioritized candidates.",
        "हिन्दी": "इस एनकाउंटर को <strong>{score_pct}%</strong> (<strong>{tier}</strong>) का अनुमानित मॉडल प्राथमिकता स्कोर प्राप्त हुआ है, जो इसे प्राथमिकता वाले उम्मीदवारों की उच्चतम श्रेणी में रखता है।",
        "ಕನ್ನಡ": "ಈ ದಾಖಲಾತಿಯು <strong>{score_pct}%</strong> (<strong>{tier}</strong>) ಅಂದಾಜು ಮಾದರಿ ಆದ್ಯತಾ ಸ್ಕೋರ್ ಪಡೆದಿದ್ದು, ಆದ್ಯತೆಯ ಅಭ್ಯರ್ಥಿಗಳ ಅತ್ಯುನ್ನತ ಶ್ರೇಣಿಯಲ್ಲಿದೆ.",
    },
    "higher_tier": {
        "English": "This encounter received an estimated model prioritization score of <strong>{score_pct}%</strong> (<strong>{tier}</strong>), positioning it above the higher-score threshold.",
        "हिन्दी": "इस एनकाउंटर को <strong>{score_pct}%</strong> (<strong>{tier}</strong>) का अनुमानित मॉडल प्राथमिकता स्कोर प्राप्त हुआ है, जो इसे उच्च-स्कोर थ्रेशोल्ड से ऊपर रखता है।",
        "ಕನ್ನಡ": "ಈ ದಾಖಲಾತಿಯು <strong>{score_pct}%</strong> (<strong>{tier}</strong>) ಅಂದಾಜು ಮಾದರಿ ಆದ್ಯತಾ ಸ್ಕೋರ್ ಪಡೆದಿದ್ದು, ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಮಿತಿಗಿಂತ ಮೇಲಿದೆ.",
    },
    "mod_high": {
        "English": "This encounter received an estimated model prioritization score of <strong>{score_pct}%</strong> (<strong>{tier}</strong>), reflecting moderate statistical prioritization.",
        "हिन्दी": "इस एनकाउंटर को <strong>{score_pct}%</strong> (<strong>{tier}</strong>) का अनुमानित मॉडल प्राथमिकता स्कोर प्राप्त हुआ है, जो मध्यम सांख्यिकीय प्राथमिकता को दर्शाता है।",
        "ಕನ್ನಡ": "ಈ ದಾಖಲಾತಿಯು <strong>{score_pct}%</strong> (<strong>{tier}</strong>) ಅಂದಾಜು ಮಾದರಿ ಆದ್ಯತಾ ಸ್ಕೋರ್ ಪಡೆದಿದ್ದು, ಮಧ್ಯಮ ಮಟ್ಟದ ಸಂಖ್ಯಾಶಾಸ್ತ್ರೀಯ ಆದ್ಯತೆಯನ್ನು ಸೂಚಿಸುತ್ತದೆ.",
    },
    "mod_tier": {
        "English": "This encounter received an estimated model prioritization score of <strong>{score_pct}%</strong> (<strong>{tier}</strong>), placing it in the secondary follow-up tier.",
        "हिन्दी": "इस एनकाउंटर को <strong>{score_pct}%</strong> (<strong>{tier}</strong>) का अनुमानित मॉडल प्राथमिकता स्कोर प्राप्त हुआ है, जो इसे द्वितीयक अनुवर्ती श्रेणी में रखता है।",
        "ಕನ್ನಡ": "ಈ ದಾಖಲಾತಿಯು <strong>{score_pct}%</strong> (<strong>{tier}</strong>) ಅಂದಾಜು ಮಾದರಿ ಆದ್ಯತಾ ಸ್ಕೋರ್ ಪಡೆದಿದ್ದು, ದ್ವಿತೀಯ ಹಂತದ ಆರೈಕೆ ಶ್ರೇಣಿಯಲ್ಲಿದೆ.",
    },
    "lower_mod": {
        "English": "This encounter received an estimated model prioritization score of <strong>{score_pct}%</strong> (<strong>{tier}</strong>), below the moderate threshold.",
        "हिन्दी": "इस एनकाउंटर को <strong>{score_pct}%</strong> (<strong>{tier}</strong>) का अनुमानित मॉडल प्राथमिकता स्कोर प्राप्त हुआ है, जो मध्यम थ्रेशोल्ड से नीचे है।",
        "ಕನ್ನಡ": "ಈ ದಾಖಲಾತಿಯು <strong>{score_pct}%</strong> (<strong>{tier}</strong>) ಅಂದಾಜು ಮಾದರಿ ಆದ್ಯತಾ ಸ್ಕೋರ್ ಪಡೆದಿದ್ದು, ಮಧ್ಯಮ ಮಿತಿಗಿಂತ ಕಡಿಮೆಯಾಗಿದೆ.",
    },
    "lowest_tier": {
        "English": "This encounter received an estimated model prioritization score of <strong>{score_pct}%</strong> (<strong>{tier}</strong>), placing it among the lowest score tiers in the cohort.",
        "हिन्दी": "इस एनकाउंटर को <strong>{score_pct}%</strong> (<strong>{tier}</strong>) का अनुमानित मॉडल प्राथमिकता स्कोर प्राप्त हुआ है, जो इसे कोहोर्ट की सबसे निचली स्कोर श्रेणी में रखता है।",
        "ಕನ್ನಡ": "ಈ ದಾಖಲಾತಿಯು <strong>{score_pct}%</strong> (<strong>{tier}</strong>) ಅಂದಾಜು ಮಾದರಿ ಆದ್ಯತಾ ಸ್ಕೋರ್ ಪಡೆದಿದ್ದು, ಗುಂಪಿನ ಅತ್ಯಂತ ಕಡಿಮೆ ಸ್ಕೋರ್ ಶ್ರೇಣಿಯಲ್ಲಿದೆ.",
    },
}

SUMMARY_CONTEXT_SENTENCE = {
    "frequent_acute": {
        "English": "This elevated score is driven primarily by frequent prior acute-care utilization ({inpatient} inpatient admissions and {emergency} emergency visits in the past year) alongside in-hospital clinical factors.",
        "हिन्दी": "यह उच्च स्कोर मुख्य रूप से अस्पताल के नैदानिक कारकों के साथ-साथ बार-बार पूर्व तीव्र देखभाल उपयोग (पिछले वर्ष में {inpatient} अस्पताल दाखिले और {emergency} आपातकालीन दौरे) से प्रेरित है।",
        "ಕನ್ನಡ": "ಈ ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಮುಖ್ಯವಾಗಿ ಆಸ್ಪತ್ರೆಯ ಕ್ಲಿನಿಕಲ್ ಅಂಶಗಳೊಂದಿಗೆ ಹಿಂದಿನ ಆಗಾಗ್ಗೆ ತುರ್ತು ಆರೈಕೆ ಬಳಕೆಯಿಂದ ({inpatient} ಒಳರೋಗಿ ದಾಖಲಾತಿಗಳು ಮತ್ತು {emergency} ತುರ್ತು ಭೇಟಿಗಳು) ಬಂದಿದೆ.",
    },
    "inpatient_only": {
        "English": "In the model's evaluation, this score reflects documented prior inpatient admission history ({inpatient} visit(s) in the past year) alongside in-hospital clinical indicators, with zero recorded emergency visits.",
        "हिन्दी": "मॉडल के मूल्यांकन में, यह स्कोर शून्य दर्ज आपातकालीन दौरों के साथ-साथ अस्पताल के नैदानिक संकेतकों और पिछले वर्ष के अस्पताल दाखिला इतिहास ({inpatient} दाखिला) को दर्शाता है।",
        "ಕನ್ನಡ": "ಮಾದರಿಯ ಮೌಲ್ಯಮಾಪನದಲ್ಲಿ, ಈ ಸ್ಕೋರ್ ಶೂನ್ಯ ತುರ್ತು ಭೇಟಿಗಳೊಂದಿಗೆ ಆಸ್ಪತ್ರೆಯ ಕ್ಲಿನಿಕಲ್ ಅಂಶಗಳು ಮತ್ತು ಹಿಂದಿನ ದಾಖಲಾತಿ ಇತಿಹಾಸವನ್ನು ({inpatient} ದಾಖಲಾತಿ) ಪ್ರತಿಬಿಂಬಿಸುತ್ತದೆ.",
    },
    "emergency_only": {
        "English": "In the model's evaluation, this score is influenced by documented prior emergency room visits ({emergency} visit(s) in the past year) despite zero recorded previous inpatient admissions.",
        "हिन्दी": "मॉडल के मूल्यांकन में, यह स्कोर शून्य पूर्व अस्पताल दाखिलों के बावजूद पिछले वर्ष के आपातकालीन दौरों ({emergency} दौरे) से प्रभावित है।",
        "ಕನ್ನಡ": "ಮಾದರಿಯ ಮೌಲ್ಯಮಾಪನದಲ್ಲಿ, ಈ ಸ್ಕೋರ್ ಶೂನ್ಯ ಒಳರೋಗಿ ದಾಖಲಾತಿಗಳ ಹೊರತಾಗಿಯೂ ಹಿಂದಿನ ತುರ್ತು ಭೇಟಿಗಳಿಂದ ({emergency} ಭೇಟಿಗಳು) ಪ್ರಭಾವಿತವಾಗಿದೆ.",
    },
    "both_moderate": {
        "English": "In the model's evaluation, this score reflects recorded prior acute-care utilization ({inpatient} inpatient admission(s) and {emergency} emergency visit(s) in the past year).",
        "हिन्दी": "मॉडल के मूल्यांकन में, यह स्कोर पिछले वर्ष के दर्ज तीव्र देखभाल उपयोग ({inpatient} अस्पताल दाखिले और {emergency} आपातकालीन दौरे) को दर्शाता है।",
        "ಕನ್ನಡ": "ಮಾದರಿಯ ಮೌಲ್ಯಮಾಪನದಲ್ಲಿ, ಈ ಸ್ಕೋರ್ ಹಿಂದಿನ ತೀವ್ರ ಆರೈಕೆ ಬಳಕೆಯನ್ನು ({inpatient} ಒಳರೋಗಿ ದಾಖಲಾತಿಗಳು ಮತ್ತು {emergency} ತುರ್ತು ಭೇಟಿಗಳು) ಪ್ರತಿಬಿಂಬಿಸುತ್ತದೆ.",
    },
    "zero_util_high": {
        "English": "Despite zero prior acute admissions over the past year, this elevated score is driven by in-hospital clinical factors including medication adjustments, stay duration, or diagnostic complexity.",
        "हिन्दी": "पिछले वर्ष शून्य पूर्व दाखिलों के बावजूद, यह उच्च स्कोर अस्पताल के नैदानिक कारकों जैसे दवा समायोजन, ठहरने की अवधि, या नैदानिक जटिलता से प्रेरित है।",
        "ಕನ್ನಡ": "ಕಳೆದ ವರ್ಷ ಯಾವುದೇ ಹಿಂದಿನ ದಾಖಲಾತಿ ಇಲ್ಲದಿದ್ದರೂ, ಔಷಧ ಬದಲಾವಣೆಗಳು, ವಾಸ್ತವ್ಯದ ಅವಧಿ ಅಥವಾ ರೋಗನಿರ್ಣಯದ ತೀವ್ರತೆಯಿಂದಾಗಿ ಈ ಸ್ಕೋರ್ ಹೆಚ್ಚಾಗಿದೆ.",
    },
    "zero_util_mod": {
        "English": "The score reflects a balanced profile where in-hospital clinical factors are tempered by an absence of prior acute-care utilization over the past year.",
        "हिन्दी": "यह स्कोर एक संतुलित प्रोफ़ाइल को दर्शाता है जहां अस्पताल के नैदानिक कारक पिछले वर्ष में पूर्व तीव्र देखभाल उपयोग की अनुपस्थिति से संतुलित होते हैं।",
        "ಕನ್ನಡ": "ಈ ಸ್ಕೋರ್ ಸಮತೋಲಿತ ವಿವರವನ್ನು ಪ್ರತಿಬಿಂಬಿಸುತ್ತದೆ, ಇಲ್ಲಿ ಹಿಂದಿನ ಯಾವುದೇ ತುರ್ತು ಆರೈಕೆ ಬಳಕೆ ಇಲ್ಲದಿರುವುದು ಆಸ್ಪತ್ರೆಯ ಅಂಶಗಳನ್ನು ಸಮತೋಲನಗೊಳಿಸುತ್ತದೆ.",
    },
    "zero_util_low": {
        "English": "The model identified predominantly score-lowering indicators, led by zero recorded prior acute admissions and stable clinical features.",
        "हिन्दी": "मॉडल ने मुख्य रूप से स्कोर घटाने वाले संकेतकों की पहचान की है, जिसमें शून्य पूर्व दाखिले और स्थिर नैदानिक विशेषताएं प्रमुख हैं।",
        "ಕನ್ನಡ": "ಮಾದರಿಯು ಮುಖ್ಯವಾಗಿ ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುವ ಅಂಶಗಳನ್ನು ಗುರುತಿಸಿದೆ, ಇದರಲ್ಲಿ ಹಿಂದಿನ ಶೂನ್ಯ ದಾಖಲಾತಿಗಳು ಮತ್ತು ಸ್ಥಿರ ಕ್ಲಿನಿಕಲ್ ಲಕ್ಷಣಗಳು ಸೇರಿವೆ.",
    },
}

SUMMARY_FACTORS = {
    # Utilization Factors
    "util_pos_frequent": {
        "English": "<strong>Supports higher score</strong>: Documented history of frequent acute utilization: <strong>{inpatient} inpatient admissions</strong> and <strong>{emergency} emergency room visits</strong> in the preceding 12 months, which the model weights as a compounding historical risk indicator.",
        "हिन्दी": "<strong>उच्च स्कोर का समर्थन करता है</strong>: पिछले 12 महीनों में बार-बार तीव्र उपयोग का दर्ज इतिहास: <strong>{inpatient} अस्पताल दाखिले</strong> और <strong>{emergency} आपातकालीन दौरे</strong>, जिसे मॉडल एक संयुक्त ऐतिहासिक जोखिम संकेतक मानता है।",
        "ಕನ್ನಡ": "<strong>ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ</strong>: ಕಳೆದ 12 ತಿಂಗಳುಗಳಲ್ಲಿ ಆಗಾಗ್ಗೆ ತೀವ್ರ ಬಳಕೆಯ ದಾಖಲಿತ ಇತಿಹಾಸ: <strong>{inpatient} ಒಳರೋಗಿ ದಾಖಲಾತಿಗಳು</strong> ಮತ್ತು <strong>{emergency} ತುರ್ತು ಕೊಠಡಿ ಭೇಟಿಗಳು</strong>, ಇದನ್ನು ಮಾದರಿಯು ಸಂಯೋಜಿತ ಅಪಾಯದ ಅಂಶವೆಂದು ಪರಿಗಣಿಸುತ್ತದೆ.",
    },
    "util_pos_both": {
        "English": "<strong>Supports higher score</strong>: Documented history of <strong>{inpatient} prior inpatient admission(s)</strong> and <strong>{emergency} emergency room visit(s)</strong> in the past year, representing prior acute-care utilization across both inpatient and emergency departments.",
        "हिन्दी": "<strong>उच्च स्कोर का समर्थन करता है</strong>: पिछले वर्ष में <strong>{inpatient} पूर्व अस्पताल दाखिले</strong> और <strong>{emergency} आपातकालीन दौरे</strong> का दर्ज इतिहास, जो इनपेशेंट और इमरजेंसी दोनों विभागों में पूर्व उपयोग को दर्शाता है।",
        "ಕನ್ನಡ": "<strong>ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ</strong>: ಕಳೆದ ವರ್ಷದಲ್ಲಿ <strong>{inpatient} ಹಿಂದಿನ ಒಳರೋಗಿ ದಾಖಲಾತಿಗಳು</strong> ಮತ್ತು <strong>{emergency} ತುರ್ತು ಭೇಟಿಗಳ</strong> ದಾಖಲಿತ ಇತಿಹಾಸ.",
    },
    "util_pos_inp_only": {
        "English": "<strong>Supports higher score</strong>: Documented history of <strong>{inpatient} prior inpatient admission(s)</strong> in the past year, alongside <strong>0 recorded emergency room visits</strong> over the same timeframe.",
        "हिन्दी": "<strong>उच्च स्कोर का समर्थन करता है</strong>: पिछले वर्ष में <strong>{inpatient} पूर्व अस्पताल दाखिले</strong> का दर्ज इतिहास, साथ ही उसी समयावधि में <strong>0 दर्ज आपातकालीन दौरे</strong>।",
        "ಕನ್ನಡ": "<strong>ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ</strong>: ಕಳೆದ ವರ್ಷದಲ್ಲಿ <strong>{inpatient} ಹಿಂದಿನ ದಾಖಲಾತಿಗಳ</strong> ದಾಖಲಿತ ಇತಿಹಾಸ, ಮತ್ತು ಅದೇ ಸಮಯದಲ್ಲಿ <strong>0 ತುರ್ತು ಭೇಟಿಗಳು</strong>.",
    },
    "util_pos_er_only": {
        "English": "<strong>Supports higher score</strong>: Documented <strong>{emergency} emergency room visit(s)</strong> in the past year, while having <strong>0 recorded previous inpatient admissions</strong>.",
        "हिन्दी": "<strong>उच्च स्कोर का समर्थन करता है</strong>: पिछले वर्ष में <strong>{emergency} आपातकालीन दौरे</strong> दर्ज किए गए, जबकि <strong>0 पूर्व अस्पताल दाखिले</strong> थे।",
        "ಕನ್ನಡ": "<strong>ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ</strong>: ಕಳೆದ ವರ್ಷದಲ್ಲಿ <strong>{emergency} ತುರ್ತು ಭೇಟಿಗಳು</strong> ದಾಖಲಾಗಿವೆ, ಮತ್ತು <strong>0 ಹಿಂದಿನ ದಾಖಲಾತಿಗಳು</strong> ಇವೆ.",
    },
    "util_neg_zero": {
        "English": "<strong>Lowers model score</strong>: The record documents <strong>0 prior inpatient admissions and 0 emergency visits</strong> in the past 12 months, which contributes negatively to the model's risk calculation.",
        "हिन्दी": "<strong>मॉडल स्कोर कम करता है</strong>: रिकॉर्ड में पिछले 12 महीनों में <strong>0 पूर्व अस्पताल दाखिले और 0 आपातकालीन दौरे</strong> दर्ज हैं, जो मॉडल की जोखिम गणना को कम करता है।",
        "ಕನ್ನಡ": "<strong>ಮಾದರಿ ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ</strong>: ದಾಖಲೆಯಲ್ಲಿ ಕಳೆದ 12 ತಿಂಗಳುಗಳಲ್ಲಿ <strong>0 ಹಿಂದಿನ ದಾಖಲಾತಿಗಳು ಮತ್ತು 0 ತುರ್ತು ಭೇಟಿಗಳು</strong> ಇವೆ, ಇದು ಅಪಾಯದ ಲೆಕ್ಕಾಚಾರವನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ.",
    },

    # Medication Factors
    "ins_pos": {
        "English": "<strong>Supports higher score</strong>: Insulin dosage was actively <strong>{change_desc} during the hospital stay</strong> (status: <em>{status}</em>), a dynamic titration pattern associated with post-discharge transition vulnerability in the model.",
        "हिन्दी": "<strong>उच्च स्कोर का समर्थन करता है</strong>: अस्पताल में रहने के दौरान इंसुलिन की खुराक सक्रिय रूप से <strong>{change_desc}</strong> (स्थिति: <em>{status}</em>), जो डिस्चार्ज के बाद संक्रमण जोखिम से जुड़ा है।",
        "ಕನ್ನಡ": "<strong>ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ</strong>: ಆಸ್ಪತ್ರೆ ವಾಸ್ತವ್ಯದ ಸಮಯದಲ್ಲಿ ಇನ್ಸುಲಿನ್ ಡೋಸ್ ಅನ್ನು <strong>{change_desc}</strong> (ಸ್ಥಿತಿ: <em>{status}</em>), ಇದು ಡಿಸ್ಚಾರ್ಜ್ ನಂತರದ ಸೂಕ್ಷ್ಮತೆಯೊಂದಿಗೆ ಸಂಬಂಧಿಸಿದೆ.",
    },
    "chg_pos": {
        "English": "<strong>Supports higher score</strong>: Diabetic medication regimen was <strong>modified during admission</strong>, which the model identifies as an indicator of in-hospital pharmacological adjustments.",
        "हिन्दी": "<strong>उच्च स्कोर का समर्थन करता है</strong>: अस्पताल में भर्ती के दौरान मधुमेह दवा व्यवस्था में <strong>बदलाव किया गया</strong>, जिसे मॉडल औषधीय समायोजन का संकेतक मानता है।",
        "ಕನ್ನಡ": "<strong>ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ</strong>: ದಾಖಲಾತಿಯ ಸಮಯದಲ್ಲಿ ಮಧುಮೇಹ ಔಷಧಿ ನಿಯಮಾವಳಿಯನ್ನು <strong>ಬದಲಾಯಿಸಲಾಗಿದೆ</strong>, ಇದನ್ನು ಔಷಧೀಯ ಹೊಂದಾಣಿಕೆಯ ಸೂಚಕವೆಂದು ಪರಿಗಣಿಸಲಾಗುತ್ತದೆ.",
    },
    "ins_neg_steady": {
        "English": "<strong>Lowers model score</strong>: Insulin regimen remained <strong>stable throughout the stay</strong> without documented dosage escalations or reductions.",
        "हिन्दी": "<strong>मॉडल स्कोर कम करता है</strong>: इंसुलिन व्यवस्था रहने के दौरान <strong>स्थिर रही</strong> बिना किसी दर्ज खुराक वृद्धि या कमी के।",
        "ಕನ್ನಡ": "<strong>ಮಾದರಿ ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ</strong>: ಯಾವುದೇ ಡೋಸ್ ಹೆಚ್ಚಳ ಅಥವಾ ಕಡಿತವಿಲ್ಲದೆ ಇನ್ಸುಲಿನ್ ನಿಯಮಾವಳಿ ವಾಸ್ತವ್ಯದುದ್ದಕ್ಕೂ <strong>ಸ್ಥಿರವಾಗಿತ್ತು</strong>.",
    },
    "dm_neg_no": {
        "English": "<strong>Lowers model score</strong>: No diabetes medications were prescribed during this encounter, which provides a negative log-odds weight in the readmission model.",
        "हिन्दी": "<strong>मॉडल स्कोर कम करता है</strong>: इस एनकाउंटर के दौरान कोई मधुमेह दवा निर्धारित नहीं की गई थी, जो मॉडल में नकारात्मक भार प्रदान करती है।",
        "ಕನ್ನಡ": "<strong>ಮಾದರಿ ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ</strong>: ಈ ದಾಖಲಾತಿಯಲ್ಲಿ ಯಾವುದೇ ಮಧುಮೇಹ ಔಷಧಿಗಳನ್ನು ಸೂಚಿಸಲಾಗಿಲ್ಲ, ಇದು ಮಾದರಿಯಲ್ಲಿ ಋಣಾತ್ಮಕ ತೂಕವನ್ನು ಒದಗಿಸುತ್ತದೆ.",
    },

    # Length of Stay
    "stay_pos": {
        "English": "<strong>Supports higher score</strong>: Hospital stay spanned <strong>{days} days</strong>, reflecting an extended inpatient duration relative to the cohort median (4 days).",
        "हिन्दी": "<strong>उच्च स्कोर का समर्थन करता है</strong>: अस्पताल में रहने की अवधि <strong>{days} दिन</strong> थी, जो औसत अवधि (4 दिन) की तुलना में अधिक है।",
        "ಕನ್ನಡ": "<strong>ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ</strong>: ಆಸ್ಪತ್ರೆಯ ವಾಸ್ತವ್ಯ <strong>{days} ದಿನಗಳಾಗಿದ್ದು</strong>, ಸರಾಸರಿ ಅವಧಿಗಿಂತ (4 ದಿನಗಳು) ದೀರ್ಘವಾಗಿದೆ.",
    },
    "stay_neg": {
        "English": "<strong>Lowers model score</strong>: Hospital stay was brief (<strong>{days} day(s)</strong>), providing a negative weight that attenuates the model score compared to extended admissions.",
        "हिन्दी": "<strong>मॉडल स्कोर कम करता है</strong>: अस्पताल में रहने की अवधि संक्षिप्त थी (<strong>{days} दिन</strong>), जो लंबे समय तक रहने की तुलना में स्कोर को कम करती है।",
        "ಕನ್ನಡ": "<strong>ಮಾದರಿ ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ</strong>: ಆಸ್ಪತ್ರೆಯ ವಾಸ್ತವ್ಯವು ಸಂಕ್ಷಿಪ್ತವಾಗಿತ್ತು (<strong>{days} ದಿನಗಳು</strong>), ಇದು ಮಾದರಿ ಸ್ಕೋರ್ ಅನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ.",
    },

    # Polypharmacy / Medication count
    "med_pos": {
        "English": "<strong>Supports higher score</strong>: Documented administration of <strong>{meds} distinct medications</strong> during the hospital encounter, indicating considerable medication regimen complexity.",
        "हिन्दी": "<strong>उच्च स्कोर का समर्थन करता है</strong>: अस्पताल प्रवास के दौरान <strong>{meds} विभिन्न दवाएं</strong> दी गईं, जो जटिल दवा व्यवस्था का संकेत देती हैं।",
        "ಕನ್ನಡ": "<strong>ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ</strong>: ಆಸ್ಪತ್ರೆ ವಾಸ್ತವ್ಯದ ಸಮಯದಲ್ಲಿ <strong>{meds} ವಿಭಿನ್ನ ಔಷಧಿಗಳನ್ನು</strong> ನೀಡಲಾಗಿದ್ದು, ಇದು ಔಷಧಿ ನಿಯಮಾವಳಿಯ ಸಂಕೀರ್ಣತೆಯನ್ನು ಸೂಚಿಸುತ್ತದೆ.",
    },
    "med_neg": {
        "English": "<strong>Lowers model score</strong>: Low medication volume recorded (<strong>{meds} medications</strong>), reflecting lower regimen complexity during hospitalization.",
        "हिन्दी": "<strong>मॉडल स्कोर कम करता है</strong>: दवाओं की कम मात्रा दर्ज की गई (<strong>{meds} दवाएं</strong>), जो अस्पताल में भर्ती के दौरान कम जटिलता को दर्शाती है।",
        "ಕನ್ನಡ": "<strong>ಮಾದರಿ ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ</strong>: ಕಡಿಮೆ ಔಷಧಿಗಳ ಸಂಖ್ಯೆ ದಾಖಲಾಗಿದೆ (<strong>{meds} ಔಷಧಿಗಳು</strong>), ಇದು ಆಸ್ಪತ್ರೆಯ ಸಮಯದಲ್ಲಿ ಕಡಿಮೆ ಸಂಕೀರ್ಣತೆಯನ್ನು ಸೂಚಿಸುತ್ತದೆ.",
    },

    # Multi-Morbidity / Diagnoses count
    "diag_cnt_pos": {
        "English": "<strong>Supports higher score</strong>: Documented high diagnostic burden with <strong>{diagnoses} billing diagnoses entered</strong>, indicating documented multi-morbidity in the medical record.",
        "हिन्दी": "<strong>उच्च स्कोर का समर्थन करता है</strong>: <strong>{diagnoses} बिलिंग निदान दर्ज</strong> के साथ उच्च नैदानिक भार, जो मेडिकल रिकॉर्ड में सह-रुग्णता को दर्शाता है।",
        "ಕನ್ನಡ": "<strong>ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ</strong>: <strong>{diagnoses} ಬಿಲ್ಲಿಂಗ್ ರೋಗನಿರ್ಣಯಗಳೊಂದಿಗೆ</strong> ಹೆಚ್ಚಿನ ರೋಗನಿರ್ಣಯದ ತೀವ್ರತೆ ದಾಖಲಾಗಿದೆ.",
    },
    "diag_cnt_neg": {
        "English": "<strong>Lowers model score</strong>: Limited secondary diagnoses entered (<strong>{diagnoses} condition(s)</strong>), reflecting lower documented multi-morbidity burden.",
        "हिन्दी": "<strong>मॉडल स्कोर कम करता है</strong>: सीमित द्वितीयक निदान दर्ज (<strong>{diagnoses} स्थितियां</strong>), जो कम सह-रुग्णता भार को दर्शाता है।",
        "ಕನ್ನಡ": "<strong>ಮಾದರಿ ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ</strong>: ಸೀಮಿತ ರೋಗನಿರ್ಣಯಗಳನ್ನು ದಾಖಲಿಸಲಾಗಿದೆ (<strong>{diagnoses} ಲಕ್ಷಣಗಳು</strong>), ಇದು ಕಡಿಮೆ ಬಹು-ಕಾಯಿಲೆಗಳ ತೀವ್ರತೆಯನ್ನು ಸೂಚಿಸುತ್ತದೆ.",
    },

    # Procedures
    "proc_pos": {
        "English": "<strong>Supports higher score</strong>: Documented <strong>{procedures} diagnostic or operative procedures</strong> performed during this admission, reflecting clinical intervention intensity.",
        "हिन्दी": "<strong>उच्च स्कोर का समर्थन करता है</strong>: इस प्रवेश के दौरान <strong>{procedures} नैदानिक या शल्य प्रक्रियाएं</strong> की गईं, जो गहन नैदानिक हस्तक्षेप को दर्शाती हैं।",
        "ಕನ್ನಡ": "<strong>ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ</strong>: ಈ ದಾಖಲಾತಿಯ ಸಮಯದಲ್ಲಿ <strong>{procedures} ರೋಗನಿರ್ಣಯ ಅಥವಾ ಶಸ್ತ್ರಚಿಕಿತ್ಸಾ ವಿಧಾನಗಳನ್ನು</strong> ನಡೆಸಲಾಗಿದೆ.",
    },
    "proc_neg": {
        "English": "<strong>Lowers model score</strong>: <strong>0 surgical or invasive procedures</strong> recorded during this stay, which attenuates the model score.",
        "हिन्दी": "<strong>मॉडल स्कोर कम करता है</strong>: इस दौरान <strong>0 शल्य या आक्रामक प्रक्रियाएं</strong> दर्ज की गईं, जो मॉडल स्कोर को कम करती हैं।",
        "ಕನ್ನಡ": "<strong>ಮಾದರಿ ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ</strong>: ಈ ವಾಸ್ತವ್ಯದ ಸಮಯದಲ್ಲಿ <strong>0 ಶಸ್ತ್ರಚಿಕಿತ್ಸಾ ವಿಧಾನಗಳು</strong> ದಾಖಲಾಗಿದ್ದು, ಇದು ಸ್ಕೋರ್ ಅನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ.",
    },

    # Age Demographic
    "age_pos": {
        "English": "<strong>Supports higher score</strong>: Patient belongs to the <strong>{age} age bracket</strong>, an older demographic category with higher statistical readmission rates in historical EHR records.",
        "हिन्दी": "<strong>उच्च स्कोर का समर्थन करता है</strong>: रोगी <strong>{age} आयु वर्ग</strong> से संबंधित है, जो ऐतिहासिक रिकॉर्ड में उच्च पुनः भर्ती दर वाली वृद्ध श्रेणी है।",
        "ಕನ್ನಡ": "<strong>ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ</strong>: ರೋಗಿಯು <strong>{age} ವಯಸ್ಸಿನ ವರ್ಗಕ್ಕೆ</strong> ಸೇರಿದವರಾಗಿದ್ದು, ಐತಿಹಾಸಿಕ ದಾಖಲೆಗಳಲ್ಲಿ ಹೆಚ್ಚಿನ ಮರುದಾಖಲಾತಿ ಪ್ರಮಾಣ ಹೊಂದಿರುವ ಹಿರಿಯ ವರ್ಗವಾಗಿದೆ.",
    },
    "age_neg": {
        "English": "<strong>Lowers model score</strong>: Patient is in the <strong>{age} age bracket</strong>, a younger demographic that provides a negative log-odds weight in the baseline model.",
        "हिन्दी": "<strong>मॉडल स्कोर कम करता है</strong>: रोगी <strong>{age} आयु वर्ग</strong> में है, जो एक युवा वर्ग है और मॉडल में नकारात्मक भार प्रदान करता है।",
        "ಕನ್ನಡ": "<strong>ಮಾದರಿ ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ</strong>: ರೋಗಿಯು <strong>{age} ವಯಸ್ಸಿನ ವರ್ಗದಲ್ಲಿದ್ದಾರೆ</strong>, ಇದು ಕಿರಿಯ ವಯಸ್ಸಿನ ವರ್ಗವಾಗಿದ್ದು ಮಾದರಿಯಲ್ಲಿ ಋಣಾತ್ಮಕ ತೂಕವನ್ನು ನೀಡುತ್ತದೆ.",
    },

    # Glycemic Labs
    "a1c_pos": {
        "English": "<strong>Recorded lab marker</strong>: Documented elevated HbA1c result of <strong>{a1c}%</strong>, reflecting heightened average blood glucose levels in the weeks preceding hospitalization.",
        "हिन्दी": "<strong>दर्ज लैब मार्कर</strong>: <strong>{a1c}%</strong> का उच्च HbA1c परिणाम दर्ज किया गया, जो अस्पताल में भर्ती होने से पहले के हफ्तों में बढ़े हुए औसत रक्त शर्करा को दर्शाता है।",
        "ಕನ್ನಡ": "<strong>ದಾಖಲಾದ ಲ್ಯಾಬ್ ಗುರುತು</strong>: <strong>{a1c}%</strong> ಹೆಚ್ಚಿನ HbA1c ಫಲಿತಾಂಶ ದಾಖಲಾಗಿದೆ, ಇದು ಆಸ್ಪತ್ರೆಗೆ ದಾಖಲಾಗುವ ಮೊದಲಿನ ವಾರಗಳಲ್ಲಿ ಹೆಚ್ಚಿನ ರಕ್ತದ ಗ್ಲೂಕೋಸ್ ಮಟ್ಟವನ್ನು ಸೂಚಿಸುತ್ತದೆ.",
    },
    "a1c_neg_norm": {
        "English": "<strong>Lowers model score</strong>: Documented normal HbA1c test result during admission, indicating baseline glycemic stability.",
        "हिन्दी": "<strong>मॉडल स्कोर कम करता है</strong>: प्रवेश के दौरान सामान्य HbA1c परीक्षण परिणाम दर्ज किया गया, जो ग्लूकोज स्थिरता को दर्शाता है।",
        "ಕನ್ನಡ": "<strong>ಮಾದರಿ ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ</strong>: ದಾಖಲಾತಿಯ ಸಮಯದಲ್ಲಿ ಸಾಮಾನ್ಯ HbA1c ಪರೀಕ್ಷಾ ಫಲಿತಾಂಶ ದಾಖಲಾಗಿದ್ದು, ಗ್ಲೈಸೆಮಿಕ್ ಸ್ಥಿರತೆಯನ್ನು ಸೂಚಿಸುತ್ತದೆ.",
    },
    "a1c_missing": {
        "English": "<strong>Missing lab documentation</strong>: No inpatient HbA1c laboratory test was recorded in the EHR for this admission, leaving recent long-term glycemic control unmeasured in the billing record.",
        "हिन्दी": "<strong>अनुपलब्ध लैब रिकॉर्ड</strong>: इस प्रवेश के लिए EHR में कोई HbA1c परीक्षण दर्ज नहीं किया गया था, जिससे दीर्घकालिक ग्लूकोज नियंत्रण रिकॉर्ड में मापा नहीं गया।",
        "ಕನ್ನಡ": "<strong>ಲಭ್ಯವಿಲ್ಲದ ಲ್ಯಾಬ್ ದಾಖಲೆ</strong>: ಈ ದಾಖಲಾತಿಗೆ ಯಾವುದೇ HbA1c ಲ್ಯಾಬ್ ಪರೀಕ್ಷೆ ದಾಖಲಾಗಿಲ್ಲ, ಇದರಿಂದ ದೀರ್ಘಕಾಲೀನ ಗ್ಲೂಕೋಸ್ ನಿಯಂತ್ರಣ ಅಳೆಯಲಾಗಿಲ್ಲ.",
    },
    "glu_pos": {
        "English": "<strong>Recorded lab marker</strong>: Documented acute blood glucose surge (<strong>{glucose} mg/dL</strong>) during hospitalization, associated with acute glycemic dysregulation.",
        "हिन्दी": "<strong>दर्ज लैब मार्कर</strong>: अस्पताल में भर्ती के दौरान तीव्र रक्त शर्करा वृद्धि (<strong>{glucose} mg/dL</strong>) दर्ज की गई, जो तीव्र ग्लूकोज असंतुलन से जुड़ी है।",
        "ಕನ್ನಡ": "<strong>ದಾಖಲಾದ ಲ್ಯಾಬ್ ಗುರುತು</strong>: ಆಸ್ಪತ್ರೆ ವಾಸ್ತವ್ಯದ ಸಮಯದಲ್ಲಿ ತೀವ್ರ ರಕ್ತದ ಗ್ಲೂಕೋಸ್ ಹೆಚ್ಚಳ (<strong>{glucose} mg/dL</strong>) ದಾಖಲಾಗಿದೆ.",
    },

    # Primary Diagnosis
    "diag_pos": {
        "English": "<strong>Supports higher score</strong>: Primary diagnostic category was recorded as <strong>{diag}</strong>.",
        "हिन्दी": "<strong>उच्च स्कोर का समर्थन करता है</strong>: प्राथमिक नैदानिक श्रेणी <strong>{diag}</strong> के रूप में दर्ज की गई थी।",
        "ಕನ್ನಡ": "<strong>ಹೆಚ್ಚಿನ ಸ್ಕೋರ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ</strong>: ಪ್ರಾಥಮಿಕ ರೋಗನಿರ್ಣಯ ವರ್ಗವನ್ನು <strong>{diag}</strong> ಎಂದು ದಾಖಲಿಸಲಾಗಿದೆ.",
    },
    "diag_neg": {
        "English": "<strong>Lowers model score</strong>: Primary diagnostic category was recorded as <strong>{diag}</strong>, which carries a negative statistical association in the model.",
        "हिन्दी": "<strong>मॉडल स्कोर कम करता है</strong>: प्राथमिक नैदानिक श्रेणी <strong>{diag}</strong> के रूप में दर्ज की गई थी, जो मॉडल में नकारात्मक सांख्यिकीय संबंध रखती है।",
        "ಕನ್ನಡ": "<strong>ಮಾದರಿ ಸ್ಕೋರ್ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ</strong>: ಪ್ರಾಥಮಿಕ ರೋಗನಿರ್ಣಯ ವರ್ಗವನ್ನು <strong>{diag}</strong> ಎಂದು ದಾಖಲಿಸಲಾಗಿದೆ, ಇದು ಮಾದರಿಯಲ್ಲಿ ಋಣಾತ್ಮಕ ಸಂಬಂಧವನ್ನು ಹೊಂದಿದೆ.",
    },
    "diag_neutral": {
        "English": "<strong>Recorded primary diagnosis</strong>: Primary clinical condition was categorized as <strong>{diag}</strong>.",
        "हिन्दी": "<strong>दर्ज प्राथमिक निदान</strong>: प्राथमिक नैदानिक स्थिति को <strong>{diag}</strong> के रूप में वर्गीकृत किया गया था।",
        "ಕನ್ನಡ": "<strong>ದಾಖಲಾದ ಪ್ರಾಥಮಿಕ ರೋಗನಿರ್ಣಯ</strong>: ಪ್ರಾಥಮಿಕ ಕ್ಲಿನಿಕಲ್ ಸ್ಥಿತಿಯನ್ನು <strong>{diag}</strong> ಎಂದು ವರ್ಗೀಕರಿಸಲಾಗಿದೆ.",
    },
    "diag_missing": {
        "English": "<strong>Data documentation</strong>: Primary diagnosis was unclassified or missing in billing records for this encounter.",
        "हिन्दी": "<strong>डेटा दस्तावेज़ीकरण</strong>: इस एनकाउंटर के लिए बिलिंग रिकॉर्ड में प्राथमिक निदान अवर्गीकृत या गायब था।",
        "ಕನ್ನಡ": "<strong>ಡೇಟಾ ದಾಖಲಾತಿ</strong>: ಈ ದಾಖಲಾತಿಗೆ ಬಿಲ್ಲಿಂಗ್ ದಾಖಲೆಗಳಲ್ಲಿ ಪ್ರಾಥಮಿಕ ರೋಗನಿರ್ಣಯವು ಅನಿರ್ದಿಷ್ಟವಾಗಿದೆ ಅಥವಾ ಲಭ್ಯವಿಲ್ಲ.",
    },
}

SUMMARY_FOLLOWUP = {
    "fu_insulin": {
        "English": "review recent inpatient insulin titration ({action} during stay) and reconcile administration schedules with the patient or caregiver",
        "हिन्दी": "अस्पताल में हाल ही में किए गए इंसुलिन समायोजन (रहने के दौरान {action}) की समीक्षा करें और रोगी या देखभालकर्ता के साथ समय सारिणी का समन्वय करें",
        "ಕನ್ನಡ": "ಆಸ್ಪತ್ರೆಯ ಇತ್ತೀಚಿನ ಇನ್ಸುಲಿನ್ ಹೊಂದಾಣಿಕೆಯನ್ನು (ವಾಸ್ತವ್ಯದಲ್ಲಿ {action}) ಪರಿಶೀಲಿಸಿ ಮತ್ತು ರೋಗಿ ಅಥವಾ ಆರೈಕೆದಾರರೊಂದಿಗೆ ವೇಳಾಪಟ್ಟಿಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ",
    },
    "fu_chg": {
        "English": "review modifications made to the diabetes medication regimen during this admission and confirm patient understanding",
        "हिन्दी": "इस प्रवेश के दौरान मधुमेह दवा व्यवस्था में किए गए संशोधनों की समीक्षा करें और रोगी की समझ की पुष्टि करें",
        "ಕನ್ನಡ": "ಈ ದಾಖಲಾತಿಯ ಸಮಯದಲ್ಲಿ ಮಧುಮೇಹ ಔಷಧಿ ನಿಯಮಾವಳಿಯಲ್ಲಿ ಮಾಡಿದ ಬದಲಾವಣೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ರೋಗಿಯ ತಿಳುವಳಿಕೆಯನ್ನು ದೃಢೀಕರಿಸಿ",
    },
    "fu_polypharmacy": {
        "English": "conduct structured medication reconciliation for the {meds} prescribed medications to review complexity and assess potential adherence barriers",
        "हिन्दी": "जटिलता की समीक्षा करने और संभावित अनुपालन बाधाओं का आकलन करने के लिए निर्धारित {meds} दवाओं के लिए संरचित दवा समाधान का संचालन करें",
        "ಕನ್ನಡ": "ಸಂಕೀರ್ಣತೆಯನ್ನು ಪರಿಶೀಲಿಸಲು ಮತ್ತು ಸಂಭಾವ್ಯ ಅಡೆತಡೆಗಳನ್ನು ನಿರ್ಣಯಿಸಲು ನಿಗದಿತ {meds} ಔಷಧಿಗಳ ವ್ಯವಸ್ಥಿತ ಪರಿಶೀಲನೆ ನಡೆಸಿ",
    },
    "fu_util_frequent": {
        "English": "evaluate eligibility for proactive care-coordinator outreach within 48-72 hours given the history of repeated acute visits ({inpatient} inpatient, {emergency} emergency in the past year)",
        "हिन्दी": "बार-बार तीव्र दौरों ({inpatient} अस्पताल दाखिले, {emergency} आपातकालीन दौरे) के इतिहास को देखते हुए 48-72 घंटों के भीतर सक्रिय देखभाल-समन्वयक आउटरीच की पात्रता का मूल्यांकन करें",
        "ಕನ್ನಡ": "ಮರುಕಳಿಸಿದ ತುರ್ತು ಭೇಟಿಗಳ ({inpatient} ಒಳರೋಗಿ, {emergency} ತುರ್ತು) ಇತಿಹಾಸವನ್ನು ಗಮನದಲ್ಲಿಟ್ಟುಕೊಂಡು 48-72 ಗಂಟೆಗಳಲ್ಲಿ ಕಾಳಜಿ ಸಂಯೋಜಕರ ಸಂಪರ್ಕದ ಅರ್ಹತೆಯನ್ನು ಪರಿಶೀಲಿಸಿ",
    },
    "fu_util_single": {
        "English": "verify that post-discharge outpatient contact information and discharge instructions are confirmed prior to departure",
        "हिन्दी": "सत्यापित करें कि डिस्चार्ज के बाद बाह्यरोगी संपर्क जानकारी और डिस्चार्ज निर्देश प्रस्थान से पहले पुष्ट किए गए हैं",
        "ಕನ್ನಡ": "ಡಿಸ್ಚಾರ್ಜ್ ನಂತರದ ಹೊರರೋಗಿ ಸಂಪರ್ಕ ವಿವರಗಳು ಮತ್ತು ಸೂಚನೆಗಳನ್ನು ನಿರ್ಗಮನಕ್ಕೆ ಮುಂಚಿತವಾಗಿ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ",
    },
    "fu_a1c_missing": {
        "English": "note that inpatient HbA1c was not documented; the team may consider outpatient glycemic testing during subsequent primary care follow-up",
        "हिन्दी": "ध्यान दें कि अस्पताल में HbA1c दर्ज नहीं किया गया था; टीम बाद के प्राथमिक देखभाल अनुवर्ती के दौरान बाह्यरोगी परीक्षण पर विचार कर सकती है",
        "ಕನ್ನಡ": "ಆಸ್ಪತ್ರೆಯಲ್ಲಿ HbA1c ದಾಖಲಾಗಿಲ್ಲ ಎಂಬುದನ್ನು ಗಮನಿಸಿ; ಮುಂದಿನ ಪ್ರಾಥಮಿಕ ಆರೈಕೆ ಭೇಟಿಯಲ್ಲಿ ಹೊರರೋಗಿ ಪರೀಕ್ಷೆಯನ್ನು ಪರಿಗಣಿಸಬಹುದು",
    },
    "fu_a1c_elevated": {
        "English": "coordinate outpatient endocrine or primary care follow-up to address elevated HbA1c ({a1c}%)",
        "हिन्दी": "बढ़े हुए HbA1c ({a1c}%) को नियंत्रित करने के लिए बाह्यरोगी एंडोक्राइन या प्राथमिक देखभाल अनुवर्ती का समन्वय करें",
        "ಕನ್ನಡ": "ಹೆಚ್ಚಿನ HbA1c ({a1c}%) ನಿಯಂತ್ರಣಕ್ಕಾಗಿ ಹೊರರೋಗಿ ಎಂಡೋಕ್ರೈನ್ ಅಥವಾ ಪ್ರಾಥಮಿಕ ಆರೈಕೆ ಭೇಟಿಯನ್ನು ಸಂಯೋಜಿಸಿ",
    },
    "fu_glucose_surge": {
        "English": "review post-discharge blood glucose monitoring plans following documented acute glucose elevation ({glucose} mg/dL)",
        "हिन्दी": "दर्ज तीव्र ग्लूकोज वृद्धि ({glucose} mg/dL) के बाद डिस्चार्ज उपरांत रक्त शर्करा निगरानी योजनाओं की समीक्षा करें",
        "ಕನ್ನಡ": "ದಾಖಲಾದ ತೀವ್ರ ಗ್ಲೂಕೋಸ್ ಹೆಚ್ಚಳದ ({glucose} mg/dL) ನಂತರ ಡಿಸ್ಚಾರ್ಜ್ ನಂತರದ ರಕ್ತದ ಗ್ಲೂಕೋಸ್ ಮೇಲ್ವಿಚಾರಣಾ ಯೋಜನೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ",
    },
    "fu_extended_stay": {
        "English": "assess home support readiness following the extended hospital stay of {days} days",
        "हिन्दी": "{days} दिनों के लंबे अस्पताल प्रवास के बाद गृह सहायता तत्परता का आकलन करें",
        "ಕನ್ನಡ": "{days} ದಿನಗಳ ದೀರ್ಘಾವಧಿಯ ಆಸ್ಪತ್ರೆ ವಾಸ್ತವ್ಯದ ನಂತರ ಮನೆಯ ಆರೈಕೆ ಸಿದ್ಧತೆಯನ್ನು ನಿರ್ಣಯಿಸಿ",
    },
    "fu_fallback_high": {
        "English": "prioritize early multidisciplinary discharge planning and confirm a primary care follow-up visit within 7 days",
        "हिन्दी": "प्रारंभिक बहु-विषयक डिस्चार्ज योजना को प्राथमिकता दें और 7 दिनों के भीतर प्राथमिक देखभाल अनुवर्ती यात्रा की पुष्टि करें",
        "ಕನ್ನಡ": "ಆರಂಭಿಕ ಬಹು-ವಿಭಾಗೀಯ ಡಿಸ್ಚಾರ್ಜ್ ಯೋಜನೆಯನ್ನು ಆದ್ಯತೆ ನೀಡಿ ಮತ್ತು 7 ದಿನಗಳಲ್ಲಿ ಪ್ರಾಥಮಿಕ ಆರೈಕೆ ಭೇಟಿಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ",
    },
    "fu_fallback_mod": {
        "English": "provide reinforced discharge education and confirm routine outpatient follow-up within 7-14 days",
        "हिन्दी": "सुदृढ़ डिस्चार्ज शिक्षा प्रदान करें और 7-14 दिनों के भीतर नियमित बाह्यरोगी अनुवर्ती की पुष्टि करें",
        "ಕನ್ನಡ": "ಸೂಕ್ತ ಡಿಸ್ಚಾರ್ಜ್ ಶಿಕ್ಷಣವನ್ನು ನೀಡಿ ಮತ್ತು 7-14 ದಿನಗಳಲ್ಲಿ ನಿಯಮಿತ ಹೊರರೋಗಿ ಆರೈಕೆಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ",
    },
    "fu_fallback_low": {
        "English": "proceed with standard discharge instructions and scheduled routine primary care follow-up",
        "हिन्दी": "मानक डिस्चार्ज निर्देशों और निर्धारित नियमित प्राथमिक देखभाल अनुवर्ती के साथ आगे बढ़ें",
        "ಕನ್ನಡ": "ಪ್ರಮಾಣಿತ ಡಿಸ್ಚಾರ್ಜ್ ಸೂಚನೆಗಳು ಮತ್ತು ನಿಗದಿತ ವಾಡಿಕೆಯ ಪ್ರಾಥಮಿಕ ಆರೈಕೆಯೊಂದಿಗೆ ಮುಂದುವರಿಯಿರಿ",
    },
}

SUMMARY_WRAPPERS = {
    "single": {
        "English": "The clinical team might consider evaluating whether to {opt}. This represents a discretionary workflow option rather than a validated clinical treatment directive.",
        "हिन्दी": "क्लिनिकल टीम विचार कर सकती है कि क्या {opt}। यह एक वैकल्पिक वर्कफ़्लो विकल्प है, मान्य चिकित्सीय उपचार निर्देश नहीं।",
        "ಕನ್ನಡ": "ಕ್ಲಿನಿಕಲ್ ತಂಡವು {opt} ಎಂಬುದನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡುವುದನ್ನು ಪರಿಗಣಿಸಬಹುದು. ಇದು ವಿವೇಚನಾಶೀಲ ಕಾರ್ಯವಿಧಾನದ ಆಯ್ಕೆಯಾಗಿದ್ದು, ವೈದ್ಯಕೀಯ ಚಿಕಿತ್ಸಾ ನಿರ್ದೇಶನವಲ್ಲ.",
    },
    "multi": {
        "English": "Potential considerations for the care team include deciding whether to {opts}. These represent discretionary workflow options rather than validated clinical treatment directives.",
        "हिन्दी": "देखभाल टीम के लिए संभावित विचारों में यह तय करना शामिल है कि क्या {opts}। ये वैकल्पिक वर्कफ़्लो विकल्प हैं, मान्य चिकित्सीय उपचार निर्देश नहीं।",
        "ಕನ್ನಡ": "ಆರೈಕೆ ತಂಡದ ಸಂಭಾವ್ಯ ಪರಿಶೀಲನೆಗಳಲ್ಲಿ {opts} ಎಂಬುದನ್ನು ನಿರ್ಧರಿಸುವುದು ಸೇರಿದೆ. ಇವು ವಿವೇಚನಾಶೀಲ ಆಯ್ಕೆಗಳಾಗಿದ್ದು, ವೈದ್ಯಕೀಯ ಚಿಕಿತ್ಸಾ ನಿರ್ದೇಶನಗಳಲ್ಲ.",
    },
    "conjunction": {
        "English": "; and ",
        "हिन्दी": "; और ",
        "ಕನ್ನಡ": "; ಮತ್ತು ",
    },
}

SUMMARY_DISCLAIMER = {
    "English": "*(Algorithmic decision support summary based on statistical association estimates. Does not indicate medical causation and should not replace independent clinical evaluation.)*",
    "हिन्दी": "*(सांख्यिकीय संबंध अनुमानों पर आधारित एल्गोरिथम निर्णय समर्थन सारांश। चिकित्सीय कार्य-कारण का संकेत नहीं देता और स्वतंत्र नैदानिक मूल्यांकन का स्थान नहीं लेता।)*",
    "ಕನ್ನಡ": "*(ಸಂಖ್ಯಾಶಾಸ್ತ್ರೀಯ ಸಂಬಂಧಗಳ ಆಧಾರದ ಮೇಲೆ ಅಲ್ಗಾರಿದಮಿಕ್ ನಿರ್ಧಾರ ಬೆಂಬಲ ಸಾರಾಂಶ. ವೈದ್ಯಕೀಯ ಕಾರಣವನ್ನು ಸೂಚಿಸುವುದಿಲ್ಲ ಮತ್ತು ಸ್ವತಂತ್ರ ಕ್ಲಿನಿಕಲ್ ಮೌಲ್ಯಮಾಪನವನ್ನು ಬದಲಾಯಿಸುವುದಿಲ್ಲ.)*",
}

ACTION_WORDS = {
    "escalated": {
        "English": "escalated",
        "हिन्दी": "बढ़ाई गई",
        "ಕನ್ನಡ": "ಹೆಚ್ಚಿಸಲಾಗಿದೆ",
    },
    "reduced": {
        "English": "reduced",
        "हिन्दी": "घटाई गई",
        "ಕನ್ನಡ": "ಕಡಿಮೆ ಮಾಡಲಾಗಿದೆ",
    },
}


# -----------------------------------------------------------------------------
# Translation Helper Functions
# -----------------------------------------------------------------------------

def t(key: str, lang: str = "English", **kwargs) -> str:
    """Fetches translated string by key with fallbacks and formatting."""
    lang_dict = UI_STRINGS.get(key, {})
    template = lang_dict.get(lang)
    if not template:
        template = lang_dict.get("English", key)
    if not template:
        template = key
    if kwargs:
        try:
            return template.format(**kwargs)
        except Exception:
            return template
    return template


def translate_tier(tier: str, lang: str = "English") -> str:
    """Translates model score tier string."""
    return TIER_TRANSLATIONS.get(tier, {}).get(lang, tier)


def translate_driver_label(driver_str: str, lang: str = "English") -> str:
    """Translates primary driver label for Outreach Queue table and patient profile."""
    if lang == "English":
        return driver_str

    if driver_str.startswith("Past Inpatient ("):
        visits = driver_str.replace("Past Inpatient (", "").replace(" visits)", "").replace(" visit)", "")
        if lang == "हिन्दी":
            return f"पूर्व भर्ती ({visits} दाखिले)"
        elif lang == "ಕನ್ನಡ":
            return f"ಹಿಂದಿನ ದಾಖಲಾತಿ ({visits} ಭೇಟಿಗಳು)"
    elif driver_str == "Recent Inpatient Admission (1 visit)":
        if lang == "हिन्दी":
            return "हाल ही में अस्पताल भर्ती (1 दाखिला)"
        elif lang == "ಕನ್ನಡ":
            return "ಇತ್ತೀಚಿನ ಆಸ್ಪತ್ರೆ ದಾಖಲಾತಿ (1 ಭೇಟಿ)"
    elif driver_str.startswith("Frequent ER Utilization ("):
        visits = driver_str.replace("Frequent ER Utilization (", "").replace(" visits)", "").replace(" visit)", "")
        if lang == "हिन्दी":
            return f"अक्सर आपातकालीन उपयोग ({visits} दौरे)"
        elif lang == "ಕನ್ನಡ":
            return f"ಆಗಾಗ್ಗೆ ತುರ್ತು ವಿಭಾಗ ಬಳಕೆ ({visits} ಭೇಟಿಗಳು)"
    elif driver_str.startswith("Past ER ("):
        visits = driver_str.replace("Past ER (", "").replace(" visits)", "").replace(" visit)", "")
        if lang == "हिन्दी":
            return f"पूर्व आपातकालीन ({visits} दौरे)"
        elif lang == "ಕನ್ನಡ":
            return f"ಹಿಂದಿನ ತುರ್ತು ({visits} ಭೇಟಿಗಳು)"
    elif driver_str.startswith("Insulin Instability ("):
        ins = driver_str.replace("Insulin Instability (", "").replace(")", "")
        if lang == "हिन्दी":
            return f"इंसुलिन अस्थिरता ({ins})"
        elif lang == "ಕನ್ನಡ":
            return f"ಇನ್ಸುಲಿನ್ ಅಸ್ಥಿರತೆ ({ins})"
    elif driver_str.startswith("Geriatric Vulnerability ("):
        bracket = driver_str.replace("Geriatric Vulnerability (", "").replace(")", "")
        if lang == "हिन्दी":
            return f"वृद्धावस्था संवेदनशीलता ({bracket})"
        elif lang == "ಕನ್ನಡ":
            return f"ಹಿರಿಯ ನಾಗರಿಕರ ದುರ್ಬಲತೆ ({bracket})"
    elif driver_str.startswith("Extended Hospital Stay ("):
        days = driver_str.replace("Extended Hospital Stay (", "").replace("d)", "").replace(" days)", "").replace(")", "")
        if lang == "हिन्दी":
            return f"लंबी अस्पताल अवधि ({days} दिन)"
        elif lang == "ಕನ್ನಡ":
            return f"ದೀರ್ಘಾವಧಿ ಆಸ್ಪತ್ರೆ ವಾಸ್ತವ್ಯ ({days} ದಿನಗಳು)"
    elif driver_str.startswith("Hospital Stay ("):
        days = driver_str.replace("Hospital Stay (", "").replace(" days)", "").replace(" day)", "")
        if lang == "हिन्दी":
            return f"अस्पताल अवधि ({days} दिन)"
        elif lang == "ಕನ್ನಡ":
            return f"ಆಸ್ಪತ್ರೆ ವಾಸ್ತವ್ಯ ({days} ದಿನಗಳು)"
    elif driver_str == "Medication Regimen Adjusted":
        if lang == "हिन्दी":
            return "दवा व्यवस्था में बदलाव"
        elif lang == "ಕನ್ನಡ":
            return "ಔಷಧಿ ಕ್ರಮ ಹೊಂದಿಸಲಾಗಿದೆ"
    elif driver_str == "High Polypharmacy (>20 meds)":
        if lang == "हिन्दी":
            return "अत्यधिक दवाएं (>20 दवाएं)"
        elif lang == "ಕನ್ನಡ":
            return "ಹೆಚ್ಚಿನ ಪಾಲಿಫಾರ್ಮಸಿ (>20 ಔಷಧಿಗಳು)"
    elif driver_str.startswith("Med Count ("):
        meds = driver_str.replace("Med Count (", "").replace(" meds)", "").replace(" med)", "")
        if lang == "हिन्दी":
            return f"दवाएं ({meds} दवाएं)"
        elif lang == "ಕನ್ನಡ":
            return f"ಔಷಧಿಗಳ ಸಂಖ್ಯೆ ({meds} ಔಷಧಿಗಳು)"
    elif driver_str == "Chronic Glycemic / Comorbid Burden":
        if lang == "हिन्दी":
            return "गंभीर ग्लाइसेमिक / सह-रुग्णता भार"
        elif lang == "ಕನ್ನಡ":
            return "ದೀರ್ಘಕಾಲಿಕ ಗ್ಲೈಸೆಮಿಕ್ / ಸಹ-ಅಸ್ವಸ್ಥತೆ ಹೊರೆ"
    elif driver_str.startswith("Age Bracket ("):
        bracket = driver_str.replace("Age Bracket (", "").replace(")", "")
        if lang == "हिन्दी":
            return f"आयु वर्ग ({bracket})"
        elif lang == "ಕನ್ನಡ":
            return f"ವಯಸ್ಸಿನ ವರ್ಗ ({bracket})"
    elif driver_str in ["Baseline Risk", "Baseline Clinical Risk"]:
        if lang == "हिन्दी":
            return "आधारभूत क्लिनिकल जोखिम"
        elif lang == "ಕನ್ನಡ":
            return "ಮೂಲ ಕ್ಲಿನಿಕಲ್ ಅಪಾಯ"

    return driver_str


def get_action_word(action_key: str, lang: str = "English") -> str:
    """Retrieves localized action descriptor."""
    return ACTION_WORDS.get(action_key, {}).get(lang, action_key)


def get_summary_tier_intro(tier_key: str, score_pct: float, tier_name: str, lang: str = "English") -> str:
    """Retrieves localized tier intro sentence for patient summary."""
    template = SUMMARY_TIER_INTRO.get(tier_key, {}).get(lang, SUMMARY_TIER_INTRO.get(tier_key, {}).get("English", ""))
    return template.format(score_pct=score_pct, tier=translate_tier(tier_name, lang))


def get_summary_context(context_key: str, inpatient: int, emergency: int, lang: str = "English") -> str:
    """Retrieves localized contextual sentence for patient summary."""
    template = SUMMARY_CONTEXT_SENTENCE.get(context_key, {}).get(lang, SUMMARY_CONTEXT_SENTENCE.get(context_key, {}).get("English", ""))
    return template.format(inpatient=inpatient, emergency=emergency)


def get_summary_factor(factor_key: str, lang: str = "English", **kwargs) -> str:
    """Retrieves localized factor bullet string for patient summary."""
    template = SUMMARY_FACTORS.get(factor_key, {}).get(lang, SUMMARY_FACTORS.get(factor_key, {}).get("English", ""))
    if kwargs:
        try:
            return template.format(**kwargs)
        except Exception:
            return template
    return template


def get_summary_followup(fu_key: str, lang: str = "English", **kwargs) -> str:
    """Retrieves localized follow-up clause for patient summary."""
    template = SUMMARY_FOLLOWUP.get(fu_key, {}).get(lang, SUMMARY_FOLLOWUP.get(fu_key, {}).get("English", ""))
    if kwargs:
        try:
            return template.format(**kwargs)
        except Exception:
            return template
    return template


def get_summary_followup_wrapped(considerations: List[str], lang: str = "English") -> str:
    """Wraps follow-up considerations in appropriate localized decision-support language."""
    if not considerations:
        return ""
    if len(considerations) == 1:
        template = SUMMARY_WRAPPERS["single"].get(lang, SUMMARY_WRAPPERS["single"]["English"])
        return template.format(opt=considerations[0])
    else:
        conj = SUMMARY_WRAPPERS["conjunction"].get(lang, "; and ")
        joined = conj.join(considerations[:2])
        template = SUMMARY_WRAPPERS["multi"].get(lang, SUMMARY_WRAPPERS["multi"]["English"])
        return template.format(opts=joined)


def get_summary_disclaimer(lang: str = "English") -> str:
    """Retrieves localized summary disclaimer."""
    return SUMMARY_DISCLAIMER.get(lang, SUMMARY_DISCLAIMER["English"])


def translate_adm_type(adm_id: str, lang: str = "English") -> str:
    """Translates admission type ID into localized clinical label."""
    key = f"adm_type_{adm_id}"
    return t(key, lang) if key in UI_STRINGS else f"{adm_id} - Other"


def translate_adm_source(src_id: str, lang: str = "English") -> str:
    """Translates admission source ID into localized clinical label."""
    key = f"adm_src_{src_id}"
    return t(key, lang) if key in UI_STRINGS else f"{src_id} - Other"


def translate_med_option(opt: str, lang: str = "English") -> str:
    """Translates dosage regimen option ('No', 'Steady', 'Up', 'Down') into localized text."""
    key = f"med_opt_{opt.lower()}"
    return t(key, lang) if key in UI_STRINGS else opt
