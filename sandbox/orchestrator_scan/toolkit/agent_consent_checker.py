def check_sync_consent(agent_metadata):
    if agent_metadata.get("autonomy") == "low":
        return True
    return agent_metadata.get("allow_sync", False)