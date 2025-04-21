def clean_agent_memory(agent_name):
    open(f"{agent_name}_memory.json", "w").close()
    return f"{agent_name}_memory.json wiped."