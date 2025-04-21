
import streamlit as st
from pathlib import Path
import importlib.util
import sys

# Tab names and their corresponding script files
tabs = {
    "Audit Dashboard": "audit_dashboard_all.py",
    "Recovery Tab": "recovery_tab.py",
    "Fix Summary": "fix_summary_tab.py",
    "Deployment Finalizer": "deploy_tab.py"
}

st.set_page_config(page_title="Streamlit Audit Guard Launcher", layout="wide")
st.title("Streamlit Audit Guard v1.0 – Launcher")

# Sidebar navigation
selected_tab = st.sidebar.radio("Select a Module", list(tabs.keys()))

# Dynamic module loading
tab_script = Path(__file__).parent / tabs[selected_tab]
spec = importlib.util.spec_from_file_location(selected_tab, tab_script)
module = importlib.util.module_from_spec(spec)
sys.modules[selected_tab] = module
spec.loader.exec_module(module)

# Run the selected module's `main()` function
if hasattr(module, "main"):
    module.main()
else:
    st.error(f"The script '{tabs[selected_tab]}' does not define a `main()` function.")
