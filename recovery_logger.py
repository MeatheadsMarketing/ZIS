
import os
import json
import datetime

LOG_PATH = "outputs/recovery_flow_log.json"

def log_recovery_snapshot(zip_name, files_processed, gpt_summary,
                          registered_components=None, shortcuts_added=None, duration="N/A"):

    os.makedirs("outputs", exist_ok=True)
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "zip_name": zip_name,
        "files_processed": files_processed,
        "gpt_summary": gpt_summary,
        "registered_components": registered_components or [],
        "shortcuts_added": shortcuts_added or [],
        "duration": duration
    }

    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(log_entry)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
