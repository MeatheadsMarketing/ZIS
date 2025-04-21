def run_huggingface_model():
    import os
    return f'HF Token: {os.getenv("HUGGINGFACE_TOKEN")}'