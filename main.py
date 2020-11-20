# INVESTMENT TOOL

# 0) Strategy
# DUAL MOVING AVERAGE CROSSOVER
#   ... BUY when short-term average (7 days) crosses long-term average (25 days) and rises ABOVE it
#   ... SELL when short-term average (7 days) crosses long-term average (25 days) and falls BELOW it

# 1) Import libraries
from PyQt5.QtWidgets import *
from pycoingecko import CoinGeckoAPI as cg
from datetime import datetime
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#plt.style.use('fivethirtyeight')               here we could preset plot style

# 2) Interface
# Interface: Choose a crypto currency
# upload data set with CoinGecko API
# -> print Chart of choosen currency pair

# Wie ich es gemacht hatte (via colab)
# upload data set (btc-usd-max.cvs) we created with CoinGecko API
#from google.colab import files
#uploaded = files.upload()
#bitcoin = pd.read_csv('btc-usd-max.cvs')
#print(bitcoin)

# VISUALIZE CHART
plt.figure(figsize=(13,5))
plt.plot(bitcoin['price'], label= 'Bitcoin')
plt.title('price')
plt.xlabel('28/04/2013 - 20/11/2020')
plt.ylabel('price in $')
plt.legend(loc='upper left')
plt.show()

# 3) INVESTMENT STRATEGY

# MOVING AVERAGE (25 days) change period!
ma25 = pd.DataFrame()
ma25['price'] = bitcoin['price'].rolling(window=25).mean()

# MOVING AVERAGE (7 days) change period!
ma7 = pd.DataFrame()
ma7['price'] = bitcoin['price'].rolling(window=7).mean()

# STORING DATA
data_bitcoin = pd.DataFrame()
data_bitcoin['Bitcoin price'] = bitcoin['price']
data_bitcoin['ma7'] = ma7['price']
data_bitcoin['ma25'] = ma25['price']
print(data_bitcoin)

# BUY & SELL FUNCTION
def buy_sell(data_bitcoin):
  Buy_price = []
  Sell_price = []
  x = -1

  for i in range(len(data_bitcoin)):
    if data_bitcoin['ma25'][i] < data_bitcoin['ma7'][i]:
      if x != 1:
        Buy_price.append(data_bitcoin['Bitcoin price'][i])
        Sell_price.append(np.nan)
        x = 1
      else:
        Buy_price.append(np.nan)
        Sell_price.append(np.nan)
    elif data_bitcoin['ma7'][i] < data_bitcoin['ma25'][i]:
      if x != 0:
        Buy_price.append(np.nan)
        Sell_price.append(data_bitcoin['Bitcoin price'][i])
        x = 0
      else:
        Buy_price.append(np.nan)
        Sell_price.append(np.nan)
    else:
      Buy_price.append(np.nan)
      Sell_price.append(np.nan)

  return (Buy_price, Sell_price)

#STORING BUY AND SELL DATA
buy_sell = buy_sell(data_bitcoin)
data_bitcoin['Buy_price'] = buy_sell[0]
data_bitcoin['Sell_price'] = buy_sell[1]

# ViSUALIZE DATA & STRATEGY
plt.figure(figsize=(13,5))
plt.plot(bitcoin['price'], label = 'Bitcoin', alpha = 0.5)
plt.plot(ma25['price'], label = 'ma25', alpha = 0.5)
plt.plot(ma7['price'], label = 'ma7', alpha = 0.5)
plt.scatter(data_bitcoin.index, data_bitcoin['Buy_price'], label = 'Buy', marker = '^', color = 'green')
plt.scatter(data_bitcoin.index, data_bitcoin['Sell_price'], label = 'Sell', marker = 'v', color = 'red')
plt.title('Bitcoin price')
plt.xlabel('28/04/2013 - 20/11/2020')
plt.ylabel('price in $')
plt.legend(loc='upper left')
plt.show()
