import pytest
from unittest.mock import patch
from modules.current_price import get_current_price
from modules.gpt_controller import get_prices
from modules.historical_getter import get_historical_data
from modules.investment_recommendation import get_investment_recommendation
from modules.option import user_option

@pytest.fixture
def mock_requests_get():
    with patch('modules.current_price.requests.get') as mock_get:
        yield mock_get

@pytest.fixture
def mock_requests_post():
    with patch('modules.investment_recommendation.requests.post') as mock_post:
        yield mock_post

def test_get_current_price(mock_requests_get):
    mock_response = mock_requests_get.return_value
    mock_response.json.return_value = {
        'data': {
            'amount': '10000.00'
        }
    }

    product_id = 'BTC-USD'
    headers = {}
    price = get_current_price(product_id, headers)
    assert price == '10000.00'
    mock_requests_get.assert_called_once()

# def test_get_prices(mock_requests_get, mock_requests_post):
#     days = '30'
#     option = 'conservative'
#     btc_usd_price = {'data': {'amount': '10000.00'}}
#     eth_usd_price = {'data': {'amount': '2000.00'}}
#     btc_data = [
#         [0, 5000, 6000, 4000, 5500],
#         [1, 6000, 7000, 5000, 6500],
#         # ...
#     ]
#     eth_data = [
#         [0, 150, 200, 100, 180],
#         [1, 200, 250, 150, 220],
#         # ...
#     ]
#     mock_requests_get.side_effect = [btc_usd_price, eth_usd_price]
#     mock_requests_post.return_value.json.return_value = {
#         'choices': [
#             {'text': 'Recommendation'}
#         ]
#     }

#     get_prices(days, option)

#     mock_requests_get.assert_called_with('https://api.coinbase.com/v2/prices/BTC-USD/spot', headers={})
#     mock_requests_get.assert_called_with('https://api.coinbase.com/v2/prices/ETH-USD/spot', headers={})
#     mock_requests_post.assert_called_once()

# def test_get_historical_data(mock_requests_get):
#     mock_response = mock_requests_get.return_value
#     mock_response.json.return_value = [
#         [0, 5000, 6000, 4000, 5500],
#         [1, 6000, 7000, 5000, 6500],
#         # ...
#     ]

#     product_id = 'BTC-USD'
#     api_url = 'https://api.pro.coinbase.com/products'
#     start_date = "2022-01-01"
#     end_date = "2022-01-30"
#     data = get_historical_data(product_id, api_url, start_date, end_date)
#     assert data == [
#         [0, 5000, 6000, 4000, 5500],
#         [1, 6000, 7000, 5000, 6500],
#         # ...
#     ]
#     mock_requests_get.assert_called_once()

def test_get_investment_recommendation(mock_requests_post):
    mock_response = mock_requests_post.return_value
    mock_response.json.return_value = {
        'choices': [
            {'text': 'Recommendation'}
        ]
    }

    btc_data = [
        [0, 5000, 6000, 4000, 5500],
        [1, 6000, 7000, 5000, 6500],
        # ...
    ]
    eth_data = [
        [0, 150, 200, 100, 180],
        [1, 200, 250, 150, 220],
        # ...
    ]
    btc_opens = [5000, 6000, ...]
    btc_highs = [6000, 7000, ...]
    btc_lows = [4000, 5000, ...]
    btc_closes = [5500, 6500, ...]
    eth_opens = [150, 200, ...]
    eth_highs = [200, 250, ...]
    eth_lows = [100, 150, ...]
    eth_closes = [180, 220, ...]
    gpt_api = 'API_KEY'
    option = 'conservative'

    recommendation = get_investment_recommendation(
        btc_data, eth_data, btc_opens, btc_highs, btc_lows, btc_closes,
        eth_opens, eth_highs, eth_lows, eth_closes, gpt_api, option
    )

    assert recommendation == 'Recommendation'
    mock_requests_post.assert_called_once()

def test_user_option(mock_requests_post):
    btc_data = [
        [0, 5000, 6000, 4000, 5500],
        [1, 6000, 7000, 5000, 6500],
        # ...
    ]
    eth_data = [
        [0, 150, 200, 100, 180],
        [1, 200, 250, 150, 220],
        # ...
    ]
    btc_opens = [5000, 6000, ...]
    btc_highs = [6000, 7000, ...]
    btc_lows = [4000, 5000, ...]
    btc_closes = [5500, 6500, ...]
    eth_opens = [150, 200, ...]
    eth_highs = [200, 250, ...]
    eth_lows = [100, 150, ...]
    eth_closes = [180, 220, ...]
    gpt_api = 'API_KEY'
    days = '30'
    option = 'conservative'

    user_option(
        btc_data, eth_data, btc_opens, btc_highs, btc_lows, btc_closes,
        eth_opens, eth_highs, eth_lows, eth_closes, gpt_api, days, option
    )

    mock_requests_post.assert_called_once()

# Additional test cases

def test_get_current_price_error(mock_requests_get):
    mock_requests_get.return_value.json.side_effect = ValueError

    product_id = 'BTC-USD'
    headers = {}
    with pytest.raises(ValueError):
        get_current_price(product_id, headers)

    mock_requests_get.assert_called_once()

# def test_get_historical_data_error(mock_requests_get):
#     mock_requests_get.return_value.json.side_effect = ValueError

#     product_id = 'BTC-USD'
#     api_url = 'https://api.pro.coinbase.com/products'
#     start_date = "2022-01-01"
#     end_date = "2022-01-30"
#     with pytest.raises(ValueError):
#         get_historical_data(product_id, api_url, start_date, end_date)

#     mock_requests_get.assert_called_once()

# Run all the tests
pytest.main()
