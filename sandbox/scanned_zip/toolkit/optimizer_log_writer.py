import json
from datetime import datetime

def log_optimization(task, strategy):
    log = {
        "task": task,
        "optimization_strategy": strategy,
        "timestamp": datetime.now().isoformat()
    }
    with open("optimizer_log.json", "a") as f:
        f.write(json.dumps(log) + "\n")
    return log