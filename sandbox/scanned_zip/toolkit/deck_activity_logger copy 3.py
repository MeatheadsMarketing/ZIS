import json
from datetime import datetime

def log_deck_action(agent, command, result):
    entry = {
        "agent": agent,
        "command": command,
        "result": result,
        "timestamp": datetime.now().isoformat()
    }
    with open("command_deck_log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
    return entry