import json
import os
from backtest.const import CONFIG_FILE_NAME
class Config:
    # def __init__(self,config_file = None):
    #     self.config_file = config_file
    def __call__(self,**kwargs):
        if kwargs.get("config_file"):
            return self.__load__(kwargs.pop("config_file"))
        raise  NameError("Need a name of json file!")

    def __load__(self,config_file=None):
        #self.config_file = config_file
        if config_file:
            try:
                with open(os.path.abspath(config_file),"r") as f:
                    data = f.read()
                    configures = json.loads(data)
                    return configures
            except Exception as e:
                print(e)
                exit(0)
            if not configures:
                print("config json file error!")
                exit(0)

config = Config()(config_file=CONFIG_FILE_NAME)
strategys = config.pop("strategy_set")
operations = config.pop("operations")
dataset = config.pop("data_set")
