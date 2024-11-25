import pandas as pd
from google.oauth2.service_account import Credentials
import gspread

def load_data(source_type, file_path=None, sheet_url=None):
    if source_type == 'csv':
        data = pd.read_csv(file_path)
    elif source_type == 'google_sheet':
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file('path_to_service_account.json', scopes=scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_url(sheet_url).sheet1
        data = pd.DataFrame(sheet.get_all_records())
    else:
        raise ValueError("Invalid source type. Choose 'csv' or 'google_sheet'")
    return data
