import json
from datetime import datetime

def log_review_result(agent_name, review_results):
    log = {
        "agent": agent_name,
        "review": review_results,
        "timestamp": datetime.now().isoformat()
    }
    with open("self_review_log.json", "a") as f:
        f.write(json.dumps(log) + "\n")
    return log