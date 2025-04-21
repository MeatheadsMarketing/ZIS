import os, json
from notion_client import Client
from datetime import datetime

NOTION_SECRET = os.getenv("NOTION_SECRET")
NOTION_DB_ID = os.getenv("NOTION_DB_COLAB", "YOUR_DB_ID_HERE")

def sync_secrets_to_notion():
    notion = Client(auth=NOTION_SECRET)
    with open("config/secrets.json", "r") as f:
        secrets = json.load(f)

    for key, val in secrets.items():
        status = "✅ Active" if val and val != "__optional__" else "❌ Missing" if not val else "💤 Optional"
        notion.pages.create(
            parent={"database_id": NOTION_DB_ID},
            properties={
                "Key": {"title": [{"text": {"content": key}}]},
                "Status": {"rich_text": [{"text": {"content": status}}]},
                "Optional": {"checkbox": val == "__optional__"},
                "Last Updated": {"date": {"start": datetime.utcnow().isoformat()}}
            }
        )
if __name__ == "__main__":
    sync_secrets_to_notion()