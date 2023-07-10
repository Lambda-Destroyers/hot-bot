import datetime
import matplotlib.pyplot as plt
from dca_utils import *

# Calculate the start and end dates for the 180-day period
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=180)

# Retrieve historical data for BTC-USD and ETH-USD
btc_data = get_historical_data("BTC-USD", start_date, end_date)
eth_data = get_historical_data("ETH-USD", start_date, end_date)

# Perform DCA with a 180-day investment period
dca_investments(btc_data, eth_data, start_date, end_date, investment_amount=5000, investment_frequency=datetime.timedelta(weeks=4))
