def simulate_behavior(profile, task):
    traits = profile.get("traits", [])
    if "bold" in traits:
        return f"{profile['name']} attacks the task directly: {task}"
    elif "cautious" in traits:
        return f"{profile['name']} analyzes before executing: {task}"
    return f"{profile['name']} performs: {task}"