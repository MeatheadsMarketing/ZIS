def orchestrate_team_sync(agent_states):
    synced = {}
    for agent, state in agent_states.items():
        synced[agent] = {
            "status": "synced",
            "shared_knowledge": state.get("current_goal", "undefined")
        }
    return synced