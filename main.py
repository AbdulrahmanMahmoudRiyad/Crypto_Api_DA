import pandas as pd
from crypto_data_fetcher import CryptoDataFetcher
from data_processor import DataProcessor

# API key and URL explicitly defined
API_KEY = '534c9c2a-1b3f-4e2a-ae83-db60f4c39c38'
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'start': '1',
    'limit': '15',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

def main():
    fetcher = CryptoDataFetcher(API_KEY, URL, parameters, headers)
    df = fetcher.run(iterations=50, sleep_time=10)

    processor = DataProcessor(df)
    processor.save_to_csv('crypto_data.csv')

    df_values = processor.analyze_data()
    processor.plot_data(df_values)
    processor.plot_bitcoin_price()

if __name__ == "__main__":
    main()
