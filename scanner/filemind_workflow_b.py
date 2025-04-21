# filemind_workflow_b.py – Unified Workflow: Intelligence → Output → Export

import streamlit as st
import pandas as pd
import zipfile
import os
from pathlib import Path

st.set_page_config(page_title="🧠 FILEMIND Workflow B", layout="wide")
st.title("🧠 FILEMIND – Workflow B: Intelligence → Output → Export")

# Load registry
try:
    df = pd.read_csv("zip_registry.csv")
    st.success("✅ zip_registry.csv loaded")
except:
    st.warning("⚠️ Run Workflow A to generate registry first")
    st.stop()

# TEAM INTELLIGENCE
with st.expander("🧠 Auto Categorize + Simulate Summaries"):
    df["Categorized Role"] = df["Extension"].map({".csv": "Table", ".txt": "Note", ".md": "Markdown", ".json": "Data"}).fillna("Unknown")
    df["Categorized Intent"] = df["Routing"].fillna("Scan")
    st.dataframe(df[["Filename", "Categorized Role", "Categorized Intent"]], use_container_width=True)

    df["Summary"] = df["Categorized Role"].apply(lambda x: f"Auto-summary: file categorized as {x}")
    st.markdown("### 📋 Simulated File Summaries")
    st.dataframe(df[["Filename", "Summary"]])
    df.to_csv("zip_registry.csv", index=False)

# TEAM OUTPUT
with st.expander("📊 Confidence Scoring + Clustering"):
    def score(row):
        score = 50
        if row["Size (KB)"] > 500: score += 10
        if row["Categorized Intent"] in ["Scan", "Merge"]: score += 20
        if row.get("Manual Tags", "") != "": score += 10
        return min(score, 100)

    df["Confidence Score"] = df.apply(score, axis=1)
    df["Cluster Group"] = df["Categorized Intent"].apply(lambda x: f"Group-{x}")
    st.dataframe(df[["Filename", "Confidence Score", "Cluster Group"]], use_container_width=True)
    df.to_csv("zip_registry.csv", index=False)

# TEAM EXPORT
with st.expander("📦 Build Export Bundle"):
    bundle_name = st.text_input("Name your ZIP export", value="filemind_bundle.zip")
    bundle_path = Path(bundle_name)
    workspace = Path("filemind_zip_workspace/extracted")

    if st.button("📤 Create Bundle"):
        with zipfile.ZipFile(bundle_path, 'w') as zipf:
            for row in df.itertuples():
                fpath = workspace / row._asdict()["Relative Path"]
                if fpath.exists():
                    arcname = f"{row.Cluster_Group}/{row.Filename}"
                    zipf.write(fpath, arcname=arcname)
        st.success(f"✅ Bundle saved: {bundle_path}")
        st.download_button("Download Bundle", open(bundle_path, "rb").read(), file_name=bundle_name)