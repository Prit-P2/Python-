
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Prompt the user to enter a ticker symbol
if len(sys.argv) > 1:
    ticker_symbol = sys.argv[1]
else:
    ticker_symbol = input("Enter the stock ticker symbol (e.g., RELIANCE.NS, TATAMOTORS.NS): ")

# Check if the user entered a symbol
if not ticker_symbol:
    print("No ticker symbol entered. Exiting.")
else:
    try:
        # Get historical data for the last 5 years
        print(f"Fetching data for {ticker_symbol}...")
        stock_data = yf.download(ticker_symbol, period="5y", progress=False)

        if stock_data.empty:
            print(f"No data found for ticker symbol '{ticker_symbol}'. Please check the symbol and try again.")
        else:
            # Calculate the 50-day and 200-day Simple Moving Averages (SMA)
            stock_data['SMA_50'] = stock_data['Close'].rolling(window=50).mean()
            stock_data['SMA_200'] = stock_data['Close'].rolling(window=200).mean()

            # Create the plot
            plt.figure(figsize=(14, 7))

            # Plot the closing price and the moving averages
            plt.plot(stock_data['Close'], label='Close Price')
            plt.plot(stock_data['SMA_50'], label='50-Day SMA')
            plt.plot(stock_data['SMA_200'], label='200-Day SMA')

            # Add titles and labels for clarity
            plt.title(f'{ticker_symbol} Stock Price Analysis')
            plt.xlabel("Date")
            plt.ylabel("Price (INR)")
            plt.legend()
            plt.grid(True)

            # Save the plot to a file
            # Replace characters that are invalid for filenames
            safe_ticker = "".join(c for c in ticker_symbol if c.isalnum() or c in ('-', '_')).rstrip()
            output_filename = f'{safe_ticker}_analysis.png'
            plt.savefig(output_filename)

            print(f"Analysis chart saved as '{output_filename}'")

    except Exception as e:
        print(f"An error occurred: {e}")
