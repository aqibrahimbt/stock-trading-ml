"""Module to manage the training of different ML models."""

from datetime import datetime
from keras import optimizers, callbacks
from model_manager.initiate_models import initialize_model

kwargs_default_compile = {
    'optimizer': optimizers.Adam(lr=.0005),
    'loss': 'mse'
}

log_dir = 'logs/fit/' + datetime.now().stftime('%Y%m%d-%H%M%S')
tensorboard_callback = callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
kwargs_default_fit = {
    'batch_size': 32,
    'epochs': 100,
    'shuffle': True,
    'validation_split': 0.1,
    'callbacks': [tensorboard_callback]
}


def train(name, **kwargs):
    """Wrapping function for compile_model, train_model, initialize_model.

    :param name: TODO
    :param **kwargs: TODO
    :returns: TODO

    """
    model = initialize_model(name)
    compiled = compile_model(model)
    history, trained = train_model(compiled)
    return history, trained


def train_model(model, **kwargs):
    """Function that trains a model while managing callbacks and checkpoints.

    :param model: str
        Name of the model to be trained.

    :returns: (history, keras.model)  # TODO: add correct history type
        Trained model.

    """
    kwargs = merge_defaults(kwargs_default_fit, **kwargs)
    history = model.fit(**kwargs)
    return history, model


def compile_model(model, **kwargs):
    """Compile a passed model an merge default arguments.

    :param model: TODO
    :param **kwargs: TODO
    :returns: TODO

    """
    kwargs = merge_defaults(kwargs_default_compile, **kwargs)
    model.compile(**kwargs)
    return model


def merge_defaults(default, **kwargs):
    """Merges default dict with passed Keyword arguments.

    :param default: dict
        Default values to be merged with kwargs.
    :param **kwargs: dict
    :returns: dict
        New merged dict of kwargs.

    """
    for key, value in kwargs:
        default.update(key, value)
    return default
