"""Module that automatically instantiates all models from a folder."""

from pathlib import Path
from importlib import import_module as imp
from tensorflow.train import load_checkpoint

from model_manager.models_util import load_model
# from model_manager.models_util import save_model
# from .models_util import save_model

MODELS_PATH = Path(__file__).parent() / 'models'
CHECKPOINT_PATH = Path(__file__).parent() / 'checkpoints'
BUILD_PATH = Path(__file__).parent() / 'build'


def import_models(name):
    """Import all models from given module from MODELS_PATH.

    :name: str
        The string of a module located in the models package.
    :returns: list
        List of models.

    """
    p = MODELS_PATH / name
    if not p.exists():
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
    model_list = [get_lates_ckpt(name, m) for m in model_list]
    return model_list
    # TODO: Finish Training and come back to use correct conventions.


def get_lates_ckpt(name, model):
    """Find and return path to latest checkpoint or saved model.

    :param name: string
        Name of the model.
    :param model: keras.model
        Model that should be restored.
    :returns: keras.model
        Model with the latest checkpoint restored.

    """
    # ckpt_contents = CHECKPOINT_PATH.glob(f'{name}*.ckpt')
    model_contents = BUILD_PATH.glob(f'{name}*.ckpt')
    # ckpt_contents.append(model_contents)
    latest = max(model_contents, lambda p: p.stat().ctime)
    return load_model(latest)
