def run_agent(input_data, agent_config):
    if "analyze" in agent_config["objectives"][0].lower():
        return f"Agent {agent_config['agent_name']} analyzing: {input_data}"
    return f"Agent {agent_config['agent_name']} received input."