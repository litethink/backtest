from backtrader.sizers import FixedSize
from backtrader import TimeFrame



TIME_FRAME_MAPS = {
    "DAYS" : TimeFrame.Days,
    "MINUTES" : TimeFrame.Minutes,
    "TICKS" :TimeFrame.Ticks

}

SIZER_MAPS = {
    "FIXED" : FixedSize
}

TIME_FRAME_MINUTES = TimeFrame.Minutes
TIME_FRAME_DAYS = TimeFrame.Days
TIME_FRAME_TICKS = TimeFrame.Ticks

DATASET_DIR = "dataset" 
CONFIG_FILE_NAME = "config.json"