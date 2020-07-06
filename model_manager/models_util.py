"""Provides utilities for the usage of Tensorflow-models."""

from pathlib import Path

BUILD_PATH = Path.cwd() / 'build'


def save_model(model, name, force=False):  # TODO: Test it.
    """Saves the weights of a model to a file.

    :model: tensorflow.keras.model
        Model whichs weights should be saved.
    :name: str
        Name of the model
    :returns: None

    """
    p = BUILD_PATH / name
    if not force and p.exists():
        ask_permission(f'File {p} already exists, save anyway?')
    model.save_weights(p)


def load_model(model, file_name, base_path=BUILD_PATH):  # TODO: Test it.
    """Loads the weights of a model from a file to a model.
    :model: tensorflow.keras.model
       Model the Weights are imported to.
    :file_name: str, pathlib.Path
       Name of the file the weights can be found in.
    :returns: tensorflow.keras.model

    """
    p = base_path / file_name
    if not p.exists():
        return

    model.load_weights(p)
    return model


def ask_permission(quest, default=False):
    """Asks for commandline permission (y/n).

    :quest: str
        Question asked to be confirmed.
    :default: bool
        Default answer (Return).
    :raises: PermissionError
        If permission is not granted an error is raised.
    :returns: None

    """
    def_op = '(Y/n)' if default else '(y/N)'
    while True:
        answ = input(f'{quest} {def_op} ')
        YES = {'y', 'Y', 'yes', 'Yes', 'yeah'}
        NO = {'n', 'N', 'no', 'No', 'nope'}
        YES.add('') if default else NO.add('')
        if answ in NO:
            raise PermissionError('Permission denied (command line).')
        if answ in YES:
            break
