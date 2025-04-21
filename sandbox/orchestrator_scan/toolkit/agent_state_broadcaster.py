import json

def broadcast_state(agent_name, state):
    message = {
        "agent": agent_name,
        "state": state
    }
    with open(f"{agent_name}_sync_state.json", "w") as f:
        json.dump(message, f, indent=2)
    return message