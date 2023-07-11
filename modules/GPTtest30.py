import requests
import json
import datetime
import matplotlib.pyplot as plt

# Read the API key from api_key.txt file
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()
headers = {
    "CB-ACCESS-KEY": api_key,
}

# Read the API key from gpt_key.txt file
with open('gpt_api.txt', 'r') as file:
    gpt_api = file.read().strip()

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
start_date = end_date - datetime.timedelta(days=30)

# Function to retrieve historical data for a given product
def get_historical_data(product_id):
    candles_url = f"{api_url}/{product_id}/candles"
    params = {
        "start": start_date.isoformat(),
        "end": end_date.isoformat(),
        "granularity": 86400,  # Daily granularity (86400 seconds = 1 day)
    }
    response = requests.get(candles_url, params=params)
    data = response.json()
    return data

# Retrieve historical data for BTC-USD
btc_data = get_historical_data("BTC-USD")
btc_timestamps = [datetime.datetime.fromtimestamp(int(entry[0])) for entry in btc_data]
btc_opens = [entry[3] for entry in btc_data]
btc_highs = [entry[2] for entry in btc_data]
btc_lows = [entry[1] for entry in btc_data]
btc_closes = [entry[4] for entry in btc_data]

# Retrieve historical data for ETH-USD
eth_data = get_historical_data("ETH-USD")
eth_timestamps = [datetime.datetime.fromtimestamp(int(entry[0])) for entry in eth_data]
eth_opens = [entry[3] for entry in eth_data]
eth_highs = [entry[2] for entry in eth_data]
eth_lows = [entry[1] for entry in eth_data]
eth_closes = [entry[4] for entry in eth_data]

# Plotting Bitcoin (BTC-USD) and Ethereum (ETH-USD) charts
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(btc_timestamps, btc_closes, color='blue')
ax1.vlines(btc_timestamps, btc_lows, btc_highs, color='black', linewidth=1)
ax1.set_title("Bitcoin (BTC-USD) - 30 Day Historical Data")
ax1.set_xlabel("Date")
ax1.set_ylabel("Price (USD)")

ax2.plot(eth_timestamps, eth_closes, color='green')
ax2.vlines(eth_timestamps, eth_lows, eth_highs, color='black', linewidth=1)
ax2.set_title("Ethereum (ETH-USD) - 30 Day Historical Data")
ax2.set_xlabel("Date")
ax2.set_ylabel("Price (USD)")

fig.autofmt_xdate()  # Automatically format the x-axis labels to avoid overlapping

plt.tight_layout()
plt.show()

def get_investment_recommendation(btc_data, eth_data):
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {gpt_api}",
    }
    btc_price = btc_data[0][4]
    eth_price = eth_data[0][4]
    btc_prompt = f"\n\nBTC-USD historical data:\n- Opens: {btc_opens}\n- Highs: {btc_highs}\n- Lows: {btc_lows}\n- Closes: {btc_closes}"
    eth_prompt = f"\n\nETH-USD historical data:\n- Opens: {eth_opens}\n- Highs: {eth_highs}\n- Lows: {eth_lows}\n- Closes: {eth_closes}"
    prompt = f"Analyze the pricing data from the Coinbase API call. Based on the data provided by Coinbase, please recommend an investment strategy. Limit the response to 3 strategies that are concise and provide clear instructions. Show the performance model of each strategy based on the pricing data reviewed.{btc_prompt}{eth_prompt}\n\nBTC-USD price: {btc_price}\nETH-USD price: {eth_price}"
    body = {
        "prompt": prompt,
        "max_tokens": 1000,
        "temperature": 0.9
    }
    response = requests.post(url, headers=headers, json=body)
    result = response.json()
    choices = result.get('choices', [])  # Get the value of 'choices', or an empty list if it doesn't exist
    completion = choices[0]['text'].strip() if choices else ''  # Use an empty string if 'choices' is empty
    return completion

# Create data dictionary
data = {
    "btc_data": btc_data,
    "eth_data": eth_data,
}

# Get investment recommendation
investment_recommendation = get_investment_recommendation(data["btc_data"], data["eth_data"])

# Print investment recommendation
print("Investment Recommendation:", investment_recommendation)
