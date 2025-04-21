
import streamlit as st
import os
import json

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")

def load_projects():
    return [f for f in os.listdir(REPORTS_DIR) if os.path.isdir(os.path.join(REPORTS_DIR, f))]

def load_report(project_name):
    report_path = os.path.join(REPORTS_DIR, project_name, "audit_report.md")
    if not os.path.exists(report_path):
        return "No report found."
    with open(report_path, "r", encoding="utf-8") as f:
        return f.read()

def load_json(project_name):
    log_path = os.path.join(REPORTS_DIR, project_name, "audit_log.json")
    if not os.path.exists(log_path):
        return {}
    with open(log_path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    st.set_page_config(page_title="Streamlit Audit Dashboard", layout="wide")
    st.title("Streamlit Audit Inspector v5")

    projects = load_projects()
    selected_project = st.sidebar.selectbox("Select a Build", projects)

    st.sidebar.markdown("### Actions")
    if st.sidebar.button("Re-Audit"):
        os.system(f"python run_audit.py --target ../streamlit_failed_builds/{selected_project}")
        st.success("Re-audit triggered. Refresh to see updated results.")

    if st.sidebar.button("Launch Streamlit Preview"):
        st.warning("Launching Streamlit app in background...")
        os.system(f"streamlit run ../streamlit_failed_builds/{selected_project}/main_app.py &")

    # Show markdown report
    st.subheader(f"Audit Report: `{selected_project}`")
    st.markdown(load_report(selected_project), unsafe_allow_html=True)

    # Show JSON summary
    with st.expander("Raw Audit Log (JSON)", expanded=False):
        st.json(load_json(selected_project))

if __name__ == "__main__":
    main()
