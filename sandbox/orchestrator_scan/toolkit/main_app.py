import streamlit as st
import os

try:
    from pages import tab_flowstack_tracker, tab_flowstack_visual
except ImportError:
    import tab_flowstack_tracker
    import tab_flowstack_visual

st.set_page_config(page_title="FlowStack Control Hub", layout="wide")
st.title("🧠 FlowStack Intelligence System")

tab1, tab2 = st.tabs(["📊 Tracker Table", "📍 Visual Map"])

with tab1:
    tab_flowstack_tracker.run_ui()

with tab2:
    tab_flowstack_visual.run_ui()

st.markdown("---")
st.caption("FlowStack v5.0.0 · Managed by GPT automation · Synced with Notion & GitHub")
