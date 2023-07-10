import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read the API key from api_key.txt file
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

headers = {
    "CB-ACCESS-KEY": api_key,
}

# Function to retrieve historical data for a given product and time range
def get_historical_data(product_id, start_date, end_date):
    api_url = "https://api.pro.coinbase.com/products"
    candles_url = f"{api_url}/{product_id}/candles"
    params = {
        "start": start_date.isoformat(),
        "end": end_date.isoformat(),
        "granularity": 86400,  # Daily granularity (86400 seconds = 1 day)
    }
    response = requests.get(candles_url, params=params)
    data = response.json()
    return data

# Function to retrieve the current price of a given cryptocurrency
def get_current_price(product_id):
    url = f"https://api.coinbase.com/v2/prices/{product_id}/spot"
    response = requests.get(url, headers=headers)
    data = response.json()
    return float(data['data']['amount'])

# Function to perform DCA investments
def dca_investments(btc_data, eth_data, start_date, end_date, investment_amount, investment_frequency):
    # Retrieve current prices for BTC-USD and ETH-USD
    btc_usd_price = get_current_price("BTC-USD")
    eth_usd_price = get_current_price("ETH-USD")

    # Calculate the number of investment periods
    num_periods = (end_date - start_date).days // investment_frequency.days

    # Initialize investment tracking variables
    total_investment = 0
    investment_values = []

    # Perform DCA investments
    for i in range(num_periods):
        investment_date = start_date + i * investment_frequency
        btc_price = btc_data[i][4]
        eth_price = eth_data[i][4]

        btc_investment = investment_amount / btc_price
        eth_investment = investment_amount / eth_price

        total_investment += investment_amount
        current_value = btc_investment * btc_usd_price + eth_investment * eth_usd_price
        investment_values.append(current_value)

    # Plot investment performance
    investment_dates = [start_date + i * investment_frequency for i in range(num_periods)]

    fig, ax = plt.subplots()
    ax.plot(investment_dates, investment_values)
    ax.set_title("Dollar Cost Averaging (DCA) Investment Performance")
    ax.set_xlabel("Investment Date")
    ax.set_ylabel("Investment Value (USD)")

    # Format x-axis labels as dates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.DayLocator())

    fig.autofmt_xdate()  # Automatically format the x-axis labels to avoid overlapping

    plt.tight_layout()
    plt.show()


# Main function to execute DCA model for the given time period
def main():
    # Calculate the start and end dates
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=30)

    # Retrieve historical data for BTC-USD and ETH-USD
    btc_data = get_historical_data("BTC-USD", start_date, end_date)
    eth_data = get_historical_data("ETH-USD", start_date, end_date)

    # Perform DCA with a 30-day investment period
    dca_investments(btc_data, eth_data, start_date, end_date, investment_amount=1000, investment_frequency=datetime.timedelta(weeks=1))


if __name__ == "__main__":
    main()
