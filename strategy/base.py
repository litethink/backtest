from backtrader import Strategy
from backtrader import TimeFrame
class SingleStrategy(Strategy):

    def log(self, txt):
        print('%s, %s' % (self.log_dt().isoformat(), txt))

    @staticmethod
    def percent(today, yesterday):
        return float(today - yesterday) / today

    def __init__(self):
        if self.time_period in ("days","Days","DAYS"):
            self.log_dt = self.datas[0].datetime.date
        else:
            self.log_dt = self.datas[0].datetime.datetime

        self.dataclose = self.datas[0].close
        self.volume = self.datas[0].volume
        self.order = None
        self.buyprice = None
        self.buycomm = None

    def notify_order(self, order):
        
        # 等待订单提交、订单被cerebro接受
        if order.status in [order.Submitted, order.Accepted]:
            return
        
        # 等待订单完成
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm

                self.bar_executed_close = self.dataclose[0]
            else:
                self.log(
                    'SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))
            self.bar_executed = len(self)
        # 如果订单保证金不足，将不会完成，而是执行以下拒绝程序
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None


    def notify_trade(self, trade):

        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))  # pnl：盈利  pnlcomm：手续费
        