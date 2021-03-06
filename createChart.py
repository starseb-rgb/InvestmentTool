########################################
# run 'main.py' to execute the project #
########################################

from pycoingecko import CoinGeckoAPI
import datetime as dt
import numpy as np



##############################################################################
# this class contains our main logic (API call, transformations, calculations)
##############################################################################

api = CoinGeckoAPI()

class Chart():

    # constructor for creating objects
    # mas = moving average short & mal = moving average long
    def __init__(self, crypto_id, currency, startDate, endDate, mas, mal):
        self.crypto_id = crypto_id
        self.currency = currency
        self.startDate = startDate
        self.endDate = endDate
        self.mas = mas
        self.mal = mal


    def callAPI(self):

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
        for index, ts in enumerate(date):
           date[index] = dt.datetime.fromtimestamp(int(ts)/1000).date()

        result = [date, price]
        return result


    def calculateMA(self, price):
        # moving average calculation

        # two new empty lists which will be filled with moving averages
        movingAverageShort = []
        movingAverageLong = []

        # start filling movingAverageShort with moving averages
        i = 0
        m = 0

        while i < len(price[:-self.mas + 1]):
            while m < self.mas - 1:
                if m == 0:
                    avg = price[0]
                else:
                    avg = sum(price[0:m + 1]) / (m + 1)
                movingAverageShort.append(avg)
                m += 1

            avg = sum(price[i:self.mas + i]) / self.mas
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

        result = [movingAverageShort, movingAverageLong]
        return result


    def calculateInvestmentSignals(self, price, movingAverageShort, movingAverageLong):
        # Implementation of BUY and SELL signals
        # DUAL MOVING AVERAGE CROSSOVER
        #   ... BUY when short-term average crosses long-term average and rises ABOVE it
        #   ... SELL when short-term average crosses long-term average and falls BELOW it

        buyPrice = []
        sellPrice = []
        # variable 'state' to define in which state we currently are
        state = -1

        for i in range(len(price)):
            if movingAverageLong[i] < movingAverageShort[i]:
                if state != 1:
                    buyPrice.append(price[i])
                    sellPrice.append(np.nan)
                    state = 1
                else:
                    buyPrice.append(np.nan)
                    sellPrice.append(np.nan)
            elif movingAverageShort[i] < movingAverageLong[i]:
                if state != 0:
                    buyPrice.append(np.nan)
                    sellPrice.append(price[i])
                    state = 0
                else:
                    buyPrice.append(np.nan)
                    sellPrice.append(np.nan)
            else:
                buyPrice.append(np.nan)
                sellPrice.append(np.nan)

        result = [buyPrice, sellPrice]
        return result