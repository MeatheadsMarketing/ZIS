import json
from datetime import datetime

def log_memory_entry(agent_name, content, tag="note"):
    entry = {
        "agent": agent_name,
        "tag": tag,
        "content": content,
        "timestamp": datetime.now().isoformat()
    }
    with open(f"{agent_name}_memory.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
    return entry