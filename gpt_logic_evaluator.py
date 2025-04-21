
import openai
import os

def set_api_key():
    openai.api_key = os.getenv("OPENAI_API_KEY") or "your-openai-key"

def gpt_analyze_script(code, model="gpt-4"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a code summarizer and logic classifier."},
            {"role": "user", "content": f"Analyze this Python script and describe its purpose:\n\n{code[:3000]}"}
        ],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"]
