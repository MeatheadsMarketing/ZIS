
import streamlit as st
import os
import json

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")

def load_audit_logs(tag_filter="Fixable"):
    from project_status import load_status
    status_data = load_status()
    logs = []

    for project in os.listdir(REPORTS_DIR):
        project_dir = os.path.join(REPORTS_DIR, project)
        log_path = os.path.join(project_dir, "audit_log.json")
        if not os.path.exists(log_path):
            continue

        tag = status_data.get(project, "Untouched")
        if tag != tag_filter:
            continue

        try:
            with open(log_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                logs.append({"project": project, "log": data})
        except:
            continue

    return logs

def render_log(project, log):
    st.markdown(f"### {project}")
    issues_found = False

    for section, result in log.items():
        status = result.get("status", "UNKNOWN")
        if status == "FAIL":
            issues_found = True
            st.markdown(f"**{section.upper()} – FAIL**")
            for key, value in result.items():
                if key == "status":
                    continue
                st.markdown(f"**{key}**:")
                if isinstance(value, list):
                    for item in value:
                        st.code(item)
                elif isinstance(value, dict):
                    for k, v in value.items():
                        st.markdown(f"- {k}: `{v}`")
                else:
                    st.markdown(f"`{value}`")
            st.markdown("---")

    if not issues_found:
        st.success("No blocking issues found. This assistant may be ready to tag as 'Ready'.")


import pandas as pd
from datetime import datetime

TRACKER_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "fix_tracker.csv")

def load_tracker():
    if os.path.exists(TRACKER_PATH):
        return pd.read_csv(TRACKER_PATH)
    return pd.DataFrame(columns=["Project", "Fix_Status", "Last_Action", "Triggered_By", "Notes", "Last_Updated"])

def save_tracker(df):
    df.to_csv(TRACKER_PATH, index=False)

def update_tracker_ui(project):
    tracker = load_tracker()
    row = tracker[tracker["Project"] == project]

    default_status = row["Fix_Status"].values[0] if not row.empty else "Pending"
    default_notes = row["Notes"].values[0] if not row.empty else ""
    default_action = row["Last_Action"].values[0] if not row.empty else ""

    st.markdown(f"**Fix Tracking: {project}**")
    status = st.selectbox("Fix Status", ["Pending", "In Progress", "Fixed"], index=["Pending", "In Progress", "Fixed"].index(default_status), key=f"status_{project}")
    notes = st.text_area("Notes", value=default_notes, key=f"notes_{project}")
    action = st.text_input("Last Action Taken", value=default_action, key=f"action_{project}")
    trigger = st.text_input("Triggered By", value="#X", key=f"trigger_{project}")

    if st.button("Update Fix Log", key=f"update_{project}"):
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        updated = {
            "Project": project,
            "Fix_Status": status,
            "Last_Action": action,
            "Triggered_By": trigger,
            "Notes": notes,
            "Last_Updated": now
        }

        if project in tracker["Project"].values:
            tracker.loc[tracker["Project"] == project] = updated
        else:
            tracker = tracker.append(updated, ignore_index=True)

        save_tracker(tracker)
        st.success("Fix tracker updated.")

def main():
    st.set_page_config(page_title="Recovery Tab", layout="wide")
    st.title("Recovery Mode – Fix Your Assistants")

    logs = load_audit_logs(tag_filter="Fixable")

    if not logs:
        st.info("No Fixable assistants found.")
        return

    for entry in logs:
        render_log(entry["project"], entry["log"])
        update_tracker_ui(entry["project"])

if __name__ == "__main__":
    main()
