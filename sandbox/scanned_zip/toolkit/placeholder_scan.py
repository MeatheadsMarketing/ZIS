
import os

KEYWORDS = ["TODO", "PLACEHOLDER", "NEEDS IMPLEMENTATION", "# Incomplete", "# Placeholder"]
MIN_VALID_SIZE = 100  # bytes

def run(target_folder):
    placeholder_hits = []
    small_files = []

    for root, _, files in os.walk(target_folder):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        for keyword in KEYWORDS:
                            if keyword in content:
                                placeholder_hits.append(path)
                                break
                    if os.path.getsize(path) < MIN_VALID_SIZE:
                        small_files.append(path)
                except:
                    continue

    status = "PASS"
    if placeholder_hits or small_files:
        status = "FAIL"

    return {
        "status": status,
        "placeholder_files": placeholder_hits,
        "small_files": small_files
    }
