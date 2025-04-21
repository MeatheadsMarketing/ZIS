
import zipfile

def validate_bundle(zip_path):
    issues = []
    with zipfile.ZipFile(zip_path, "r") as zipf:
        for file in zipf.namelist():
            if file.endswith(".py"):
                with zipf.open(file) as f:
                    content = f.read().decode("utf-8", errors="ignore")
                    if "PLACEHOLDER" in content or "TODO" in content:
                        issues.append(f"{file} contains placeholder text")
                    if "run_ui" not in content and "main_app.py" not in file:
                        issues.append(f"{file} missing run_ui()")
    return issues


import streamlit as st
import os

DEPLOY_DIR = os.path.join(os.path.dirname(__file__), "..", "deploy_ready")
ZIP_PATH = os.path.join(DEPLOY_DIR, "fixed_assistants_bundle.zip")
CHANGELOG_PATH = os.path.join(DEPLOY_DIR, "CHANGELOG.md")

def main():
    st.set_page_config(page_title="v1.0 Deployment Tab", layout="wide")
    st.title("Deployment Finalizer – v1.0 Fixed Assistants")

    st.markdown("### Review CHANGELOG")
    if os.path.exists(CHANGELOG_PATH):
        with open(CHANGELOG_PATH, "r", encoding="utf-8") as f:
            changelog = f.read()
        st.code(changelog, language="markdown")
    else:
        st.warning("CHANGELOG.md not found.")

    st.markdown("### Ready-to-Push ZIP")
    if os.path.exists(ZIP_PATH):
        st.download_button(
            label="Download Fixed Assistants ZIP",
            file_name="fixed_assistants_bundle.zip",
            data=open(ZIP_PATH, "rb").read(),
            mime="application/zip"
        )
    else:
        st.warning("Bundle ZIP not found.")

    st.markdown("### Version Tag")
    version = st.text_input("Enter Version Tag", value="v1.0-fixed")

    
    st.markdown("### Final Validation")

    if st.button("Run Final Validation Check"):
        if os.path.exists(ZIP_PATH):
            issues = validate_bundle(ZIP_PATH)
            if not issues:
                st.success("All checks passed. This bundle is production-ready.")
            else:
                st.error("Validation Failed:")
                for issue in issues:
                    st.markdown(f"- {issue}")
        else:
            st.warning("No ZIP found to validate.")


    if st.button("Push to GitHub (Simulated)"):
        st.success(f"Simulated push of ZIP + CHANGELOG with tag: {version}")
        st.info("This would trigger a GitHub release in the real system.")

if __name__ == "__main__":
    main()
