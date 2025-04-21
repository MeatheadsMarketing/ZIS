import os
import requests
import pandas as pd

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_FLOWSTACK_DB_ID")
HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

CSV_OUTPUT = "flowstack_from_notion.csv"

def fetch_notion_rows():
    url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
    results = []
    has_more = True
    next_cursor = None

    while has_more:
        payload = {"page_size": 100}
        if next_cursor:
            payload["start_cursor"] = next_cursor

        response = requests.post(url, headers=HEADERS, json=payload).json()
        results.extend(response.get("results", []))
        has_more = response.get("has_more", False)
        next_cursor = response.get("next_cursor")

    return results

def parse_row(row):
    props = row["properties"]
    return {
        "Name": props.get("Name", {}).get("title", [{}])[0].get("text", {}).get("content", ""),
        "Tool Type": props.get("Tool Type", {}).get("select", {}).get("name", ""),
        "Flow Level": props.get("Flow Level", {}).get("number", ""),
        "Development Status": props.get("Development Status", {}).get("select", {}).get("name", ""),
        "System Membership": props.get("System Membership", {}).get("rich_text", [{}])[0].get("text", {}).get("content", ""),
        "Validation Score": props.get("Validation Score", {}).get("number", "")
    }

def sync_from_notion_to_csv():
    rows = fetch_notion_rows()
    parsed = [parse_row(row) for row in rows]
    df = pd.DataFrame(parsed)
    df.to_csv(CSV_OUTPUT, index=False)
    print(f"✅ Synced {len(df)} rows from Notion to {CSV_OUTPUT}")

if __name__ == "__main__":
    sync_from_notion_to_csv()
