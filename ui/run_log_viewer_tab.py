
import streamlit as st
import pandas as pd
import os

def run_log_viewer_tab():
    st.title("📊 Run Log Tracker")
    st.caption("View assistant launch history and tool interaction logs.")

    logs_path = "logs/run_log.csv"
    if not os.path.exists(logs_path):
        st.warning("No run log file found yet.")
        return

    df = pd.read_csv(logs_path)
    if df.empty:
        st.info("Run log is currently empty.")
        return

    with st.expander("🔍 Filter by Component or Action"):
        search = st.text_input("Search logs")
        if search:
            df = df[df.apply(lambda row: search.lower() in str(row).lower(), axis=1)]

    st.dataframe(df, use_container_width=True)
