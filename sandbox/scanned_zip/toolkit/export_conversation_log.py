import streamlit as st
import datetime

st.set_page_config(page_title="📁 Export Conversation", layout="wide")
st.title("📁 GPT Conversation Exporter")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show current chat history
st.subheader("🧠 Current Conversation")
if st.session_state.chat_history:
    for msg in st.session_state.chat_history:
        label = "You" if msg["role"] == "user" else "GPT"
        st.markdown(f"**{label}:** {msg['content']}")
else:
    st.info("No messages to export.")

# Export chat log
if st.session_state.chat_history:
    export_name = f"chat_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    md_content = ""
    for msg in st.session_state.chat_history:
        label = "You" if msg["role"] == "user" else "GPT"
        md_content += f"### {label}
{msg['content']}

"

    st.download_button("📥 Download Markdown", data=md_content, file_name=export_name, mime="text/markdown")
