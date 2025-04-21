
import streamlit as st
import os
import json
from datetime import datetime

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")

def parse_audit_log(project):
    log_path = os.path.join(REPORTS_DIR, project, "audit_log.json")
    if not os.path.exists(log_path):
        return None

    try:
        with open(log_path, "r", encoding="utf-8") as f:
            log = json.load(f)

        return {
            "Project": project,
            "Structure": log.get("structure", {}).get("status", "N/A"),
            "Placeholders": "Yes" if log.get("placeholders", {}).get("status") == "FAIL" else "No",
            "UI Score": "Bad" if log.get("ui", {}).get("status") == "FAIL" else "Good",
            "Runtime OK": "Yes" if log.get("runtime", {}).get("status") == "PASS" else "No",
            "Manifest": log.get("manifest", {}).get("status", "N/A"),
            "Perf Issues": "Yes" if log.get("performance", {}).get("status") == "FAIL" else "No",
            "Last Audited": datetime.fromtimestamp(os.path.getmtime(log_path)).strftime("%Y-%m-%d %H:%M")
        }
    except:
        return None

def main():
    st.set_page_config(page_title="Multi-Project Audit View", layout="wide")
    st.title("Audit Control Tower – All Builds Overview")

    project_dirs = [d for d in os.listdir(REPORTS_DIR) if os.path.isdir(os.path.join(REPORTS_DIR, d))]
    audit_data = [parse_audit_log(p) for p in project_dirs]
    audit_data = [row for row in audit_data if row is not None]

    if audit_data:
        
    # Apply icons to audit statuses
    for row in audit_data:
        row["Structure"] = status_icon(row.get("Structure", ""))
        row["Placeholders"] = status_icon("FAIL" if row.get("Placeholders") == "Yes" else "PASS")
        row["UI Score"] = status_icon("FAIL" if row.get("UI Score") == "Bad" else "PASS")
        row["Runtime OK"] = status_icon("FAIL" if row.get("Runtime OK") == "No" else "PASS")
        row["Manifest"] = status_icon(row.get("Manifest", ""))
        row["Perf Issues"] = status_icon("FAIL" if row.get("Perf Issues") == "Yes" else "PASS")

    st.dataframe(audit_data, use_container_width=True)


from project_status import load_status, save_status

def status_icon(value):
    if value == "FAIL":
        return "❌"
    elif value == "PASS":
        return "✅"
    else:
        return "⚠️"


from assistant_registry import load_registry

registry_data = load_registry()

# Merge assistant info if available
for row in audit_data:
    code = row["Project"]
    if code in registry_data:
        row["Assistant Name"] = registry_data[code].get("Name", "")
        row["Use Case"] = registry_data[code].get("Use Case", "")

# Override tag if assistant registry has a known status
if code in registry_data:
    registry_status = registry_data[code].get("Status", "").strip()
    if registry_status in tag_options:
        row["Tag"] = registry_status
        status_data[code] = registry_status

    else:
        row["Assistant Name"] = ""
        row["Use Case"] = ""

import pandas as pd

status_data = load_status()
tag_options = ["Ready", "Fixable", "Placeholder Only", "Dead", "Untouched"]

# Allow tagging each project
for row in audit_data:
    current_tag = status_data.get(row["Project"], "Untouched")
    new_tag = st.selectbox(f"Tag for {row['Project']}", tag_options, index=tag_options.index(current_tag), key=row["Project"])
    if new_tag != current_tag:
        status_data[row["Project"]] = new_tag

save_status(status_data)

# Add tags to the dataframe view
for row in audit_data:
    row["Tag"] = status_data.get(row["Project"], "Untouched")

# Download CSV export
if st.button("Export as CSV"):
    df = pd.DataFrame(audit_data)
    csv_path = os.path.join(REPORTS_DIR, "audit_summary_export.csv")
    df.to_csv(csv_path, index=False)
    st.success(f"Exported to: {csv_path}")


# Filter by tag
st.sidebar.markdown("## Filter Projects by Tag")
selected_filter = st.sidebar.selectbox("Show only...", ["All"] + tag_options)

if selected_filter != "All":
    audit_data = [row for row in audit_data if row.get("Tag") == selected_filter]

# Show updated table after filtering

    # Apply icons to audit statuses
    for row in audit_data:
        row["Structure"] = status_icon(row.get("Structure", ""))
        row["Placeholders"] = status_icon("FAIL" if row.get("Placeholders") == "Yes" else "PASS")
        row["UI Score"] = status_icon("FAIL" if row.get("UI Score") == "Bad" else "PASS")
        row["Runtime OK"] = status_icon("FAIL" if row.get("Runtime OK") == "No" else "PASS")
        row["Manifest"] = status_icon(row.get("Manifest", ""))
        row["Perf Issues"] = status_icon("FAIL" if row.get("Perf Issues") == "Yes" else "PASS")

    st.dataframe(audit_data, use_container_width=True)

# Launch buttons for each row
st.subheader("Launch Tools")
for row in audit_data:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"**{row['Project']}** – Tag: `{row['Tag']}`")
    with col2:
        if st.button(f"▶️ Launch", key=f"launch_{row['Project']}"):
            os.system(f"streamlit run ../streamlit_failed_builds/{row['Project']}/main_app.py &")


    else:
        st.warning("No valid audit logs found in reports directory.")

if __name__ == "__main__":
    main()
