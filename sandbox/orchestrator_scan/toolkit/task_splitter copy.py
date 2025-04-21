def split_objective_into_tasks(objective):
    tasks = []
    if "analyze" in objective.lower():
        tasks = ["Ingest data", "Parse structure", "Run analysis", "Generate summary"]
    elif "deploy" in objective.lower():
        tasks = ["Build environment", "Test deployment", "Monitor logs"]
    else:
        tasks = ["Step 1: Understand goal", "Step 2: Build plan", "Step 3: Execute"]
    return tasks