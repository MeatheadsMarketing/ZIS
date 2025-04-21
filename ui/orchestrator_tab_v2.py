
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import openai
import zipfile
import shutil
from pathlib import Path
from gpt_recovery_flow_engine import recover_and_register, export_tool_zip
from gpt_logic_evaluator import set_api_key

def orchestrator_tab():
    st.title("🧠 GPT Orchestrator v2")
    st.caption("Drop a ZIP, select a file, and let GPT analyze it for recovery actions.")

    scan_dir = "sandbox/orchestrator_scan"
    uploaded = st.file_uploader("Upload a ZIP archive for analysis", type="zip")

    if uploaded:
        if os.path.exists(scan_dir):
            shutil.rmtree(scan_dir)
        os.makedirs(scan_dir, exist_ok=True)

        zip_path = os.path.join(scan_dir, uploaded.name)
        with open(zip_path, "wb") as f:
            f.write(uploaded.read())

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(scan_dir)

        py_files = list(Path(scan_dir).rglob("*.py"))
        filenames = [str(p.name) for p in py_files]

        if not filenames:
            st.warning("No Python files found in archive.")
            return

        selected_name = st.selectbox("Select a Python file to scan with GPT", filenames)
        selected_path = next(p for p in py_files if p.name == selected_name)

        code = selected_path.read_text(encoding="utf-8", errors="ignore")
        st.markdown(f"### 📄 GPT will scan: `{selected_name}`")

        set_api_key()
        with st.spinner("🧠 GPT analyzing file..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a recovery assistant for GPT-driven systems."},
                    {"role": "user", "content": f"Analyze this file and suggest 3 recovery actions:\n\n{code[:3000]}"}
                ]
            )
            gpt_summary = response["choices"][0]["message"]["content"]

        st.markdown("### ✅ GPT Recovery Plan")
        st.success(gpt_summary)

        st.markdown("### 🔧 Execute Recovery")
        selected_action = st.selectbox("Choose Action", [
            "Run GPT Tags + Register", "Export Tools to ZIP", "Add Shortcut Triggers"
        ])
        selected_files = st.multiselect("Select Tools", filenames)

        if st.button("✅ Execute"):
            results = []
            if selected_action == "Run GPT Tags + Register":
                for f in selected_files:
                    results.append(recover_and_register(f, category="Orchestrated"))
            elif selected_action == "Export Tools to ZIP":
                results.append(export_tool_zip(selected_files, pack_name="OrchestratedPack"))
            elif selected_action == "Add Shortcut Triggers":
                results = [f"📎 Shortcut `#{f.replace('.py','').upper()}` would be created." for f in selected_files]

            for r in results:
                st.success(r)
