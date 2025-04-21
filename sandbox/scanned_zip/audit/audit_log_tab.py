import streamlit as st
import pandas as pd
import os

st.subheader("📑 Assistant Run Audit Log")

log_file = "assistant_log.csv"

if os.path.exists(log_file):
    df = pd.read_csv(log_file)
    st.dataframe(df, use_container_width=True)

    st.markdown("### 🔍 Filter by Tag")
    all_tags = set()
    for tag_str in df["Tags"].dropna():
        all_tags.update([tag.strip() for tag in tag_str.split(",")])
    all_tags = sorted(all_tags)

    selected_tags = st.multiselect("Select tag(s) to filter:", all_tags)

    if selected_tags:
        df_filtered = df[df["Tags"].str.contains("|".join(selected_tags), na=False)]
        st.dataframe(df_filtered, use_container_width=True)
else:
    st.warning("assistant_log.csv not found. Export at least one session log to view this report.")
