def process_feedback(current_state, feedback):
    if "error" in feedback.lower():
        return current_state + " -> Apply error handler"
    elif "success" in feedback.lower():
        return current_state + " -> Confirm and proceed"
    return current_state + " -> Request clarification"