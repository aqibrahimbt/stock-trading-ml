"""Module that automatically instantiates all models from a folder."""

from pathlib import Path
from importlib import import_module as imp

from model_manager.models_util import save_model
# from .models_util import save_model

MODELS_PATH = Path.cwd() / 'models'


def import_models(name):
    """Import all models from given module from MODELS_PATH.

    :name: str
        The string of a module located in the models package.
    :returns: list
        List of models.

    """
    p = MODELS_PATH / name
    if not p.exists()
        raise FileNotFoundError(f'File {p} cannot be found.')

    module = imp(f'models.{name}')
    c_list = dir(module)
    model_list = [getattr(module, x) for x in c_list if x.endswith('model')]
    return model_list


def initialize_model(name):
    """Initializes all models of a given module.

    :name: str
        Name of the Module with models.
    :returns: None

    """
    model_list = import_models(name)

