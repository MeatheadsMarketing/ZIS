import json
import os

def retrieve_agent_memory(agent_name, tag_filter=None):
    filename = f"{agent_name}_memory.json"
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        lines = f.readlines()
    entries = [json.loads(line) for line in lines]
    if tag_filter:
        entries = [e for e in entries if e["tag"] == tag_filter]
    return entries