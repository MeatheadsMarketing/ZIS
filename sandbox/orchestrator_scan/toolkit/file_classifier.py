import pandas as pd
from pathlib import Path

def classify_files(base_path: Path) -> pd.DataFrame:
    file_data = []
    for filepath in base_path.rglob("*"):
        if filepath.is_file():
            file_data.append({
                "filename": filepath.name,
                "path": str(filepath),
                "ext": filepath.suffix.lower(),
                "size_kb": round(filepath.stat().st_size / 1024, 2),
                "role": detect_role(filepath.name)
            })
    return pd.DataFrame(file_data)

def detect_role(filename):
    if filename.startswith("main") or filename.startswith("app"):
        return "launcher"
    elif "config" in filename:
        return "config"
    elif "readme" in filename.lower():
        return "documentation"
    elif filename.endswith(".json") or filename.endswith(".csv"):
        return "data"
    elif filename.endswith(".py"):
        return "logic"
    else:
        return "misc"