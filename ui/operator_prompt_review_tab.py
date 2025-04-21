
import streamlit as st
import json
import os
import openai

from gpt_logic_evaluator import set_api_key

QUEUE_PATH = "outputs/operator_prompt_queue.json"

def operator_prompt_review_tab():
    st.title("🧠 Operator Agent — Routing Review")
    st.caption("View file suggestions and route them via GPT live.")

    if not os.path.exists(QUEUE_PATH):
        st.warning("No prompt queue found. Please run `operator_file_router.py` first.")
        return

    with open(QUEUE_PATH, "r", encoding="utf-8") as f:
        prompts = json.load(f)

    set_api_key()

    for i, item in enumerate(prompts):
        st.markdown(f"### 📄 File: `{item['file']}`")
        st.markdown(f"**📂 Path:** `{item['path']}`")
        st.markdown("**🧠 Routing Prompt Preview:**")
        st.code(item["prompt"][:1000] + "\n\n... [truncated]", language="text")

        if st.button(f"🧠 Send to GPT: {item['file']}", key=f"send_gpt_{i}"):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a file router for a GPT-driven assistant."},
                        {"role": "user", "content": item["prompt"]}
                    ],
                    temperature=0.3
                )
                output = response["choices"][0]["message"]["content"]
                st.success("✅ GPT Response:")
                st.code(output, language="json")
            except Exception as e:
                st.error(f"❌ GPT call failed: {e}")

        st.markdown("---")
