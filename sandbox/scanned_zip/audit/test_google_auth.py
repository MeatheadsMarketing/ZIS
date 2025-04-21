from google.oauth2 import service_account
from googleapiclient.discovery import build
from config.keychain_loader import load_gcp_credentials

def test_gcp_access():
    try:
        path = load_gcp_credentials()
        creds = service_account.Credentials.from_service_account_file(path)
        drive = build('drive', 'v3', credentials=creds)
        result = drive.about().get(fields="user").execute()
        print("✅ GCP Auth Success. Service Account Email:", result["user"]["email"])
    except Exception as e:
        print("❌ GCP Auth Failed:", e)

if __name__ == "__main__":
    test_gcp_access()