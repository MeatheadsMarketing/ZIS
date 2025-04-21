
import streamlit as st
import os
import zipfile
import shutil
import datetime

def scan_zip_tab():
    st.title("📦 Scan ZIP Archive")
    st.caption("Upload any ZIP archive to scan and extract assistant logic.")

    uploaded = st.file_uploader("Upload a .zip archive", type="zip")
    scan_dir = "sandbox/scanned_zip"

    if uploaded:
        os.makedirs(scan_dir, exist_ok=True)
        zip_path = os.path.join(scan_dir, f"scan_{datetime.datetime.now().isoformat()}.zip")

        with open(zip_path, "wb") as f:
            f.write(uploaded.read())

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(scan_dir)

        st.success(f"Archive extracted to: `{scan_dir}`")
        file_list = []
        for root, _, files in os.walk(scan_dir):
            for file in files:
                if file.endswith((".py", ".csv", ".md", ".json")):
                    file_list.append(os.path.join(root, file))
        if file_list:
            st.markdown("### 📂 Files Detected:")
            for f in file_list:
                st.markdown(f"- `{f}`")
        else:
            st.warning("No supported files (.py, .csv, .md, .json) found.")
