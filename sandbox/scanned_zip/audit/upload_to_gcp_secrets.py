import json
from google.cloud import secretmanager
from google.oauth2 import service_account

def upload_secrets_to_gcp(json_path="config/secrets.json", credentials_path="config/google_credentials.json", project_id=None):
    creds = service_account.Credentials.from_service_account_file(credentials_path)
    client = secretmanager.SecretManagerServiceClient(credentials=creds)

    with open(json_path, "r") as f:
        secrets = json.load(f)

    if not project_id:
        project_id = creds.project_id

    for key, value in secrets.items():
        parent = f"projects/{project_id}"
        secret_id = key.replace("_", "-").lower()

        try:
            client.create_secret(
                request={
                    "parent": parent,
                    "secret_id": secret_id,
                    "secret": {"replication": {"automatic": {}}}
                }
            )
        except Exception:
            pass  # Secret may already exist

        payload = value.encode("UTF-8")
        client.add_secret_version(
            request={
                "parent": f"{parent}/secrets/{secret_id}",
                "payload": {"data": payload}
            }
        )
        print(f"✅ Uploaded: {key}")

if __name__ == "__main__":
    upload_secrets_to_gcp()