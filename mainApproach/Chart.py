from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt

api = CoinGeckoAPI()

class Chart():
    # constructor for creating objects
    def __init__(self, crypto_id, currency, startDate, endDate):
        self.crypto_id = crypto_id
        self.currency = currency
        self.startDate = startDate
        self.endDate = endDate

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

        # turn timestamps of list 'date' into actual dates and not timestamps

        #######
        # needs to be added
        #######

        # visualize our two lists with matplotlib
        plt.plot(date, price)
        plt.show()