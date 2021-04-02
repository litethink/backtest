from backtrader import indicators as inds
from backtrader import Indicator
class VolumeWeightedAveragePrice(Indicator):
    plotinfo = dict(subplot=False)

    params = (('period', 30), )

    alias = ('VWAP', 'VolumeWeightedAveragePrice',)
    lines = ('VWAP',)
    plotlines = dict(VWAP=dict(linestyle='-', alpha=0.50, linewidth=2.0))
    plotinfo = dict(subplot=False)


    def __init__(self):
        typical_price = (self.data.close + self.data.high + self.data.low)/3
        typical_price_volume = typical_price * self.data.volume
        total_volume = inds.SumN(self.data.volume, period = self.p.period)
        total_pv = inds.SumN(typical_price_volume, period = self.p.period)
        self.lines[0] = total_pv / total_volume

        super(VolumeWeightedAveragePrice, self).__init__()



