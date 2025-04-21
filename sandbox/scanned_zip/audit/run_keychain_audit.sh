#!/bin/bash
echo "🔐 Running Keychain Integrity Audit + Notion Sync"
python config/test_keychain.py
python config/notion_sync_keys.py
echo "☁️ Optionally push to GCP Secret Manager?"
read -p "Type YES to continue: " confirm
if [ "$confirm" == "YES" ]; then
  python config/gcp_secret_uploader.py
fi