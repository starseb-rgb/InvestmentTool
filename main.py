from createChart import Chart

if __name__=="__main__":

    btc = Chart('bitcoin', 'eur', '1448150400', '1606003200', 15, 300)
    btc.createChart()

    # sample data: 01/01/2020 --> 1577836800    01/02/2020 --> 1580515200
    # sample data: 01/11/2020 --> 1604188800    22/11/2020 --> 1606003200
    # sample data: 22/11/2015 --> 1448150400
