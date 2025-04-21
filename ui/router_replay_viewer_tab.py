
import streamlit as st
import os
import json

LOG_PATH = "outputs/router_replay_log.json"

def router_replay_viewer_tab():
    st.title("📋 Operator Replay History")
    st.caption("Review all files re-processed from GPT Operator decisions.")

    if not os.path.exists(LOG_PATH):
        st.warning("No replay log found.")
        return

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        log = json.load(f)

    log = sorted(log, key=lambda x: x.get("timestamp", ""), reverse=True)

    for entry in log:
        st.markdown(f"### 📄 `{entry['file']}`")
        st.markdown(f"- 🕒 Time: `{entry['timestamp']}`")
        st.markdown(f"- 🧠 Action: `{entry['action']}`")
        st.markdown(f"- 📍 Route: `{entry['route']}`")
        st.markdown(f"- 💬 Reason:")
        st.info(entry["reason"])
        st.markdown("---")
