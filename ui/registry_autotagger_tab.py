
import streamlit as st
import os
import pandas as pd
import openai

from gpt_logic_evaluator import set_api_key, gpt_analyze_script

REGISTRY_PATH = "registry/component_registry.csv"

def registry_autotagger_tab():
    st.title("🧠 Registry Auto-Tagger")
    st.caption("Let GPT auto-fill missing tags and roles in your component registry.")

    if not os.path.exists(REGISTRY_PATH):
        st.warning("Registry file not found.")
        return

    df = pd.read_csv(REGISTRY_PATH)
    if "GPT_Notes" not in df.columns:
        df["GPT_Notes"] = ""
    if "Tags" not in df.columns:
        df["Tags"] = ""

    missing = df[df["Tags"].isna() | (df["Tags"] == "")]
    st.write("Entries missing tags:")
    st.dataframe(missing)

    set_api_key()
    updates = []

    if st.button("🔁 Run GPT Tag Enhancer"):
        for idx, row in missing.iterrows():
            notes = row["GPT_Notes"] or f"Tool name: {row['Component']}"
            response = gpt_analyze_script(notes)
            tag = "Unknown"
            for r in ["Cleaner", "Trigger", "Planner", "Auditor", "Utility"]:
                if r.lower() in response.lower():
                    tag = r
                    break
            df.at[idx, "Tags"] = tag
            df.at[idx, "GPT_Notes"] += f"\n[Auto-Tagged as: {tag}]"
            updates.append((row["Component"], tag))

        df.to_csv(REGISTRY_PATH, index=False)
        st.success(f"Auto-tagged {len(updates)} components.")
        for comp, tag in updates:
            st.markdown(f"✅ `{comp}` → **{tag}**")
