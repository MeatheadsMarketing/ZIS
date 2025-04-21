def evaluate_metrics(output, context):
    return {
        "speed": context.count("fast") + output.count("cache"),
        "accuracy": context.count("validate") + output.count("check")
    }