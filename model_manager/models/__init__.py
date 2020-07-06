"""Package to hold all model-declaration files."""


def __getattr__(item):
    """Return a list of models in the specified item.

    :item: string
    :returns: iterable

    """
    if not isinstance(item, str):
        raise TypeError(f'{item} is not a string. Cannot import!')

    print('called')
    raise AttributeError(f'No module named {item} found.')
