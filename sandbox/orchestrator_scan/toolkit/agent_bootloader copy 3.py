def initialize_agent(name, goals, input_format, output_format):
    return {
        "agent_name": name,
        "objectives": goals,
        "input_format": input_format,
        "output_format": output_format,
        "status": "initialized"
    }