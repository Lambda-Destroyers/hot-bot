import requests
from modules.GPTtest30 import btc_data

def get_investment_recommendation(btc_data, eth_data, btc_opens, btc_highs, btc_lows, btc_closes, eth_opens, eth_highs, eth_lows, eth_closes, gpt_api, option_choice):
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {gpt_api}",
    }
    btc_price = btc_data[0][4]
    eth_price = eth_data[0][4]
    btc_prompt = f"\n\nBTC-USD historical data:\n- Opens: {btc_opens}\n- Highs: {btc_highs}\n- Lows: {btc_lows}\n- Closes: {btc_closes}"
    eth_prompt = f"\n\nETH-USD historical data:\n- Opens: {eth_opens}\n- Highs: {eth_highs}\n- Lows: {eth_lows}\n- Closes: {eth_closes}"
    prompt = f"Analyze the pricing data from the Coinbase API call. Based on the data provided by Coinbase, please recommend an investment strategy {option_choice}. Limit the response to 3 strategies that are concise and provide clear instructions. Show the performance model of each strategy based on the pricing data reviewed.{btc_prompt}{eth_prompt}\n\nBTC-USD price: {btc_price}\nETH-USD price: {eth_price}"
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
