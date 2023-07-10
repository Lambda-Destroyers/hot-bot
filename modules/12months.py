import requests
import datetime
import matplotlib.pyplot as plt

# Read the API key from api_key.txt file
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

headers = {
    "CB-ACCESS-KEY": api_key,
}

# Function to retrieve the current price of a given cryptocurrency
def get_current_price(product_id):
    url = f"https://api.coinbase.com/v2/prices/{product_id}/spot"
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['data']['amount']

# Retrieve current prices for BTC-USD and ETH-USD
btc_usd_price = get_current_price("BTC-USD")
eth_usd_price = get_current_price("ETH-USD")

# Print current prices
print("BTC-USD price:", btc_usd_price)
print("ETH-USD price:", eth_usd_price)

# Historical chart code (including API information)
api_url = "https://api.pro.coinbase.com/products"

# Calculate the start and end dates
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=365)

# Function to retrieve historical data for a given product
def get_historical_data(product_id):
    candles_url = f"{api_url}/{product_id}/candles"
    params = {
        "start": start_date.isoformat(),
        "end": end_date.isoformat(),
        "granularity": 604800,  # Daily granularity (86400 seconds = 1 day)
    }
    response = requests.get(candles_url, params=params)
    data = response.json()
    return data

# Retrieve historical data for BTC-USD
btc_data = get_historical_data("BTC-USD")
print("BTC Data:", btc_data)

# Retrieve historical data for ETH-USD
eth_data = get_historical_data("ETH-USD")
print("ETH Data:", eth_data)
