def render_command_deck(agents):
    layout = []
    for agent in agents:
        layout.append(f"[{agent['name']}] Status: {agent.get('status', 'idle')}, Current Task: {agent.get('task', '-')}")
    return "\n".join(layout)