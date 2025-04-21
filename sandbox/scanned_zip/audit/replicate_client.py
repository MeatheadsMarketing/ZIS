def call_replicate():
    import os
    return f'Replicate Token: {os.getenv("REPLICATE_API_TOKEN")}'