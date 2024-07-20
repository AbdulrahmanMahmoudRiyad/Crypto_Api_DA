# Crypto_Api_DA

This project involves building a Python script to automate the collection of cryptocurrency data from an API provided by CoinMarketCap. The script fetches real-time data on cryptocurrency listings, processes and stores this data in a structured format, and performs analysis and visualization of key metrics.

## Project Structure

The project is organized into the following files:

- `crypto_data_fetcher.py`: Handles the API requests.
- `data_processor.py`: Handles data processing and visualization.
- `main.py`: The entry point of the script, coordinating the data fetching, processing, and visualization.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AbdulrahmanMahmoudRiyad/Crypto_Api_DA.git
    cd Crypto_Api_DA
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. To run the script, simply execute `main.py`:
    ```sh
    python main.py
    ```

## File Descriptions

- **crypto_data_fetcher.py**: 
    - Contains the `CryptoDataFetcher` class responsible for fetching cryptocurrency data from the CoinMarketCap API.
    
- **data_processor.py**: 
    - Contains the `DataProcessor` class responsible for processing the fetched data, saving it to a CSV file, and generating visualizations.
    
- **main.py**: 
    - The entry point of the script. It creates instances of `CryptoDataFetcher` and `DataProcessor`, runs the data fetching process, and generates visualizations.

## Example Visualizations

The script generates the following visualizations:

1. Average Percent Change in Cryptocurrency Prices:
    ![Percent Change Visualization](example_percent_change.png)

2. Bitcoin Price Over Time:
    ![Bitcoin Price Visualization](example_bitcoin_price.png)
