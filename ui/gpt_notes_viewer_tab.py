
import streamlit as st
import pandas as pd
import os

REGISTRY_PATH = "registry/component_registry.csv"

def gpt_notes_viewer_tab():
    st.title("🧠 GPT Notes Viewer")
    st.caption("View all GPT-generated insights from exported tools.")

    if not os.path.exists(REGISTRY_PATH):
        st.warning("component_registry.csv not found.")
        return

    df = pd.read_csv(REGISTRY_PATH)
    if "GPT_Notes" not in df.columns:
        st.info("No GPT notes recorded yet.")
        return

    df = df[df["GPT_Notes"].notna() & (df["GPT_Notes"].str.len() > 10)]
    st.markdown(f"### 🧠 Notes Found: `{len(df)}`")

    sort_method = st.radio("Sort Notes By", ["Component", "Tags", "Length"], horizontal=True)

    if sort_method == "Tags":
        df = df.sort_values(by="Tags")
    elif sort_method == "Length":
        df["NoteLength"] = df["GPT_Notes"].str.len()
        df = df.sort_values(by="NoteLength", ascending=False)

    for _, row in df.iterrows():
        st.markdown(f"#### 🧠 `{row['Component']}`\nTag: `{row['Tags']}` — Status: `{row['Status']}`")
        st.info(row["GPT_Notes"])
        st.markdown("---")

    if st.button("📤 Export All Notes to File"):
        export_path = "outputs/gpt_comments.md"
        with open(export_path, "w") as f:
            for _, row in df.iterrows():
                f.write(f"### {row['Component']} — {row['Tags']}\n{row['GPT_Notes']}\n\n---\n")
        st.success(f"Saved to `{export_path}`")
