from google.oauth2 import service_account
from googleapiclient.discovery import build
from config.keychain_loader import load_gcp_credentials

def upload_file_to_drive(filename, mimetype='application/octet-stream'):
    creds_path = load_gcp_credentials()
    creds = service_account.Credentials.from_service_account_file(creds_path)
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': filename}
    media = MediaFileUpload(filename, mimetype=mimetype)
    uploaded = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return uploaded.get('id')