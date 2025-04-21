
import streamlit as st
import pandas as pd
import os

TRACKER_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "fix_tracker.csv")

def load_tracker():
    if os.path.exists(TRACKER_PATH):
        return pd.read_csv(TRACKER_PATH)
    return pd.DataFrame(columns=["Project", "Fix_Status", "Last_Action", "Triggered_By", "Notes", "Last_Updated"])

def main():
    st.set_page_config(page_title="Fix Progress Summary", layout="wide")
    st.title("Fix Progress Tracker")

    df = load_tracker()
    if df.empty:
        st.info("No fix tracker entries found.")
        return

    st.markdown("### Filter by Status")
    filter_status = st.selectbox("Select Fix Status", ["All", "Pending", "In Progress", "Fixed"])

    if filter_status != "All":
        df = df[df["Fix_Status"] == filter_status]

    st.dataframe(df, use_container_width=True)

    st.markdown("### Summary Stats")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Pending", len(df[df['Fix_Status'] == 'Pending']))
    with col2:
        st.metric("In Progress", len(df[df['Fix_Status'] == 'In Progress']))
    with col3:
        st.metric("Fixed", len(df[df['Fix_Status'] == 'Fixed']))

if __name__ == "__main__":
    main()
