#!/usr/bin/env python3
from model_manager.train_model import train

import pandas as pd

import panda_datareader.data as web
from datetime import datetime
from pandas import Series, DataFrame

start = datetime(2010, 1, 1)
end = datetime(2015, 1, 1)
df = web.DataReader("AAPL", 'yahoo', start, end)

data_split = 0.9
n = int(df.shape[0] * data_split)

# testing the function
hist, model = train('simple_lstm', x=ohlcv_train, y=y_train)
