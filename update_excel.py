import requests
import pandas as pd
import time
import openpyxl

def update_excel():
    """Fetch and update live cryptocurrency data in an Excel file every 5 minutes."""
    excel_filename = "live_crypto_data.xlsx"

    while True:
        try:
            # Fetch live data
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
                df.columns = ['Cryptocurrency Name', 'Symbol', 'Current Price (USD)', 'Market Capitalization', '24-hour Trading Volume', 'Price Change (24-hour, %)']

                # Save data to Excel
                df.to_excel(excel_filename, index=False)
                print("Live cryptocurrency data updated in", excel_filename)
            else:
                print("Failed to fetch data")

        except Exception as e:
            print("Error:", str(e))

        # Wait for 5 minutes before next update
        time.sleep(300)

if __name__ == "__main__":
    update_excel()
