
import streamlit as st
import os
import pandas as pd
import openai

from gpt_logic_evaluator import set_api_key, gpt_analyze_script

REGISTRY_PATH = "registry/component_registry.csv"

def export_launcher_tab():
    st.title("📦 Export Launcher")
    st.caption("Bundle launch-ready tools into assistant packs or export-ready ZIPs.")

    if not os.path.exists(REGISTRY_PATH):
        st.warning("Registry not found.")
        return

    df = pd.read_csv(REGISTRY_PATH)
    launch_ready = df[df["Status"] == "Launch-Ready"]
    if launch_ready.empty:
        st.info("No launch-ready tools found.")
        return

    selected = st.multiselect("Select tools to bundle", launch_ready["Component"].tolist())
    pack_name = st.text_input("Bundle name", "assistant_bundle")
    export_dir = f"exports/{pack_name}"
    os.makedirs(export_dir, exist_ok=True)

    if st.button("💡 GPT Suggest Pack Tags"):
        set_api_key()
        notes = "\n".join(launch_ready["GPT_Notes"].fillna("")[:3].tolist())
        suggestion = gpt_analyze_script(notes)
        st.markdown("### GPT Suggestion:")
        st.info(suggestion)

    if st.button("📦 Build ZIP"):
        for file in selected:
            src_path = f"RecoveredTools_Library_Categorized/*/{file}"
            found = False
            for root, _, files in os.walk("RecoveredTools_Library_Categorized"):
                if file in files:
                    shutil.copy(os.path.join(root, file), os.path.join(export_dir, file))
                    found = True
                    break
            if not found:
                st.warning(f"{file} not found.")
        zip_name = f"{export_dir}.zip"
        shutil.make_archive(export_dir, "zip", export_dir)
        st.success(f"Exported: `{zip_name}`")
