#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
from datetime import datetime

class OctopusEnergyAPI:
    def __init__(self, api_key, mpan, serial_number):
        self.api_base_url = "https://api.octopus.energy/v1/"
        self.api_key = api_key
        self.mpan = mpan
        self.serial_number = serial_number
        self.headers = {'Accept': 'application/json'}
        self.auth = HTTPBasicAuth(api_key, '')

    def get_consumption_data(self, group_by, page_size, period_from, period_to):
        consumption_url = f"{self.api_base_url}electricity-meter-points/{self.mpan}/meters/{self.serial_number}/consumption/"
        request_body = {
            "group_by": group_by,
            "page_size": page_size,
            "period_from": period_from,
            "period_to": period_to,
        }
        res = requests.get(consumption_url, headers=self.headers, auth=self.auth, params=request_body)
        res.raise_for_status()
        return res.json()['results']

class DataProcessor:
    def __init__(self, api):
        self.api = api

    def process_consumption_data(self):
        try:
            consumption_data = self.api.get_consumption_data("day", "100000", "2024-01-01T23:30:00.000Z", datetime.now().isoformat())
            consumption_dataframe = pd.DataFrame(consumption_data)
            sorted_reverse_dataframe = consumption_dataframe.sort_values(by='interval_start', ascending=False)
            print(sorted_reverse_dataframe.head(5))
        except Exception as e:
            print("Error:", e)


load_dotenv()

api_key = os.getenv('API_KEY')
mpan = os.getenv('MPAN')
serial_number = os.getenv('SERIAL_NUMBER')
api = OctopusEnergyAPI(api_key, mpan, serial_number)

data_processor = DataProcessor(api)
data_processor.process_consumption_data()
