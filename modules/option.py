from rich.console import Console
console = Console()
from modules.investment_recommendation import get_investment_recommendation

def user_option(btc_data, eth_data, btc_opens, btc_highs, btc_lows, btc_closes, eth_opens, eth_highs, eth_lows, eth_closes, gpt_api, days, option):
    investment_recommendation = get_investment_recommendation(btc_data, eth_data, btc_opens, btc_highs, btc_lows, btc_closes, eth_opens, eth_highs, eth_lows, eth_closes, gpt_api, option)

    print("\nInvestment Recommendation:", investment_recommendation)
    return