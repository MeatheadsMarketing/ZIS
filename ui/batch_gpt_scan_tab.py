
import streamlit as st
import os
import pandas as pd
from gpt_logic_evaluator import set_api_key, gpt_analyze_script

def batch_gpt_scan_tab():
    st.title("💡 Batch GPT Scan")
    st.caption("Run GPT suggestions across all `.py` files in a selected tool category.")

    base_dir = "RecoveredTools_Library_Categorized"
    if not os.path.exists(base_dir):
        st.warning("No recovered tool directory found.")
        return

    categories = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
    selected_cat = st.selectbox("Choose Folder to Scan", categories)
    folder_path = os.path.join(base_dir, selected_cat)
    files = [f for f in os.listdir(folder_path) if f.endswith(".py")]

    set_api_key()

    result_log = []

    if st.button("🔁 Run GPT Scan"):
        with st.spinner("Running GPT across tools..."):
            for f in files:
                path = os.path.join(folder_path, f)
                with open(path, "r", encoding="utf-8", errors="ignore") as codefile:
                    code = codefile.read()
                response = gpt_analyze_script(code)
                result_log.append({
                    "Component": f,
                    "Folder": selected_cat,
                    "GPT_Notes": response
                })

        if result_log:
            df = pd.DataFrame(result_log)
            st.success("GPT Scan Complete.")
            st.dataframe(df)
            output_path = "outputs/gpt_suggestions_bulk.csv"
            df.to_csv(output_path, index=False)
            st.info(f"Saved: `{output_path}`")
