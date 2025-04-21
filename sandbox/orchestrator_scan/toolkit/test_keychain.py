import os
import json
from config.keychain_loader import load_keychain

# Step 1: Load secrets from .env or secrets.json
load_keychain()

# Step 2: Define the services to check
services = {
    'OPENAI_API_KEY': 'OpenAI',
    'VERTEX_API_KEY': 'Vertex',
    'GEMINI_API_KEY': 'Gemini',
    'CLAUDE_API_KEY': 'Claude',
    'HUGGINGFACE_TOKEN': 'HuggingFace',
    'REPLICATE_API_TOKEN': 'Replicate',
    'GITHUB_TOKEN': 'GitHub',
    'NOTION_SECRET': 'Notion',
    'SLACK_BOT_TOKEN': 'Slack',
    'TWILIO_ACCOUNT_SID': 'Twilio SID',
    'TWILIO_AUTH_TOKEN': 'Twilio Token',
    'CLICKUP_API_KEY': 'ClickUp'
}

# Step 3: Check and print status
print("🔍 Key Status:")
for key, name in services.items():
    val = os.getenv(key)
    status = "✅" if val and val != "__optional__" else "❌"
    print(f"{status} {name} = {key}")

# Step 4: Debug GCP token path
gcp_path = os.getenv("GOOGLE_CREDENTIALS_PATH")
gcp_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
print(f"\nGCP Token Path: {gcp_path if gcp_path else 'None'}")
print(f"GCP Token (Base64 present): {bool(gcp_json)}")

# Step 5: Optional key format checker
def is_probably_valid(val):
    if not val or val == "__optional__":
        return False
    return any(val.startswith(prefix) for prefix in ["sk-", "SG.", "xoxp-", "ntn_", "hf_", "AC", "ghp_", "r8_", "AIza", "GOCSPX-", "eyJ"])

print("\nEnhanced Key Check:")
for key in services:
    val = os.getenv(key)
    status = "✅" if is_probably_valid(val) else "❌"
    print(f"{status} {key} = {val[:6]}..." if val else f"❌ {key} is empty")