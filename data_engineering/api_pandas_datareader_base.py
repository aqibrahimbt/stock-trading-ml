"""ABC that implements stock interfaces of the pandas_datareader package."""

from pandas_datareader.data import DataReader as web

from functools import partial

from api_base_class import APIBaseClass


class PandasDatareaderBase(APIBaseClass):
    """Abstract Base Class implementing pandas_datareader interfaces."""
    def __init__(self, api_name: str, **kwargs):
        super().__init__(**kwargs)
        self.api_name = api_name

        # extract super class request func to do some python magic
        super_func = super().request.__func__

        # a little pyton magic to use the super classes default parameters
        # for funtion calls from this class and it's subclasses
        self.request.__func__.__kwdefaults__ = super_func.__kwdefaults__

        # some more python magic to automate the inclusion of the api_name for
        # the data source passed through kwargs
        self.request = partial(self.request, data_source=api_name)

        # reset the signature and add the docstring from the super class
        self.request.func.__func__.__doc__ = self._build_doc(
            super_func.__doc__, self.request.func.__doc__)

    def request(self, name, *args, start, end, **kwargs):
        """Passes arguments directly to the pandas_datareader API.

        :data_source: Identifier of the pandas_datareader interface.
        """  # note this documentation is beeing merged with the base class one

        kwargs['start'] = kwargs.get('start') or start
        kwargs['end'] = kwargs.get('end') or end
        # this rather peculiar syntax makes sure arguments passed through
        # kwargs take precedent

        return web(name, *args, **kwargs)

    @staticmethod
    def _build_doc(super_doc, sub_doc):
        """Merges documentation for a function of a super class."""
        super_list = super_doc.splitlines(keepends=True)[2:]
        return sub_doc[:-8] + "".join(super_list)
