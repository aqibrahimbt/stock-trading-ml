"""Testing models using only 1D convolutional NNs."""

from keras.models import Sequential
from keras.layers import Dense, Conv1D, MaxPooling1D, Dropout

shape = (50, 5)

# simple cnn model architecture
model = Sequential()
model.add(
    Conv1D(32,
           2,
           padding='valid',
           name='conv_0',
           activation='relu',
           input_shape=shape))
model.add(MaxPooling1D(2, name='max_pooling_0'))
model.add(Dropout(0.2))
model.add(Dense(1, name='dense_1', activation='sigmoid'))

# cnn_input = Input(shape=shape, name='cnn_input')
# x = Conv1D(32, 2, name='convolutional_0', activation='relu')(cnn_input)
# x = MaxPooling1D(2, name='max_pooling_0')(x)
# x = Dropout(0.4, name='cnn_dropout_0')(x)
# x = Dense(5, name='dense_1', activation='tanh')

# model = Model(inputs=cnn_input, outputs=x)

model.summary()
