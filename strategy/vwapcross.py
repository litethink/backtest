from .base import SingleStrategy
from backtrader.indicators import SMA,WMA
from backtest.indicators import VolumeWeightedAveragePrice 
from backtest.config import strategys
from backtest.bt import period
test_config = {
    'ma_indicator' : "wma",
    "vwap_period" :1000,
    "ma_period_short" : 30,
    "ma_period_long" :150

}

ma_indis = {
    "wma" :WMA,
    "sma" :SMA
}

if strategys.get("vwap_cross"):
    config = strategys.pop("vwap_cross")
else:
    config = test_config
class VwapCross(SingleStrategy):

    params = (
        ("vwap_period", config.pop("vwap_period")),
        ('ma_period_long', config.pop('ma_period_long')),
        ('ma_period_short', config.pop('ma_period_short'))
    )
        

    def __init__(self):
        self.time_period = period
    

        super(VwapCross,self).__init__()
        self.ma_short = ma_indis[config.get("ma_indicator")](self.dataclose, period=self.params.ma_period_short)
        # 
        self.ma_long = ma_indis[config.get("ma_indicator")](self.dataclose, period=self.params.ma_period_long)
        self.vwap = VolumeWeightedAveragePrice(self.data,period=self.params.vwap_period)

        # 策略逻辑实现
    def next(self):
        if self.order:
            return
        # import pdb
        # pdb.set_trace()
        if (self.ma_short[0] < self.vwap[0]) and (self.ma_long[0] < self.vwap[0]):
        # 当今天的short均线大于long均线并且昨天的short均线小于long均线，则买
            if (self.ma_short[0] > self.ma_long[0]) and (self.ma_short[-1] < self.ma_long[-1]):
                #real
                if not self.position:
                    self.order = self.buy()
                    return
                    
                # if self.position:
                #     self.order = self.sell()    
                #     return  


            elif (self.ma_short[0] < self.ma_long[0]) and (self.ma_short[-1] > self.ma_long[-1]):
                #real
                if self.position:
                    self.order = self.sell()    
                    return  
                # if not self.position:
                #     self.order = self.buy()
                #     return

            
        # 当今天的10日均线小于30日均线并且昨天的10日均线大于30日均线，则退出市场(卖）
        elif (self.ma_short[0] > self.vwap[0]) and (self.ma_short[-1] < self.vwap[-1]):
            if self.position:
                self.order = self.sell()
                return

        elif self.ma_short[0] > self.vwap[0]:
            if self.position:
                self.order = self.sell()
                return