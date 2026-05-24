import yfinance as yf
import pandas as pd


# ticker information
ticker_symbol = "AAPL"
ticker = yf.Ticker(ticker_symbol)
data = ticker.history(period="1d", interval="1m")

# move Datetime index into a normal column
data.reset_index(inplace=True)

# round prices
price_cols = ["Open", "High", "Low", "Close"]
data[price_cols] = data[price_cols].round(2)

# volume as integer
data["Volume"] = data["Volume"].astype(int)

# save csv
data.to_csv("aapl_1min_data.csv", index=False)
print("CSV saved successfully")

# verify
print(data.head())
# print(type(data))
