import os
import json
from notion_client import Client

def sync_keys_to_notion(database_id="YOUR_NOTION_DB_ID"):
    notion = Client(auth=os.getenv("NOTION_SECRET"))
    with open("config/secrets.json", "r") as f:
        secrets = json.load(f)

    for key, value in secrets.items():
        notion.pages.create(parent={"database_id": database_id}, properties={
            "Key": {"title": [{"text": {"content": key}}]},
            "Value": {"rich_text": [{"text": {"content": value[:30] + '...'}}]},
            "Status": {"select": {"name": "✅ Synced" if value else "❌ Missing"}}
        })

if __name__ == "__main__":
    sync_keys_to_notion()