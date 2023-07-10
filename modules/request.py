import requests

# Read the API key from the file
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

headers = {
    "CB-ACCESS-KEY": api_key,
}

response = requests.get(url, headers=headers)
data = response.json()

btc_usd_price = data['data']['amount']
print("BTC-USD price:", btc_usd_price)

eth_usd_price = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot", headers=headers).json()['data']['amount']
print("ETH-USD price:", eth_usd_price)