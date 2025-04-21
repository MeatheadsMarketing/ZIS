import streamlit as st
from ui_layer.vault_dashboard_tab import *

st.set_page_config(page_title="Assistant Vault", layout="wide")

st.sidebar.title("🔧 Assistant Launcher")
selected_tab = st.sidebar.radio("Choose a tab:", ["Vault Control"])

if selected_tab == "Vault Control":
    pass  # vault_dashboard_tab.py already handles logic when imported