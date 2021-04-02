from backtrader.feeds import GenericCSVData
from backtest.config import dataset
from backtest.const import DATASET_DIR

csv_test_config = {
    "name": "testcsvdata",
    "dataname" :"binance_nov_18_mar_19_btc.csv",
    # 'time': -1,
    'datetime': 0,
    'open': 1,
    'high': 2,
    'low': 3,
    'close': 4,
    'volume': 5,
    'openinterest': 6
}

if dataset.get("csv_data_set"):
    config = dataset.pop("csv_data_set")
else:
    config = csv_test_config


class CustomCsvData(GenericCSVData):
    params = (
        ('name', config.pop("name")),
       # ('time', config.pop("time")),
        ('dataname', '{}/{}'.format(DATASET_DIR,config.pop("dataname"))),
        ('datetime', config.pop("datetime")),
        ('open', config.pop("open")),
        ('high', config.pop("high")),
        ('low', config.pop("low")),
        ('close', config.pop("close")),
        ('volume', config.pop("volume")),
        ('openinterest', config.pop("openinterest")),
        ('nullvalue',0.0)
    )
