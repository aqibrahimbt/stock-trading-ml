"""Initial Test."""

from keras.models import Model, Sequential
from keras.layers import Dense, Dropout, LSTM, Input, Activation

history_points = 200
shape = (history_points, 5)

model = Sequential()
model.add(LSTM(16, input_shape=shape, name='lstm_0'))
model.add(Dropout(0.5, name='dropout_0'))
model.add(Dense(64, name='dense_1', activation='relu'))
model.add(Dropout(0.5, name='dropout_1'))
model.add(Dense(1, name='dense_2', activation='sigmoid'))

# # simple lstm model architecture
# lstm_input = Input(shape=shape, name='lstm_input')
# x = LSTM(100, name='lstm_0')(lstm_input)
# x = Dropout(0.2, name='lstm_dropout_0')(x)
# x = Dense(64, name='dense_0')(x)
# x = Activation('sigmoid', name='sigmoid_0')(x)
# x = Dense(1, name='dense_1')(x)
# output = Activation('linear', name='linear_output')(x)

# model = Model(inputs=lstm_input, outputs=output)

print(model)
print(model.input_shape)
