
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def analyze_stock(ticker):
    """
    Analyzes a stock by fetching its historical data, calculating moving averages,
    and plotting the closing price and moving averages.
    """
    # Fetch historical data
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")

    if hist.empty:
        print(f"No data found for ticker {ticker}")
        return

    # Calculate moving averages
    hist['SMA_50'] = hist['Close'].rolling(window=50).mean()
    hist['SMA_200'] = hist['Close'].rolling(window=200).mean()

    # Print historical data
    print("Historical Data (last 5 days):")
    print(hist.tail())

    # Plot closing price and moving averages
    plt.figure(figsize=(12, 6))
    plt.plot(hist['Close'], label='Close Price')
    plt.plot(hist['SMA_50'], label='50-Day SMA')
    plt.plot(hist['SMA_200'], label='200-Day SMA')
    plt.title(f'{ticker} Stock Analysis')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    ticker = input("Enter a stock ticker (e.g., AAPL): ")
    analyze_stock(ticker)
