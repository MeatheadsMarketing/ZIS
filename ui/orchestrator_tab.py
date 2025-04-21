
import streamlit as st
import openai
import os
import zipfile
import shutil
from pathlib import Path
from gpt_logic_evaluator import set_api_key, gpt_analyze_script

def orchestrator_tab():
    st.title("🧠 GPT Orchestrator")
    st.caption("Upload a ZIP, let GPT drive recovery, classification, and next steps.")

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

        py_files = [p for p in Path(scan_dir).rglob("*.py")]
        sample = ""
        for p in py_files:
            code = p.read_text(encoding="utf-8", errors="ignore")
            if len(code) > 50:
                sample = code[:3000]
                break

        if sample:
            set_api_key()
            with st.spinner("🧠 GPT is analyzing your ZIP contents..."):
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a recovery workflow planner and assistant logic designer."},
                        {"role": "user", "content": f"""Analyze this ZIP archive code snippet. What is the purpose of the logic inside? What are the top 3 actions the user should take next (e.g., classify, tag, export, bundle)? Respond in numbered steps with brief rationale.

CODE:
{sample}
"""}
                    ],
                    temperature=0.4
                )
                gpt_summary = response['choices'][0]['message']['content']
                st.markdown("### ✅ GPT Recovery Plan")
                st.success(gpt_summary)

                st.markdown("---")
                st.markdown("### 🚦 Choose One to Execute Now:")
                st.radio("Select:", ["Run GPT Tags + Register", "Export Tools to ZIP", "Add to Assistant Pack"], key="next_action")
                st.button("✅ Execute Selected Step (Coming Soon)")

        else:
            st.warning("No usable Python files found in the archive.")
