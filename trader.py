import yfinance as yf
import pandas as pd
from collections import deque

NUM_OF_DAYS = 5


'''
# Ticker Class
class Ticker:
    def __init__(self, ticker, day, interval):
        self.ticker_symbol = ticker
        self.day = day
        self.interval = interval
    
    def moving_avg()


'''

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

# add sequence id
data["Sequence"] = range(1, len(data) + 1)

# save csv
data.to_csv("aapl_1min_data.csv", index=False)
print("CSV saved successfully")

close_prices = data["Close"]
closing_bucket = deque()

# change to fixed point
close_prices = (close_prices * 100).astype("uint32")

# seed
for i in range(NUM_OF_DAYS):
    closing_bucket.append(close_prices.iloc[i])
    
running_sum = sum(closing_bucket)

# average for first 5 days
average = running_sum / NUM_OF_DAYS

# limit order algorithm
for i in range(0, len(close_prices)):
    current_price = close_prices.iloc[i]
    average = running_sum // NUM_OF_DAYS
    
    # buy when current price is lower (limit order)
    threshold = 999

    # print(f"{current_price} and {average}")
    
    if current_price * 1000 < average * threshold:
        print("BUY")
        # place_buy_limit_order()
        #print(f"bought! {current_price}")
        pass
    
    remove_price = closing_bucket.popleft()
    closing_bucket.append(current_price)

    running_sum -= remove_price
    running_sum += current_price

