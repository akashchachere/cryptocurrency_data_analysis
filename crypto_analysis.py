import pandas as pd

def analyze_crypto_data():
    """Perform basic analysis on the cryptocurrency data."""
    try:
        df = pd.read_csv("crypto_data.csv")

        # Top 5 cryptocurrencies by market cap
        top_5_by_market_cap = df.nlargest(5, 'Market Capitalization')

        # Average price of the top 50 cryptocurrencies
        average_price = df['Current Price (USD)'].mean()

        # Highest and lowest 24-hour percentage price change
        highest_change = df['Price Change (24-hour, %)'].max()
        lowest_change = df['Price Change (24-hour, %)'].min()

        # Save analysis results
        analysis_results = f"""
        Cryptocurrency Analysis Report:
        ---------------------------------
        Top 5 Cryptocurrencies by Market Cap:
        {top_5_by_market_cap[['Cryptocurrency Name', 'Market Capitalization']]}

        Average Price of Top 50 Cryptocurrencies: ${average_price:.2f}

        Highest 24h Percentage Price Change: {highest_change:.2f}%
        Lowest 24h Percentage Price Change: {lowest_change:.2f}%
        """

        with open("crypto_analysis.txt", "w") as f:
            f.write(analysis_results)

        print("Analysis report saved to crypto_analysis.txt")

    except FileNotFoundError:
        print("Error: crypto_data.csv not found. Please run fetch_crypto_data.py first.")

if __name__ == "__main__":
    analyze_crypto_data()
