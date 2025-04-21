
import streamlit as st
import os
import json

from replay_logger import append_replay_log
from gpt_recovery_flow_engine import recover_and_register, export_tool_zip

REPLAY_PATH = "outputs/operator_output.json"

def operator_replay_tab():
    st.title("🔁 Operator Replay Trigger")
    st.caption("Re-run routed logic on files using GPT's previous suggestions.")

    if not os.path.exists(REPLAY_PATH):
        st.warning("No operator output found.")
        return

    with open(REPLAY_PATH, "r", encoding="utf-8") as f:
        routes = json.load(f)

    for entry in routes:
        st.markdown(f"### 📄 `{entry['file']}`")
        st.markdown(f"**🔁 GPT Suggested Route:** `{entry['route']}`")
        st.markdown(f"💬 Reason: {entry['reason']}")
        col1, col2 = st.columns(2)

        with col1:
            if st.button(f"🧠 Register via GPT → {entry['file']}", key=f"reg_{entry['file']}"):
                result = recover_and_register(entry["file"], category="Rerouted")
                st.success(result)
                append_replay_log(entry['file'], 'export', entry['route'], entry['reason'])
                append_replay_log(entry['file'], 'register', entry['route'], entry['reason'])

        with col2:
            if st.button(f"📦 Export ZIP → {entry['file']}", key=f"zip_{entry['file']}"):
                result = export_tool_zip([entry["file"]], pack_name="OperatorReplay")
                st.success(result)

        st.markdown("---")
