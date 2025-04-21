import streamlit as st
import pandas as pd

def load_flowstack_data():
    return pd.read_csv("flowstack_master_v5.csv")

def run_ui():
    st.title("FlowStack Intelligence Tracker")
    df = load_flowstack_data()

    st.sidebar.header("Filter Options")
    tool_type = st.sidebar.multiselect("Tool Type", options=df["Tool Type"].dropna().unique())
    system_membership = st.sidebar.multiselect("System Membership", options=df["System Membership"].dropna().unique())
    dev_status = st.sidebar.multiselect("Development Status", options=df["Development Status"].dropna().unique())

    filtered_df = df.copy()
    if tool_type:
        filtered_df = filtered_df[filtered_df["Tool Type"].isin(tool_type)]
    if system_membership:
        filtered_df = filtered_df[filtered_df["System Membership"].isin(system_membership)]
    if dev_status:
        filtered_df = filtered_df[filtered_df["Development Status"].isin(dev_status)]

    st.dataframe(filtered_df, use_container_width=True)

if __name__ == "__main__":
    run_ui()
