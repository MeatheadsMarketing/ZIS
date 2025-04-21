# filemind_workflow_a.py – Unified Workflow: Team Ingest, Registry, Detection

import streamlit as st
import zipfile, os, shutil
from pathlib import Path
import pandas as pd
import re

st.set_page_config(page_title="📂 FILEMIND Workflow A", layout="wide")
st.title("📂 FILEMIND – Workflow A: Ingest → Registry → Detection")

workspace = Path("filemind_zip_workspace/extracted")
workspace.mkdir(parents=True, exist_ok=True)

# TEAM INGEST
with st.expander("📤 Upload + Extract ZIP"):
    uploaded = st.file_uploader("Upload a .zip file", type="zip")
    if uploaded:
        zip_path = Path("filemind_zip_workspace") / uploaded.name
        with open(zip_path, "wb") as f: f.write(uploaded.read())
        with zipfile.ZipFile(zip_path, 'r') as zipf: zipf.extractall(workspace)
        st.success("ZIP extracted")
        for root, _, files in os.walk(workspace):
            for name in files:
                rel = os.path.relpath(os.path.join(root, name), workspace)
                size = os.path.getsize(os.path.join(root, name)) / 1024
                st.write(f"- `{rel}` ({size:.1f} KB)")

# TEAM REGISTRY
with st.expander("📑 File Registry + Sizing"):
    file_rows = []
    for root, _, files in os.walk(workspace):
        for name in files:
            full = Path(root) / name
            rel = full.relative_to(workspace)
            file_rows.append({
                "Filename": name,
                "Relative Path": str(rel),
                "Extension": full.suffix,
                "Size (KB)": round(full.stat().st_size / 1024, 2)
            })
    if file_rows:
        df = pd.DataFrame(file_rows)
        df["Size Tier"] = pd.cut(df["Size (KB)"], bins=[0,10,100,1000,10000,float('inf')], labels=["Tiny","Small","Medium","Large","Huge"])
        st.dataframe(df, use_container_width=True)
        df.to_csv("zip_registry.csv", index=False)
        st.success("zip_registry.csv saved")

# TEAM DETECTION
with st.expander("🔍 Detect Assistants + Shortcuts"):
    assistants, shortcuts = [], []
    assistant_pattern = re.compile(r"A\\d{4}|T-R-[A-Z\\-]+", re.IGNORECASE)
    shortcut_pattern = re.compile(r"#\\w+[\\-\\w]*")
    for row in df.itertuples():
        path = workspace / row._asdict()["Relative Path"]
        if path.suffix in [".txt", ".md", ".json"]:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
                    for m in set(assistant_pattern.findall(text)):
                        assistants.append({"File": row.Filename, "Ref": m})
                    for s in set(shortcut_pattern.findall(text)):
                        shortcuts.append({"File": row.Filename, "Shortcut": s})
            except: continue
    if assistants:
        st.subheader("🧩 Assistants Detected")
        st.dataframe(pd.DataFrame(assistants))
    if shortcuts:
        st.subheader("🏷️ Shortcuts Detected")
        st.dataframe(pd.DataFrame(shortcuts))