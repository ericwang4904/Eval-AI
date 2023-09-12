import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
import numpy as np

class SheetsAPI:
    def __init__(self, scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']):
        self.scopes = scopes
        self.creds = self.configure_credentials()

    def configure_credentials(self):
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.scopes)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.scopes)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        return creds
    
    def get_sheet_values(self, sheet_id, range):
        service = build('sheets', 'v4', credentials=self.creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheet_id, range=range).execute()
        values = result.get('values', [])

        if not values:
            raise ValueError('No data found.')
        
        df = pd.DataFrame(values)
        return df
    
    def get_dict_from_sheet_values(self, values):
        students = list(values.drop(0, axis=1).iloc[0])
        notes = values.drop(0, axis=1).iloc[1:]
        notes = [list(notes[col]) for col in notes.columns]
        return {student: note for student, note in zip(students, notes)}