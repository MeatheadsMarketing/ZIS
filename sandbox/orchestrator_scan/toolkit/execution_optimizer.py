def optimize_execution(task, metrics):
    if metrics["speed"] > metrics["accuracy"]:
        return f"Optimize '{task}' for async or parallel execution."
    elif metrics["accuracy"] > metrics["speed"]:
        return f"Optimize '{task}' with validation and stepwise logic."
    return f"Balance speed and accuracy for '{task}'."