import streamlit as st

from ui_layer.vault_editor_tab import vault_editor_ui
from ui_layer.file_stripper import file_stripper_ui
from ui_layer.function_runner_tab import run_ui as function_runner_ui
from ui_layer.dag_builder_tab import run_ui as dag_builder_ui
from ui_layer.blueprint_viewer_tab import run_ui as blueprint_viewer_ui
from ui_layer.assistant_sorter_tab import run_ui as assistant_sorter_ui
from ui_layer.behavioral_dashboard_tab import run_ui as behavioral_dashboard_ui
from ui_layer.assistant_composer_tab import run_ui as assistant_composer_ui
from ui_layer.vault_lineage_tab import run_ui as vault_lineage_ui

st.set_page_config(page_title="Assistant Engine", layout="wide")
st.sidebar.title("🧠 Assistant Dev Menu")

tabs = [
    "🔐 Vault Control",
    "🛠️ File Stripper",
    "🧪 Function Runner",
    "🔗 DAG Builder",
    "📋 Blueprint Viewer",
    "🧠 Assistant Sorter",
    "📊 Behavioral Dashboard",
    "🧬 Assistant Composer",
    "🧠 Vault Lineage"
]

selected_tab = st.sidebar.radio("Select a tab:", tabs)

if selected_tab == "🔐 Vault Control":
    vault_editor_ui()
elif selected_tab == "🛠️ File Stripper":
    file_stripper_ui()
elif selected_tab == "🧪 Function Runner":
    function_runner_ui()
elif selected_tab == "🔗 DAG Builder":
    dag_builder_ui()
elif selected_tab == "📋 Blueprint Viewer":
    blueprint_viewer_ui()
elif selected_tab == "🧠 Assistant Sorter":
    assistant_sorter_ui()
elif selected_tab == "📊 Behavioral Dashboard":
    behavioral_dashboard_ui()
elif selected_tab == "🧬 Assistant Composer":
    assistant_composer_ui()
elif selected_tab == "🧠 Vault Lineage":
    vault_lineage_ui()
