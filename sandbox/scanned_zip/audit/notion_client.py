def query_notion():
    import os
    return f'Notion Secret: {os.getenv("NOTION_SECRET")}'