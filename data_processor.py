import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class DataProcessor:
    def __init__(self, df):
        self.df = df

    def save_to_csv(self, filename):
        self.df.to_csv(filename, index=False)

    def load_from_csv(self, filename):
        self.df = pd.read_csv(filename)

    def analyze_data(self):
        df_grouped = self.df.groupby('name', sort=False)[[
            'quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 
            'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 
            'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d'
        ]].mean()

        df_stack = df_grouped.stack()
        df_values = df_stack.to_frame(name='values').reset_index()

        index = pd.Index(range(len(df_values)))
        df_values.set_index(index, inplace=True)

        df_values.rename(columns={'level_1': 'percent_change'}, inplace=True)
        df_values['percent_change'] = df_values['percent_change'].replace([
            'quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 
            'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 
            'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d'
        ], ['t1', 't2', 't3', 't4', 't5', 't6'])

        return df_values

    def plot_data(self, df_values):
        plt.figure(figsize=(12, 6))
        sns.catplot(x='percent_change', y='values', hue='name', data=df_values, kind='point')
        plt.title('Average Percent Change in Cryptocurrency Prices')
        plt.ylabel('Average Percent Change')
        plt.xlabel('Time Period')
        plt.show()

    def plot_bitcoin_price(self):
        df_bitcoin = self.df.query("name == 'Bitcoin'")[['name', 'quote.USD.price', 'timestamp']]
        sns.set_theme(style="darkgrid")
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='timestamp', y='quote.USD.price', data=df_bitcoin)
        plt.title('Bitcoin Price Over Time')
        plt.ylabel('Price (USD)')
        plt.xlabel('Timestamp')
        plt.show()
