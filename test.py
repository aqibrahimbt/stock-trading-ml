#!/usr/bin/env python3

from model_manager.train_model import train
from preprocessing_utils import prepare_stock_data

import matplotlib.pyplot as plt

import pandas_datareader.data as web
from datetime import datetime

start = datetime(2010, 1, 1)
end = datetime(2020, 8, 21)
df = web.DataReader("TSLA", 'yahoo', start, end)
df2 = web.DataReader("AAPL", "yahoo", start, end)

print(prepare_stock_data(df))

# # testing the function
# hist, model = train('convolutional_model', x=data, y=target_data, epochs=4)
# print(hist)
# hf = DataFrame(hist.history)

# hf.plot(kind='line', y=['loss', 'val_loss'])
# plt.show()
