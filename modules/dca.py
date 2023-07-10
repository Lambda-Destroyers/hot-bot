import requests
import json
import time
import math
import logging
import threading

from bard.api import BardAPI


def get_latest_prices():
    """Gets the latest prices for Ethereum and Bitcoin."""

    response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD")
    if response.status_code == 200:
        return json.loads(response.content)["data"]["price"]
    else:
        return None


def dollar_cost_average():
    """Dollar cost averages Ethereum at a fixed amount per day."""

    investment_amount = 100

    while True:
        price = get_latest_prices()
        if price is not None:
            num_shares_to_buy = investment_amount / price
            logging.info(
                "Buying {} shares of Ethereum at ${}".format(num_shares_to_buy, price)
            )

        time.sleep(24 * 60 * 60)


def main():
    """Runs the dollar cost averaging algorithm."""

    api = BardAPI("YOUR_API_KEY")

    threading.Thread(target=dollar_cost_average).start()

    while True:
        time.sleep(60)


if __name__ == "__main__":
    main()