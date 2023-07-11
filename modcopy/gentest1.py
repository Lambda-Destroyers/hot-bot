import datetime
import matplotlib.pyplot as plt
from dca_utils import *
from thrtydys import get_historical_data

# Calculate the start and end dates for the 30-day period
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=30)

# Retrieve historical data for BTC-USD and ETH-USD
btc_data = get_historical_data("BTC-USD", start_date, end_date)
eth_data = get_historical_data("ETH-USD", start_date, end_date)

# Perform DCA with a 30-day investment period
investment_amount = 1000
investment_frequency = datetime.timedelta(weeks=1)
results = dca_investments(btc_data, eth_data, start_date, end_date, investment_amount, investment_frequency)

# Calculate the rate of return
initial_investment = investment_amount * len(results)
final_portfolio_value = results[-1]['portfolio_value']
rate_of_return = (final_portfolio_value - initial_investment) / initial_investment * 100

# Display rate of return
print("Rate of Return: {:.2f}%".format(rate_of_return))

# Display summary of trades
print("Summary of Trades:")
for trade in results:
    print("Date: {}, Investment: ${:.2f}, Portfolio Value: ${:.2f}".format(trade['date'], trade['investment'], trade['portfolio_value']))

# Extract BTC-USD prices
btc_prices = [entry['price'] for entry in btc_data]

# Extract ETH-USD prices
eth_prices = [entry['price'] for entry in eth_data]

# Calculate high, low, and average prices
btc_high = max(btc_prices)
btc_low = min(btc_prices)
btc_avg = sum(btc_prices) / len(btc_prices)

eth_high = max(eth_prices)
eth_low = min(eth_prices)
eth_avg = sum(eth_prices) / len(eth_prices)

# Display high, low, and average prices
print("BTC-USD Prices - High: ${:.2f}, Low: ${:.2f}, Average: ${:.2f}".format(btc_high, btc_low, btc_avg))
print("ETH-USD Prices - High: ${:.2f}, Low: ${:.2f}, Average: ${:.2f}".format(eth_high, eth_low, eth_avg))
