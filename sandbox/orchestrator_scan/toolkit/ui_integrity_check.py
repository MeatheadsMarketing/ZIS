
import os

KEY_FUNCTIONS = ["run_ui", "st.header", "st.button", "st.columns", "st.dataframe"]

def run(target_folder):
    issues = []

    for root, _, files in os.walk(target_folder):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        file_issues = []
                        if "run_ui" not in content:
                            file_issues.append("Missing run_ui()")
                        if not any(k in content for k in KEY_FUNCTIONS[1:]):
                            file_issues.append("No Streamlit layout elements found")
                        if file_issues:
                            issues.append({"file": path, "issues": file_issues})
                except:
                    continue

    return {
        "status": "FAIL" if issues else "PASS",
        "ui_issues": issues
    }
