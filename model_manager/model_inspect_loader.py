"""Module that provides a class to make import of models more abstract."""

from importlib.abc import InspectLoader


class ModelInspectLoader(InspectLoader):
    """Provides functionality for abstract model imports from standardized files."""
    def __init__(self, input_shape=None, output_mask=None):
        """"""
        self.input_shape = input_shape
        self.output_mask = output_mask

    def get_source(self, fullname):
        """Provide source code object for a module in the models directory.

        :param fullname: str or pathlib.Path
        :returns: keras.model

        """
        with open(fullname) as f:
            s = f.read()
        print(s)
        return s

    def is_package(self, fullname):
        """TODO: Docstring for is_package.

        :param fullname: TODO
        :returns: TODO

        """
        pass
