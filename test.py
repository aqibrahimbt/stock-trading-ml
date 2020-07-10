#!/usr/bin/env python3
from model_manager.train_model import train

from util import csv_to_dataset

# dataset
ohlcv_histories, _, next_day_open_values, unscaled_y, y_normaliser = csv_to_dataset(
    'IBM_daily.csv')

test_split = 0.9
n = int(ohlcv_histories.shape[0] * test_split)

ohlcv_train = ohlcv_histories[:n]
y_train = next_day_open_values[:n]

ohlcv_test = ohlcv_histories[n:]
y_test = next_day_open_values[n:]

unscaled_y_test = unscaled_y[n:]

# testing the function
hist, model = train('simple_lstm', x=ohlcv_train, y=y_train)
