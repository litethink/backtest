from .base import SingleStrategy
from backtrader.indicators import SMA,WMA
from backtest.config import strategys
from backtest.bt import period
test_config = {
    'ma_indicator' : "wma",
    "period_short" : 300,
    "period_long" :600
}

ma_indis = {
    "wma" :WMA,
    "sma" :SMA
}

if strategys.get("double_average"):
    config = strategys.pop("double_average")
else:
    config = test_config
class DoubleAverage(SingleStrategy):

    params = (
        ('period_long', config.pop('period_long')),
        ('period_short', config.pop('period_short'))
    )
        

    def __init__(self):
        self.time_period = period
        #
        super(DoubleAverage,self).__init__()
        self.ma_short = ma_indis[config.get("ma_indicator")](self.dataclose, period=self.params.period_short)
        # 
        self.ma_long = ma_indis[config.get("ma_indicator")](self.dataclose, period=self.params.period_long)

    def next(self):
        if self.order:
            return 
        # 当今天的10日均线大于30日均线并且昨天的10日均线小于30日均线，则进入市场（买）
        if self.ma_short[0] < self.ma_long[0] and self.ma_short[-1] > self.ma_long[-1]:
            # 判断订单是否完成，完成则为None，否则为订单信息


            #若上一个订单处理完成，可继续执行买入操作
            if self.position:
                self.order = self.sell()
            
        # 当今天的10日均线小于30日均线并且昨天的10日均线大于30日均线，则退出市场（卖）
        elif self.ma_short[0] > self.ma_long[0] and self.ma_short[-1] < self.ma_long[-1]:
                # 卖出


            if not self.position:
                self.order = self.buy()