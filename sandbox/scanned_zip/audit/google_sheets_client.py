from google.oauth2 import service_account
from googleapiclient.discovery import build
from config.keychain_loader import load_gcp_credentials

def append_to_sheet(spreadsheet_id, range_, values):
    creds_path = load_gcp_credentials()
    creds = service_account.Credentials.from_service_account_file(creds_path)
    service = build('sheets', 'v4', credentials=creds)

    body = {'values': values}
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range=range_,
        valueInputOption="RAW", body=body).execute()
    return result