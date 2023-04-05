import yfinance as yf
import pandas as pd
import matplotlib

# Using the Ticker module we can create an object that will allow us to access functions to extract data.
## Provide the ticker symbol for the stock, for Apple the ticker symbol is *AAPL*
apple = yf.Ticker("AAPL")

# Go on terminal and using the following cmd, get the functions and variables to extract the type of data we need. (access https://aroussi.com/post/python-yahoo-finance to view them and what they represent here )
## !wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json

import json
with open(r"C:\Users\Filipe\Documents\Python\apple.json") as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable
    # Print ("Type:", type(apple_info))
print("Type:", type(apple_info))

# Get the 'country' using the key country
print(apple_info['country'])

# Extracting share price (the single smallest part of a company's stock that you can buy)
# The history() method get the share price of the stock over a certain period of time
# The period parameter we can set how far back from the present to get data. The options are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
apple_share_price_data = apple.history(period="10y")

apple_share_price_data.head()

apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="Open")