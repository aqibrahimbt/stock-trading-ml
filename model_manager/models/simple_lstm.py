"""Initial Test."""

from keras.models import Model
from keras.layers import Dense, Dropout, LSTM, Input, Activation

history_points = 200

# simple lstm model architecture
lstm_input = Input(shape=(history_points, 5), name='lstm_input')
x = LSTM(100, name='lstm_0')(lstm_input)
x = Dropout(0.2, name='lstm_dropout_0')(x)
x = Dense(64, name='dense_0')(x)
x = Activation('sigmoid', name='sigmoid_0')(x)
x = Dense(1, name='dense_1')(x)
output = Activation('linear', name='linear_output')(x)

model = Model(inputs=lstm_input, outputs=output)

print(model)
print(model.get_input_at(0).shape)
