"""Module that provides different preprocessing utils for stock data."""
# TODO: module still needs basic testing

import pandas as pd  # pandas ist das neue numpy
import tensorflow as tf

# factor to provide padding for normalized stock data
MARGIN_FACTOR = 0.8


def normalize_stock_data(df):
    """Normalizes a given stock timeseries."""
    # normalize the volume data individually
    df['Volume'] = df['Volume'] / max(df['Volume'])
    rest = df.loc[:, ['High', 'Low', 'Open', 'Close', 'Adj Close']]
    rest = rest / max(df['High'])
    rest *= MARGIN_FACTOR


def data_to_recurrent(history_points, df):
    """Yield data slices of length given by the history_points.

    :history_points: int
    :data: pandas.DataFrame
    :yields: (pandas.DataFrame, pandas.DataFrame)

    """
    for ind in range(df.shape[0] - history_points - 1):
        print(df.iloc[ind:ind + history_points, :])
        print(
            ind,
            pd.DataFrame({
                'x': df.iloc[ind:ind + history_points, :],
                'y': df.iloc[ind + history_points + 1, :]
            }))

        yield pd.DataFrame({
            'x': df.iloc[ind:ind + history_points, :],
            'y': df.iloc[ind + history_points + 1, :]
        })


def prepare_stock_data(df, history_points=50, validation_split=0.8):
    """Prepares stock data to train RNNs with tensorflow."""
    # normalize the stock data (the memory address is passed: no return)
    normalize_stock_data(df)

    # make the dataset suitable for RNNs
    df = pd.concat(data_to_recurrent(history_points, df), axis=1)

    # split the data into training and validation data
    train = tf.constant(df.iloc[:int(len(df) * validation_split), :])
    test = tf.constant(df.iloc[int(len(df) * validation_split), :])
    print(train, test)
    return train, test


def joined_recurrent_stock_data(*args):
    """TODO: Docstring for joined_recurrent_stock_data.

    :param args: pandas.DataFrame
    :returns: tensorflow.tensor

    """
    return tf.hstack(*args)
