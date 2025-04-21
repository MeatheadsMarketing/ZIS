from .gpt_explainer import explain_file
from pathlib import Path

def explain_all_files(base_path: Path):
    for file in base_path.rglob("*"):
        if file.is_file():
            explain_file(file)