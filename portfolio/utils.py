import requests

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "INR",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": True  # Enable sparkline data
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_historical_data(symbol, days=7):
    url = f'https://api.coingecko.com/api/v3/coins/{symbol}/market_chart'
    params = {
        'vs_currency': 'inr',
        'days': days
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        prices = [price[1] for price in data['prices']]
        return prices
    return []
