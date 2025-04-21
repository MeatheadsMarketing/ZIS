import json

def write_agent_config(agent_profile, filename="agent_config.json"):
    with open(filename, "w") as f:
        json.dump(agent_profile, f, indent=2)
    return filename