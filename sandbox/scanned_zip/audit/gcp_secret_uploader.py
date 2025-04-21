import os, json
from google.cloud import secretmanager

def upload_to_gcp_secrets(project_id="your-gcp-project-id"):
    client = secretmanager.SecretManagerServiceClient()
    with open("config/secrets.json", "r") as f:
        secrets = json.load(f)

    for name, value in secrets.items():
        parent = f"projects/{project_id}"
        try:
            secret = client.create_secret(
                request={
                    "parent": parent,
                    "secret_id": name.lower().replace("_", "-"),
                    "secret": {"replication": {"automatic": {}}},
                }
            )
        except:
            secret = client.secret_path(project_id, name.lower().replace("_", "-"))

        client.add_secret_version(
            request={
                "parent": f"{parent}/secrets/{name.lower().replace('_', '-')}",
                "payload": {"data": value.encode("UTF-8")},
            }
        )
if __name__ == "__main__":
    upload_to_gcp_secrets()