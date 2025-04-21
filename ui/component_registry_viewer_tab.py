
import streamlit as st
import pandas as pd
import os

REGISTRY_PATH = "registry/component_registry.csv"

def registry_viewer_tab():
    st.title("📋 Component Registry Viewer")
    st.caption("View and filter all registered tools, tags, and GPT metadata.")

    if not os.path.exists(REGISTRY_PATH):
        st.warning("Registry not found.")
        return

    df = pd.read_csv(REGISTRY_PATH)
    if df.empty:
        st.info("Registry is empty.")
        return

    st.markdown("### 🔍 Registry Snapshot")
    st.markdown(f"**Total Tools:** `{len(df)}`")
    st.markdown(f"**Launch-Ready:** `{len(df[df['Status'] == 'Launch-Ready'])}`")

    with st.expander("🔧 Filter Options"):
        tags = st.multiselect("Filter by Tag", df["Tags"].dropna().unique())
        statuses = st.multiselect("Filter by Status", df["Status"].dropna().unique())
        origin = st.multiselect("Filter by Origin", df["Origin"].dropna().unique())

        if tags:
            df = df[df["Tags"].isin(tags)]
        if statuses:
            df = df[df["Status"].isin(statuses)]
        if origin:
            df = df[df["Origin"].isin(origin)]

    st.dataframe(df, use_container_width=True)

    with st.expander("🧠 GPT Notes Viewer"):
        for _, row in df.iterrows():
            if row.get("GPT_Notes") and isinstance(row["GPT_Notes"], str) and len(row["GPT_Notes"]) > 20:
                st.markdown(f"**🧠 {row['Component']}** — *{row['Tags']}*")
                st.info(row["GPT_Notes"])
                st.markdown("---")

    if st.button("📤 Export Filtered View to CSV"):
        out_path = "outputs/registry_snapshot.csv"
        df.to_csv(out_path, index=False)
        st.success(f"Saved to `{out_path}`")
