
import streamlit as st
import os
import openai
from pathlib import Path

from gpt_logic_evaluator import set_api_key

def gpt_generate_questions(code_sample, model="gpt-4"):
    prompt = f"""You are building a dynamic recovery assistant. Based on the code below, generate the 5–10 most important clarifying questions a human user should answer before GPT proceeds to classify, tag, or register the tool. These should help GPT understand user intent, preferences, and context.

Respond only with a numbered list of questions.

CODE SAMPLE:
{code_sample}
"""
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a reasoning assistant builder."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )
    return response['choices'][0]['message']['content']

def gpt_finalize_with_answers(code_sample, user_answers, model="gpt-4"):
    prompt = f"""Based on the following script and user's answers to intelligence tuning questions, classify the script into a system role, assign tags, determine launch-readiness, and suggest a shortcut code.

SCRIPT:
{code_sample}

USER ANSWERS:
{user_answers}

Return your answer in 4 parts:
1. Final Role
2. Launch Readiness (Yes/No)
3. Tags (comma-separated)
4. Suggested Shortcut Code
"""
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a tool classification and assistant metadata engine."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )
    return response['choices'][0]['message']['content']

def intelligence_sheet_tab():
    st.title("📝 Intelligence Sheet Generator (Interactive)")
    st.caption("Let GPT generate an intelligence questionnaire based on scanned logic — then use your answers to finalize classification.")

    uploaded = st.file_uploader("Upload a ZIP archive", type="zip")
    scan_dir = "sandbox/intel_sheet_scan"

    if uploaded:
        import zipfile
        import shutil
        if os.path.exists(scan_dir):
            shutil.rmtree(scan_dir)
        os.makedirs(scan_dir, exist_ok=True)

        zip_path = os.path.join(scan_dir, uploaded.name)
        with open(zip_path, "wb") as f:
            f.write(uploaded.read())

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(scan_dir)

        py_files = [p for p in Path(scan_dir).rglob("*.py")]
        sample = ""
        for p in py_files:
            code = p.read_text(encoding="utf-8", errors="ignore")
            if len(code) > 100:
                sample = code[:3000]
                break

        if sample:
            set_api_key()
            st.markdown("### 🔍 GPT-Generated Intelligence Sheet Questions")
            questions = gpt_generate_questions(sample)
            st.markdown(questions)

            qlist = [q for q in questions.split("\n") if q.strip().startswith(tuple("1234567890"))]
            answers = []
            with st.form("answer_form"):
                for i, q in enumerate(qlist):
                    answer = st.text_input(f"{q}", key=f"ans_{i}")
                    answers.append(answer)
                submitted = st.form_submit_button("Submit Answers")

            if submitted:
                user_response = "\n".join([f"{qlist[i]}\n{answers[i]}" for i in range(len(qlist))])
                st.markdown("### 🤖 GPT Final Analysis Based on Your Input")
                result = gpt_finalize_with_answers(sample, user_response)
                st.success(result)
        else:
            st.warning("No usable Python files found in the uploaded ZIP.")
