
import tushare as ts
from  datetime import datetime
from backtest.strategy import VwapCross
from backtest.dataset import CustomCsvData
from backtest import bt

data = CustomCsvData(
    timeframe=bt.period,
    #from 2018-9-20
    fromdate=datetime(2018,9, 20),
    todate=datetime(2019, 1,1 ),
    compression=1
)
if __name__ == "__main__":

    #bt.resampledata(data, timeframe=bt.period, compression=10)
    bt.add_data(data)
    bt.add_strategy(VwapCross)
    bt.run()
    print('Finally property: {}.'.format(round(bt.broker.getvalue(),2)))

