"""Module that automatically instantiates all models from a folder."""

from pathlib import Path
from importlib import import_module as imp
# from tensorflow.train import load_checkpoint

from model_manager.models_util import load_model
from model_manager.model_inspect_loader import ModelInspectLoader as MIL
# from model_manager.models_util import save_model
# from .models_util import save_model

MODELS_PATH = Path(__file__).parent / 'models'
CHECKPOINT_PATH = Path(__file__).parent / 'checkpoints'
BUILD_PATH = Path(__file__).parent / 'build'


# obsolete, should be deleted soon
def import_model(name):
    """Import all models from given module from MODELS_PATH.

    :name: str
        The string of a module located in the models package.
    :returns: list
        List of models.

    """
    p = MODELS_PATH / (name + '.py')
    if not p.exists():
        raise FileNotFoundError(f'File {p} cannot be found.')

    module = imp(f'model_manager.models.{name}')
    c_list = dir(module)
    model_list = [getattr(module, x) for x in c_list if x.endswith('model')]
    # return model_list  # for now only a single module can be imported
    return model_list[-1]


def initialize_model(name, data_shape):
    """Initializes all models of a given module.

    :name: str
        Name of the Module with models.
    :returns: None

    """
    loader = MIL(input_shape=data_shape)
    name_path = MODELS_PATH / (name + '.py')
    model = loader.import_model(name_path)
    # model = get_lates_ckpt(name, model)
    return model
    # TODO: Finish Training and come back to use correct conventions.


# unused, still needs proper setup
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
    model_contents = list(BUILD_PATH.glob(f'{name}*.ckpt'))
    # ckpt_contents.append(model_contents)
    if not model_contents:
        return model

    latest = max(model_contents, key=lambda p: p.stat().ctime)
    return load_model(latest)
