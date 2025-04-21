
import os

REQUIRED_DIRS = [".streamlit", "pages"]
REQUIRED_FILES = ["main_app.py"]

def run(target_folder):
    results = {
        "missing_dirs": [],
        "missing_files": [],
        "status": "PASS"
    }

    for dir_name in REQUIRED_DIRS:
        dir_path = os.path.join(target_folder, dir_name)
        if not os.path.isdir(dir_path):
            results["missing_dirs"].append(dir_name)

    for file_name in REQUIRED_FILES:
        file_path = os.path.join(target_folder, file_name)
        if not os.path.isfile(file_path):
            results["missing_files"].append(file_name)

    if results["missing_dirs"] or results["missing_files"]:
        results["status"] = "FAIL"

    return results
