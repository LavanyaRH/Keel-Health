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
            "Bars indicate the exact mathematical contribution $(\\beta_i \\cdot x_i)$ of this encounter's features to the predicted probability. "
            "**Statistical associations do not imply medical causation.**"
        ),
        "हिन्दी": (
            "इस लॉजिस्टिक रिग्रेशन मॉडल के लिए, लॉग-ऑड्स रैखिक हैं: $\\text{logit}(p) = \\beta_0 + \\sum \\beta_i x_i$। "
            "बार अनुमानित संभावना में इस एनकाउंटर की विशेषताओं के सटीक गणितीय योगदान $(\\beta_i \\cdot x_i)$ को दर्शाते हैं। "
            "**सांख्यिकीय संबंध चिकित्सीय कार्य-कारण का संकेत नहीं देते हैं।**"
        ),
        "ಕನ್ನಡ": (
            "ಈ ಲಾಜಿಸ್ಟಿಕ್ ರಿಗ್ರೆಷನ್ ಮಾದರಿಗೆ, ಲಾಗ್-ಆಡ್ಸ್ ರೇಖೀಯವಾಗಿದೆ: $\\text{logit}(p) = \\beta_0 + \\sum \\beta_i x_i$. "
            "ಗ್ರಾಫ್‌ಗಳು ಅಂದಾಜು ಸಂಭವನೀಯತೆಗೆ ಈ ದಾಖಲಾತಿಯ ವೈಶಿಷ್ಟ್ಯಗಳ ನಿಖರವಾದ ಗಣಿತದ ಕೊಡುಗೆಯನ್ನು $(\\beta_i \\cdot x_i)$ ಸೂಚಿಸುತ್ತವೆ. "
            "**ಸಂಖ್ಯಾಶಾಸ್ತ್ರೀಯ ಸಂಬಂಧಗಳು ವೈದ್ಯಕೀಯ ಕಾರಣವನ್ನು ಸೂಚಿಸುವುದಿಲ್ಲ.**"
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
        "English": "##### 🔻 Top Risk-Reducing Factors $(\\beta_i x_i < 0)$",
        "हिन्दी": "##### 🔻 शीर्ष जोखिम कम करने वाले कारक $(\\beta_i x_i < 0)$",
        "ಕನ್ನಡ": "##### 🔻 ಅಪಾಯ ಕಡಿಮೆ ಮಾಡುವ ಪ್ರಮುಖ ಅಂಶಗಳು $(\\beta_i x_i < 0)$",
    },
    "neg_chart_xaxis": {
        "English": "Negative Log-Odds Impact (Protective)",
        "हिन्दी": "नकारात्मक लॉग-ऑड्स प्रभाव (सुरक्षात्मक)",
        "ಕನ್ನಡ": "ಋಣಾತ್ಮಕ ಲಾಗ್-ಆಡ್ಸ್ ಪ್ರಭಾವ (ರಕ್ಷಣಾತ್ಮಕ)",
    },
    "neg_empty_state": {
        "English": "No significant protective factors identified for this encounter.",
        "हिन्दी": "इस एनकाउंटर के लिए कोई महत्वपूर्ण सुरक्षात्मक कारक नहीं पाया गया।",
        "ಕನ್ನಡ": "ಈ ದಾಖಲಾತಿಗೆ ಯಾವುದೇ ಪ್ರಮುಖ ರಕ್ಷಣಾತ್ಮಕ ಅಂಶಗಳು ಕಂಡುಬಂದಿಲ್ಲ.",
    },
    "intercept_caption": {
        "English": "Base model intercept $(\\beta_0)$: `{val:.3f}`",
        "हिन्दी": "बेस मॉडल इंटरसेप्ट $(\\beta_0)$: `{val:.3f}`",
        "ಕನ್ನಡ": "ಮೂಲ ಮಾದರಿಯ ಇಂಟರ್‌ಸೆಪ್ಟ್ $(\\beta_0)$: `{val:.3f}`",
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
        "English": "The model identified predominantly protective indicators, led by zero recorded prior acute admissions and stable clinical features.",
        "हिन्दी": "मॉडल ने मुख्य रूप से सुरक्षात्मक संकेतकों की पहचान की है, जिसमें शून्य पूर्व दाखिले और स्थिर नैदानिक विशेषताएं प्रमुख हैं।",
        "ಕನ್ನಡ": "ಮಾದರಿಯು ಮುಖ್ಯವಾಗಿ ರಕ್ಷಣಾತ್ಮಕ ಅಂಶಗಳನ್ನು ಗುರುತಿಸಿದೆ, ಇದರಲ್ಲಿ ಹಿಂದಿನ ಶೂನ್ಯ ದಾಖಲಾತಿಗಳು ಮತ್ತು ಸ್ಥಿರ ಕ್ಲಿನಿಕಲ್ ಲಕ್ಷಣಗಳು ಸೇರಿವೆ.",
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
    template = lang_dict.get(lang, lang_dict.get("English", key))
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
