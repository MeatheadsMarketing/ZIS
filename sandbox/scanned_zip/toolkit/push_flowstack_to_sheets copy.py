import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Define constants
CSV_PATH = "flowstack_master_v5.csv"
SPREADSHEET_NAME = "FlowStack Intelligence Table"
WORKSHEET_NAME = "Sheet1"
CREDENTIALS_FILE = "your_service_account_credentials.json"  # Replace with your actual file name

def push_csv_to_google_sheet():
    # Define scope and credentials
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)

    # Load CSV
    df = pd.read_csv(CSV_PATH)
    
    # Open spreadsheet and worksheet
    try:
        spreadsheet = client.open(SPREADSHEET_NAME)
    except gspread.SpreadsheetNotFound:
        spreadsheet = client.create(SPREADSHEET_NAME)
    
    try:
        worksheet = spreadsheet.worksheet(WORKSHEET_NAME)
        spreadsheet.del_worksheet(worksheet)
    except gspread.WorksheetNotFound:
        pass

    worksheet = spreadsheet.add_worksheet(title=WORKSHEET_NAME, rows=str(len(df)+1), cols=str(len(df.columns)))
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print(f"✅ Data from {CSV_PATH} pushed to Google Sheet: {SPREADSHEET_NAME}")

if __name__ == "__main__":
    push_csv_to_google_sheet()
