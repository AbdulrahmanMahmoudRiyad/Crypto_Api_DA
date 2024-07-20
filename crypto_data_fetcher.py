import json
import pandas as pd
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from time import sleep

class CryptoDataFetcher:
    def __init__(self, api_key, url, parameters, headers):
        self.api_key = api_key
        self.url = url
        self.parameters = parameters
        self.headers = headers
        self.session = Session()
        self.session.headers.update(headers)
        
    def fetch_data(self):
        try:
            response = self.session.get(self.url, params=self.parameters)
            data = json.loads(response.text)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            return None

    def api_runner(self, df):
        data = self.fetch_data()
        if data:
            df_new = pd.json_normalize(data['data'])
            df_new['timestamp'] = pd.to_datetime('now')
            df = pd.concat([df, df_new], ignore_index=True)
        return df

    def run(self, iterations=50, sleep_time=10):
        df = pd.DataFrame()
        for i in range(iterations):
            df = self.api_runner(df)
            print(f'API Runner completed {i+1}/{iterations}')
            sleep(sleep_time)
        return df
