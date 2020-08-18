#!/usr/bin/env python3
# from functools import reduce
import numpy as np
from model_manager.train_model import train
# from tensorflow.data.Dataset import from_tensor_slices

# import pandas as pd

import pandas_datareader.data as web
from datetime import datetime
# from pandas import Series, DataFrame

start = datetime(2010, 1, 1)
end = datetime(2015, 1, 1)
df = web.DataReader("AAPL", 'yahoo', start, end)
print(df)


def data_to_recurrent(history_points, data):
    """Yield data slices of length given by the history_points.

    :history_points: int
    :data: numpy.ndarray
    :yields: numpy.ndarray

    """
    for index in range(data.shape[0] - history_points - 1):
        yield data[index:index + history_points]


history_points = 50
# print(*map(lambda x: x.to_numpy(), data_to_recurrent(history_points, df)))
data = np.stack(data_to_recurrent(history_points, df))
print(data)
target_data = df['Open'][history_points + 1:].values
print(len(target_data))
print(len(data))
# testing the function
hist, model = train('simple_lstm', x=data, y=target_data)
