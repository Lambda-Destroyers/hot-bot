from rich.console import Console
console = Console()
from modules.investment_recommendation import get_investment_recommendation

def user_option(btc_data, eth_data, btc_opens, btc_highs, btc_lows, btc_closes, eth_opens, eth_highs, eth_lows, eth_closes, gpt_api, option):
    investment_recommendation = get_investment_recommendation(btc_data, eth_data, btc_opens, btc_highs, btc_lows, btc_closes, eth_opens, eth_highs, eth_lows, eth_closes, gpt_api, option)

    # Print investment recommendation
    print("Investment Recommendation:", investment_recommendation)
    console.print('Press "enter" to exit')