from .base import SingleStrategy
from backtrader.indicators import EMA,MACDHisto
from backtest.config import strategys
from backtest.bt import period

test_config = {
    'ma_period' : 15,
    "me_long_period" : 26,
    "me_short_period" :12,
    "macd_period": 9
}
if strategys.get("macd_cross"):
    config = strategys.pop("macd_cross")
else:
    config = test_config

class MacdCross(SingleStrategy):
    params = (
        ('maperiod', config.pop("ma_period")),
    )

    def __init__(self):

        self.time_period = period
        short_me = EMA(self.data, period=config.pop("me_short_period"))
        long_me = EMA(self.data, period=config.pop("me_long_period"))
        self.macd = short_me - long_me
        self.signal = EMA(self.macd, period=config.pop("macd_period"))
        # MACDHisto(self.data)
        super(MacdCross,self).__init__()


    # Python 实用宝典
    def next(self):
        self.log('Close, %.2f' % self.dataclose[0])
        if self.order:
            return
        #import pdb
        #pdb.set_trace()
        if not self.position:
            condition1 = self.macd[-1] - self.signal[-1]
            condition2 = self.macd[0] - self.signal[0]
            if condition1 < 0 and condition2 > 0:
                self.log('BUY CREATE, %.2f' % self.dataclose[0])
                self.order = self.buy()

        else:
            condition = (self.dataclose[0] - self.bar_executed_close) / self.dataclose[0]
            if condition > 0.1 or condition < -0.1:
                self.log('SELL CREATE, %.2f' % self.dataclose[0])
                self.order = self.sell()

