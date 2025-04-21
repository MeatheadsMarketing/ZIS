import streamlit as st

st.set_page_config(page_title="🧠 Memory Inspector", layout="wide")
st.title("🧠 Session Memory Inspector")

if st.button("Clear Memory"):
    st.session_state.clear()
    st.success("🧹 Memory cleared.")

st.subheader("🔍 Current st.session_state Contents")
if st.session_state:
    for key in st.session_state:
        st.markdown(f"**{key}**")
        st.json(st.session_state[key])
else:
    st.info("No active session state found.")
