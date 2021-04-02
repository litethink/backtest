from backtrader import Cerebro

from backtest.const import SIZER_MAPS,TIME_FRAME_MAPS
from backtest.config import operations

test_config = {
    "plot" : True,
    "time_period" : "minutes",
    "init_cash" :1000000,
    "sizer" :"fixed",
    "commission" : 0.005,
    "stake" : 1
}


if operations:
    config = operations
else:
    config = test_config
period = TIME_FRAME_MAPS[config.pop("time_period").upper()]

class BackTesting(Cerebro):
    period = period
    def run(self,**kwargs):
        if kwargs.get("strategy"):
            self.add_strategy(kwargs.pop("strategy"))
        #kwargs.get will raise NoneError 
        if "data" in kwargs:
            self.add_data(kwargs.pop("data"))
        self.broker.setcash(config.pop("init_cash"))
        sizer = SIZER_MAPS[config.pop("sizer").upper()]
        self.addsizer(sizer, stake=config.pop("stake"))
        self.broker.setcommission(commission=config.pop("commission"))
        super(BackTesting,self).run()
        plot = config.pop("plot")
        if plot:
            self.plot()

    def add_strategy(self,strategy):
        super(BackTesting,self).addstrategy(strategy)
    def add_data(self,data):
    	super(BackTesting,self).adddata(data)



bt = BackTesting()
