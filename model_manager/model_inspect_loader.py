"""Module that provides a class to make import of models more abstract."""

from importlib.abc import InspectLoader


class ModelInspectLoader(InspectLoader):
    """Provides functionality for abstract model imports from standardized files."""
    def __init__(self):
        """Not really interesting?"""
        pass

    @override
    def get_source(self, fullname):
        """Provide source code object for a module in the models directory.

        :param fullname: str or pathlib.Path
        :returns: keras.model

        """
        pass
