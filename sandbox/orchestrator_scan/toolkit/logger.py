
import json
import os
from datetime import datetime

def log_result(result_dict, output_path="audit_log.json"):
    with open(output_path, "w") as f:
        json.dump(result_dict, f, indent=4)

def save_report(results, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Streamlit Audit Report\n")
        f.write(f"**Generated:** {datetime.now().isoformat()}\n\n")

        for section, result in results.items():
            f.write(f"## {section.upper()}\n")
            status = result.get("status", "UNKNOWN")
            f.write(f"**Status:** `{status}`\n\n")

            for key, value in result.items():
                if key == "status":
                    continue
                f.write(f"**{key}:**\n")
                if isinstance(value, list):
                    for item in value:
                        f.write(f"- {item}\n")
                elif isinstance(value, dict):
                    for subkey, subval in value.items():
                        f.write(f"- {subkey}: {subval}\n")
                else:
                    f.write(f"- {value}\n")
            f.write("\n")
