def call_gemini():
    import os
    return f'Gemini API Key: {os.getenv("GEMINI_API_KEY")}'