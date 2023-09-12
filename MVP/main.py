from sheets_api import SheetsAPI
import replicate
from dotenv import load_dotenv
import os


class EvalWriter:
    def __init__(self):
        load_dotenv()
        self.REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')
        self.sheets_api = SheetsAPI(scopes=['https://www.googleapis.com/auth/spreadsheets.readonly'])

    def 
