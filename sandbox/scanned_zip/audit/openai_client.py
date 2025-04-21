def call_openai(prompt):
    import os
    key = os.getenv('OPENAI_API_KEY')
    return f'Calling OpenAI with key: {key[:5]}...'