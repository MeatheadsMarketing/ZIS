
import streamlit as st
import json
import os

OUTPUT_PATH = "outputs/operator_output.json"

def router_viewer_tab():
    st.title("📊 Operator Routing Log")
    st.caption("See how each file was routed by the GPT Operator system.")

    if not os.path.exists(OUTPUT_PATH):
        st.warning("No operator output found.")
        return

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        routed = json.load(f)

    for item in routed:
        st.markdown(f"### 📄 `{item['file']}`")
        st.markdown(f"- 📂 Path: `{item.get('path', 'N/A')}`")
        st.markdown(f"- 🧠 Suggested Route: `{item['route']}`")
        st.markdown(f"- 💬 Reason:")
        st.info(item["reason"])
        st.markdown("---")
