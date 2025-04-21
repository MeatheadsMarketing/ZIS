
import streamlit as st
import os
from datetime import datetime

st.title("📘 README Generator")

readme_sections = {
    "Title": st.text_input("Project Title:", "Recovered Assistant Bundle"),
    "Description": st.text_area("Project Description:", "This assistant package includes..."),
    "Contents": st.text_area("Contents Overview:", "- tool_1.py: Does XYZ\n- tool_2.py: Handles ABC"),
    "Usage": st.text_area("Usage Instructions:", "To use this package, unzip and run..."),
    "Version": st.text_input("Version", "v2.0"),
    "Date": datetime.now().strftime("%Y-%m-%d")
}

generate = st.button("Generate README.md")

if generate:
    readme_content = "\n\n".join([f"## {k}\n{v}" for k, v in readme_sections.items()])
    with open("./outputs/assistant_README.md", "w") as f:
        f.write(readme_content)
    st.success("README.md created successfully.")
