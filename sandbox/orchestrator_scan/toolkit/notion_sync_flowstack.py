import os
import requests
import pandas as pd

NOTION_API_URL = "https://api.notion.com/v1/pages"
NOTION_DATABASE_ID = os.getenv("NOTION_FLOWSTACK_DB_ID")
NOTION_API_KEY = os.getenv("NOTION_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def create_notion_page(row):
    properties = {
        "Name": {"title": [{"text": {"content": row["Name"]}}]},
        "Tool Type": {"select": {"name": row["Tool Type"]}},
        "Flow Level": {"number": int(row["Flow Level"])} if row["Flow Level"] else None,
        "Development Status": {"select": {"name": row["Development Status"]}} if row["Development Status"] else None,
        "System Membership": {"rich_text": [{"text": {"content": str(row["System Membership"])}}]},
        "Validation Score": {"number": float(row["Validation Score"])} if row["Validation Score"] else None
    }

    # Remove None values
    properties = {k: v for k, v in properties.items() if v is not None}

    data = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": properties
    }

    response = requests.post(NOTION_API_URL, headers=HEADERS, json=data)
    return response.status_code, response.text

def sync_to_notion(csv_path):
    df = pd.read_csv(csv_path)
    for index, row in df.iterrows():
        status, response = create_notion_page(row)
        print(f"Synced {row['Name']}: Status {status}")

if __name__ == "__main__":
    sync_to_notion("flowstack_master_v5.csv")
