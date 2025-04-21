
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from ui.orchestrator_tab_v2 import orchestrator_tab
from ui.scan_zip_tab import scan_zip_tab
from ui.recovered_tools_launcher_tab import recovered_tools_launcher_tab
from ui.component_registry_viewer_tab import registry_viewer_tab
from ui.view_outputs_tab import view_outputs_tab
from ui.shortcut_registry_viewer_tab import shortcut_registry_viewer_tab
from ui.gpt_notes_viewer_tab import gpt_notes_viewer_tab
from ui.gpt_notes_timeline_tab import gpt_notes_timeline_tab
from ui.batch_gpt_scan_tab import batch_gpt_scan_tab
from ui.intelligence_sheet_tab import intelligence_sheet_tab
from ui.export_launcher_tab import export_launcher_tab
from ui.registry_autotagger_tab import registry_autotagger_tab
from ui.assistant_pack_builder_tab import assistant_pack_builder_tab
from ui.readme_generator_tab import readme_generator_tab
from ui.run_log_viewer_tab import run_log_viewer_tab
from ui.operator_prompt_review_tab import operator_prompt_review_tab
from ui.router_viewer_tab import router_viewer_tab
from ui.operator_replay_tab import operator_replay_tab
from ui.router_replay_viewer_tab import router_replay_viewer_tab

TABS = {
    "🧠 GPT Orchestrator": orchestrator_tab,
    "📦 Scan ZIP": scan_zip_tab,
    "🧠 Recovered Tools": recovered_tools_launcher_tab,
    "📋 Registry Viewer": registry_viewer_tab,
    "📊 Recovery Outputs": view_outputs_tab,
    "🧩 Shortcut Registry": shortcut_registry_viewer_tab,
    "🧠 GPT Notes": gpt_notes_viewer_tab,
    "🕘 GPT Notes Timeline": gpt_notes_timeline_tab,
    "💡 Batch GPT Scan": batch_gpt_scan_tab,
    "📝 Intelligence Sheet": intelligence_sheet_tab,
    "📦 Export Launcher": export_launcher_tab,
    "🧠 Auto-Tagger": registry_autotagger_tab,
    "📦 Assistant Pack Builder": assistant_pack_builder_tab,
    "📝 README Generator": readme_generator_tab,
    "📊 Run Log Tracker": run_log_viewer_tab,
    "🧠 Operator Review": operator_prompt_review_tab,
    "📊 Operator Log": router_viewer_tab,
    "🔁 Operator Replay": operator_replay_tab,
    "📋 Operator Replays": router_replay_viewer_tab
}

st.set_page_config(page_title="ZIP Intelligence System", layout="wide")

with st.sidebar:
    st.title("🧠 ZIP Intelligence System")
    st.markdown("**Living Space:** MasterFlow > ZIP_Intelligence_System")
    st.markdown("Recover, route, tag, and replay assistant logic with GPT orchestration.")
    selected_tab = st.radio("📂 Choose a Module", list(TABS.keys()))

TABS[selected_tab]()
