def trigger_feedback_response(trigger_type):
    if trigger_type == "failure":
        return "Detected failure pattern — rerouting agent task"
    elif trigger_type == "success":
        return "Execution succeeded — updating context"
    return "Unknown trigger"