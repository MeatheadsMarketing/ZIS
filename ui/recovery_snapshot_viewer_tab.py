
import streamlit as st
import os
import json
from recovery_logger import log_recovery_snapshot

LOG_PATH = "outputs/recovery_flow_log.json"

def recovery_snapshot_viewer_tab():
    st.title("📜 Recovery Flow Snapshot")
    st.caption("View all past recovery sessions — and replay actions with one click.")

    if not os.path.exists(LOG_PATH):
        st.warning("No recovery logs available yet.")
        return

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        logs = json.load(f)

    logs = sorted(logs, key=lambda x: x.get("timestamp", ""), reverse=True)

    for idx, entry in enumerate(logs):
        zip_name = entry.get("zip_name")
        timestamp = entry.get("timestamp")
        files = entry.get("files_processed", [])
        registered = entry.get("registered_components", [])
        shortcuts = entry.get("shortcuts_added", [])
        gpt_summary = entry.get("gpt_summary", "N/A")
        duration = entry.get("duration", "N/A")

        st.markdown(f"### 🔁 `{zip_name}`")
        st.markdown(f"🕒 `{timestamp}` — ⏱ Duration: `{duration}`")
        st.markdown(f"📂 Files: `{', '.join(files)}`")

        with st.expander("🧠 GPT Summary"):
            st.info(gpt_summary)

        with st.expander("✅ Registered Components"):
            for comp in registered:
                st.markdown(f"- `{comp}`")

        with st.expander("🏷️ Shortcuts Added"):
            for s in shortcuts:
                st.markdown(f"- `{s}`")

        if st.button(f"▶️ Replay: Register Tools from Entry {idx}"):
            for comp in registered:
                log_recovery_snapshot(zip_name, [comp], gpt_summary, [comp], [])
            st.success(f"Replayed registration for: {', '.join(registered)}")

        if st.button(f"▶️ Replay: Shortcut Trigger for Entry {idx}"):
            for s in shortcuts:
                log_recovery_snapshot(zip_name, [s], gpt_summary, [], [s])
            st.success(f"Shortcut re-tagged: {', '.join(shortcuts)}")

        st.markdown("---")
