
import streamlit as st
import os
import zipfile
import json
from datetime import datetime

TOOLS_DIR = "./RecoveredTools_Library_Categorized/"
OUTPUT_DIR = "./outputs/"

st.title("📦 Assistant Pack Builder")

tool_files = []
for root, _, files in os.walk(TOOLS_DIR):
    for file in files:
        if file.endswith(".py"):
            rel_path = os.path.join(root, file)
            tool_files.append(rel_path)

selected_tools = st.multiselect("Select tools to include in the assistant package:", tool_files)

package_name = st.text_input("Name your assistant package:", "assistant_bundle_v2.0")
generate = st.button("Generate Assistant ZIP")

if generate and selected_tools:
    zip_path = os.path.join(OUTPUT_DIR, f"{package_name}.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file_path in selected_tools:
            zipf.write(file_path, os.path.relpath(file_path, TOOLS_DIR))
    st.success(f"ZIP package created: {zip_path}")
