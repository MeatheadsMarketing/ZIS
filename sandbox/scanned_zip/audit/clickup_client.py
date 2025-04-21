def push_to_clickup():
    import os
    return f'ClickUp Key: {os.getenv("CLICKUP_API_KEY")}'