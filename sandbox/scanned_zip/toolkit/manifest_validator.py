
import os
import json

def run(target_folder):
    manifest_path = os.path.join(target_folder, "version_manifest.json")
    if not os.path.exists(manifest_path):
        return {
            "status": "FAIL",
            "error": "version_manifest.json not found"
        }

    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        missing_files = []
        if isinstance(manifest, dict):
            for key, filepath in manifest.items():
                abs_path = os.path.join(target_folder, filepath)
                if not os.path.exists(abs_path):
                    missing_files.append(filepath)
        elif isinstance(manifest, list):
            for entry in manifest:
                if isinstance(entry, dict) and "file" in entry:
                    abs_path = os.path.join(target_folder, entry["file"])
                    if not os.path.exists(abs_path):
                        missing_files.append(entry["file"])

        return {
            "status": "FAIL" if missing_files else "PASS",
            "missing_files": missing_files
        }

    except Exception as e:
        return {
            "status": "FAIL",
            "exception": str(e)
        }
