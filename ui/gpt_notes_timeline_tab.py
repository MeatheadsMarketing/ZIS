
import streamlit as st
import os
import json
from pathlib import Path
import datetime

LOG_PATH = "outputs/gpt_notes_log.json"

def gpt_notes_timeline_tab():
    st.title("🕘 GPT Notes Timeline")
    st.caption("Chronologically review GPT notes logged during recovery and registration.")

    if not os.path.exists(LOG_PATH):
        st.warning("No GPT note log found yet.")
        return

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        logs = json.load(f)

    sorted_logs = sorted(logs, key=lambda x: x.get("timestamp", ""), reverse=True)

    for entry in sorted_logs:
        st.markdown(f"### 🔧 `{entry['component']}`")
        st.markdown(f"- 📂 Category: `{entry['origin']}`")
        st.markdown(f"- 🕒 Logged at: `{entry['timestamp']}`")
        st.markdown(f"- 🏷️ Role: `{entry['role']}`")
        st.info(entry["gpt_notes"])
        st.markdown("---")
