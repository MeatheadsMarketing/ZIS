def assign_tasks_to_agents(task_list, agents):
    assignments = {}
    for i, task in enumerate(task_list):
        agent = agents[i % len(agents)]
        if agent not in assignments:
            assignments[agent] = []
        assignments[agent].append(task)
    return assignments