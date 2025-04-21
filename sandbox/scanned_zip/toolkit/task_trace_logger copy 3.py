import json
from datetime import datetime

def log_task_trace(agent, task, status="pending"):
    trace = {
        "agent": agent,
        "task": task,
        "status": status,
        "timestamp": datetime.now().isoformat()
    }
    with open("task_trace_log.json", "a") as f:
        f.write(json.dumps(trace) + "\n")
    return trace