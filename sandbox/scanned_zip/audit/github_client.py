def push_to_github():
    import os
    return f'GitHub Token: {os.getenv("GITHUB_TOKEN")}'