import requests
import pandas as pd


def fetch_crypto_data():
    """Fetch live data for the top 50 cryptocurrencies from CoinGecko API."""
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 50,
        'page': 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)

        # Select necessary columns
        df = df[['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]
        df.columns = ['Cryptocurrency Name', 'Symbol', 'Current Price (USD)', 'Market Capitalization',
                      '24-hour Trading Volume', 'Price Change (24-hour, %)']

        # Save data as CSV
        df.to_csv("crypto_data.csv", index=False)
        print("Live cryptocurrency data saved to crypto_data.csv")
        return df
    else:
        print("Failed to fetch data")
        return None


if __name__ == "__main__":
    fetch_crypto_data()
