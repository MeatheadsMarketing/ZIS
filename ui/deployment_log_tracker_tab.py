
import streamlit as st
import json
import os
from datetime import datetime

LOG_PATH = "./outputs/deployment_log.json"

st.title("📜 Deployment Log Tracker")

if os.path.exists(LOG_PATH):
    with open(LOG_PATH, "r") as f:
        log_data = json.load(f)
else:
    log_data = []

st.write("### Logged Deployments")
for entry in log_data:
    st.json(entry)

new_entry = st.button("Log New Deployment")

if new_entry:
    new_record = {
        "timestamp": datetime.now().isoformat(),
        "event": "Assistant Export",
        "package_name": "assistant_bundle_v2.0.zip"
    }
    log_data.append(new_record)
    with open(LOG_PATH, "w") as f:
        json.dump(log_data, f, indent=2)
    st.success("Deployment logged.")
