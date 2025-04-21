import streamlit as st
import openai
import os

st.set_page_config(page_title="🧪 GPT Board Tester", layout="wide")
st.title("🧪 Test All GPT Chat Boards")

openai.api_key = st.secrets["OPENAI_API_KEY"]

boards = [f"GPT Chat Board {i}" for i in range(1, 6)]
prompt = "Say: 'I am alive and functioning.'"

st.markdown("Testing prompt: `" + prompt + "`")

results = {}

if st.button("Run Test on All Boards"):
    for i, board in enumerate(boards, 1):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-1106-preview",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1
            )
            reply = response.choices[0].message.content
            results[board] = reply
        except Exception as e:
            results[board] = f"❌ ERROR: {e}"

    st.subheader("Results:")
    for board, result in results.items():
        st.markdown(f"**{board}:**")
        st.code(result)
