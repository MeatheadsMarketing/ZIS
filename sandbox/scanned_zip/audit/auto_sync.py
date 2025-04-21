import streamlit as st
import subprocess

@st.cache_data
def auto_sync_secrets():
    subprocess.run(["python", "config/notion_sync_keys.py"])