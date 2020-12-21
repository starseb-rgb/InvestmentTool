from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

api = CoinGeckoAPI()

class Chart():

    # constructor for creating objects
    # mas = moving average short
    def __init__(self, crypto_id, currency, startDate, endDate, mas, mal):
        self.crypto_id = crypto_id
        self.currency = currency
        self.startDate = startDate
        self.endDate = endDate
        self.mas = mas
        self.mal = mal

    def createChart(self):

        crypto = api.get_coin_market_chart_range_by_id(id=self.crypto_id, vs_currency=self.currency, from_timestamp=self.startDate, to_timestamp=self.endDate)
        # a few annotations to the request above:
            # id = pass the coin id (can be obtained from /coins) eg. bitcoin
            # vs_currency = The target currency of market data (usd, eur, jpy, etc.)
            # from_timestamp = start date in unix timestamp format
            # to_timestamp = end date in unix timestamp format

        # for plotting our data with matplotlib, we transform 'btc' of type dict into two lists

        # step1: turn 'crypto' into list
        crypto_list = []
        for i in crypto.values():
            crypto_list.append(i)

        # create new list with values only belonging to first key of the initial ditcionary
        crypto_list = crypto_list[0]

        # step2: split 'crypto_list' into two lists
        date, price = map(list, zip(*crypto_list))

        # turn timestamps of list 'date' into actual dates

        #######
        # needs to be added
        #######

        # visualize our two lists with matplotlib
        # weights = np.repeat(1.0, 50)/50
        # smas = np.convolve(price, weights, 'valid')

        # print(smas)


        # ------------------------------
        # moving average calculation
        # ------------------------------

        # two new empty lists which will be filled with moving averages
        movingAverageShort = []
        movingAverageLong = []

        # start filling movingAverageShort with moving averages
        i = 0
        m = 0

        while i < len(price[:-self.mas+1]):
            while m < self.mas-1:
                if m == 0:
                    avg = price[0]
                else:
                    avg = sum(price[0:m+1])/(m+1)
                movingAverageShort.append(avg)
                m += 1

            avg = sum(price[i:self.mas+i])/self.mas
            movingAverageShort.append(avg)
            i += 1

        # start filling movingAverageLong with moving averages
        i = 0
        m = 0

        while i < len(price[:-self.mal + 1]):
            while m < self.mal - 1:
                if m == 0:
                    avg = price[0]
                else:
                    avg = sum(price[0:m + 1]) / (m + 1)
                movingAverageLong.append(avg)
                m += 1

            avg = sum(price[i:self.mal + i]) / self.mal
            movingAverageLong.append(avg)
            i += 1




        plt.plot(date, price)
        plt.plot(date, movingAverageShort)
        plt.plot(date, movingAverageLong)
        plt.show()