import os
from google.cloud import secretmanager

def load_secrets_from_gcp(project_id="your-gcp-project-id"):
    client = secretmanager.SecretManagerServiceClient()
    parent = f"projects/{project_id}"
    response = client.list_secrets(request={"parent": parent})
    for secret in response.secrets:
        name = secret.name.split("/")[-1].upper().replace("-", "_")
        version_path = f"{secret.name}/versions/latest"
        secret_response = client.access_secret_version(request={"name": version_path})
        os.environ[name] = secret_response.payload.data.decode("utf-8")
        print(f"✅ Loaded {name}")