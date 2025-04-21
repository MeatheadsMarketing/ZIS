
import streamlit as st
import pandas as pd
import os

SHORTCUT_PATH = "shortcuts/shortcut_registry_batch_05.csv"

def shortcut_registry_viewer_tab():
    st.title("🧩 Shortcut Registry Viewer")
    st.caption("Review GPT-triggerable shortcuts registered to logic components.")

    if not os.path.exists(SHORTCUT_PATH):
        st.warning("No shortcut registry found.")
        return

    df = pd.read_csv(SHORTCUT_PATH)
    if df.empty:
        st.info("No shortcuts have been added yet.")
        return

    st.markdown(f"### 📎 Total Shortcuts: `{len(df)}`")
    df["Shortcut"] = df["Shortcut"].fillna("Untitled")
    df["Component"] = df["Component"].fillna("Unknown")

    with st.expander("🔍 Filter by Trigger or Tool"):
        shortcut_filter = st.text_input("Filter Shortcut Code")
        component_filter = st.text_input("Filter Component Name")

        if shortcut_filter:
            df = df[df["Shortcut"].str.contains(shortcut_filter, case=False)]
        if component_filter:
            df = df[df["Component"].str.contains(component_filter, case=False)]

    st.dataframe(df, use_container_width=True)

    if st.button("📤 Export Shortcut Table"):
        path = "outputs/shortcut_registry_snapshot.csv"
        df.to_csv(path, index=False)
        st.success(f"Exported to `{path}`")
