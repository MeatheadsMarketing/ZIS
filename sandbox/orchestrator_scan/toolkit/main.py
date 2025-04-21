# clarity_hack_engine_v1/main.py

import zipfile
import os
from pathlib import Path
import streamlit as st

from tools.scaffold_visualizer import visualize_structure
from tools.file_classifier import classify_files
from tools.gpt_explainer import explain_file
from tools.export_bundle import export_clarity_package
from tools.clarity_score import score_clarity
from tools.meta_index_builder import build_meta_index
from tools.timeline_mapper import generate_timeline
from tools.run_history_tracker import track_history
from tools.explain_all_mode import explain_all_files

# === Streamlit UI Entry Point ===
st.set_page_config(page_title="Clarity Hack Engine", layout="wide")
st.title("Clarity Hack Engine v1.0")

uploaded_file = st.file_uploader("Upload a Zip File to Analyze", type="zip")

if uploaded_file:
    with st.spinner("Extracting zip..."):
        zip_path = Path("temp_zip")
        zip_path.mkdir(exist_ok=True)
        with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
            zip_ref.extractall(zip_path)

    st.success("Zip Extracted. Building Visual Tree...")
    st.subheader("1. Folder Tree Overview")
    folder_html = visualize_structure(zip_path)
    st.components.v1.html(folder_html, height=500, scrolling=True)

    st.subheader("2. File Classification & Scoring")
    file_table = classify_files(zip_path)
    file_table = score_clarity(file_table)
    st.dataframe(file_table)

    st.subheader("3. System Timeline View")
    timeline_chart = generate_timeline(zip_path)
    st.altair_chart(timeline_chart, use_container_width=True)

    st.subheader("4. File Clarity Breakdown")
    selected_file = st.selectbox("Select a file for full clarity breakdown:", file_table['path'])

    if selected_file:
        clarity_result = explain_file(selected_file)
        st.markdown(clarity_result['summary'])

        if clarity_result['visual']:
            st.image(clarity_result['visual'], caption="Logic Map")

    st.subheader("5. Explain Entire Project")
    if st.button("Run Full Clarity Pass"):
        explain_all_files(zip_path)
        st.success("All files processed.")

    st.subheader("6. Export Clarity Bundle")
    meta_csv, meta_json = build_meta_index(file_table)
    history_log = track_history(file_table)
    st.download_button("Download Clarity Bundle", data=export_clarity_package(zip_path), file_name="clarity_package.zip")