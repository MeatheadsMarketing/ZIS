import json
from datetime import datetime

def log_feedback_event(agent_name, trigger, adjustment):
    event = {
        "agent": agent_name,
        "trigger": trigger,
        "adjustment": adjustment,
        "timestamp": datetime.now().isoformat()
    }
    with open("feedback_log.json", "a") as f:
        f.write(json.dumps(event) + "\n")
    return event