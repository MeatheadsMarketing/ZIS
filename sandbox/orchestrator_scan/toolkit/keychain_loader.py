import os
import json
from pathlib import Path
from dotenv import load_dotenv

def load_keychain(env_path='.env', json_path='secrets.json'):
    # Load from .env
    if Path(env_path).exists():
        load_dotenv(env_path)
        print(f"✅ Loaded environment variables from {env_path}")
    else:
        print(f"⚠️ .env file not found at {env_path}")

    # Load from JSON as fallback
    if Path(json_path).exists():
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
            for k, v in data.items():
                if k not in os.environ:
                    os.environ[k] = v
            print(f"✅ Loaded fallback secrets from {json_path}")
        except Exception as e:
            print(f"❌ Failed to load {json_path}: {e}")
    else:
        print(f"⚠️ secrets.json not found at {json_path}")

def get_key(key_name):
    return os.getenv(key_name)

import base64

def load_gcp_credentials():
    path = os.getenv("GOOGLE_CREDENTIALS_PATH")
    encoded_json = os.getenv("GOOGLE_CREDENTIALS_JSON")

    if path and Path(path).exists():
        print(f"✅ Using GCP credentials from file: {path}")
        return path
    elif encoded_json:
        decoded_path = "/tmp/google_credentials.json"
        with open(decoded_path, "wb") as f:
            f.write(base64.b64decode(encoded_json))
        print(f"✅ Decoded GCP credentials from environment variable")
        return decoded_path
    else:
        print("❌ No valid GCP credentials found")
        return None