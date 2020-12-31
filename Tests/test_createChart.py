from createChart import Chart
import datetime
import numpy as np

def test_callAPI():
    # create 'mock-object' only for testing purposes
    coin = Chart('bitcoin', 'eur', '1448150400', '1448150401', 60, 200)
    data = coin.callAPI()
    date = data[0]
    price = data[1]

    assert type(coin.callAPI())== list

    for i in date:
        assert type(i) == datetime.date

    for i in price:
        assert type(i) == float

def test_calculateMA():
    coin = Chart('bitcoin', 'eur', '1448150400', '1448150401', 2, 5)
    averages = coin.calculateMA([1,2,3,4,5,6,7,8,9,10])
    short = averages[0]
    long = averages[1]

    assert short == [1, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
    assert long == [1, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8]

def test_calculateInvestmentSignals():
    coin = Chart('bitcoin', 'eur', '1448150400', '1448150401', 2, 5)
    prices = [50, 75, 75, 100, 150, 250, 100, 150, 50, 100]
    maShort = [50, 50, 75, 100, 100, 100, 75, 50, 50, 50]
    maLong = [100, 100, 74, 50, 50, 50, 76, 100, 100, 100]
    signals = coin.calculateInvestmentSignals(prices, maShort, maLong)
    buy = signals[0]
    sell = signals[1]

    assert buy == [np.nan, np.nan, 75, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
    assert sell == [50, np.nan, np.nan, np.nan, np.nan, np.nan, 100, np.nan, np.nan, np.nan]







