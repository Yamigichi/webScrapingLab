#!pip install pandas
!pip install yfinance

import yfinance as yf
import pandas as pd

apple = yf.Ticker("AAPL") #ticker allows us to access functionss to extract data.

apple_info=apple.info
apple_info

apple_info['country']

#Extracting Share Price/Using history method we can get the share price
#using period paramters we can set how far from the present to get data.
apple_share_price_data = apple.history(period="max")

# With the Date as the index the share Open, High, Low, Close, Volume, and Stock Splits are given for each day.
apple_share_price_data.head()

#Reset Dataframe using the reset_index

apple_share_price_data.reset_index(inplace=True)

#plotting the open price aginst the date:
apple_share_price_data.plot(x="Date", y="Open")

#Extracting Dividends

apple.dividens

#plot over time
apple.dividens.plot()







