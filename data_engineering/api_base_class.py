"""API abstract base class interface that normalizes data gathering."""

from abc import ABC, abstractmethod

from pandas import DataFrame
from datetime import datetime, timedelta


class APIBaseClass(ABC):
    """Abstract Base Class that implements an data gathering interface ."""
    def __init__(self,
                 api_key: str = None,
                 creds: dict = {
                     'name': None,
                     'pass': None
                 }):
        self.api_key = api_key
        self.creds = creds

    @abstractmethod
    def request(
        self,
        name: str,
        *args,
        start: datetime = datetime.today() - timedelta(days=1000),
        end: datetime = datetime.today(),
        **kwargs,
    ) -> DataFrame:
        """Request stock data from a given stock in a standardized format.

        :name:  Identifier token for the requested stock.
        :start: Starting date for the requested stock data time seriers.
        :end: End date for the requested stock data time series.
        :returns: Stock data for given identifier token in a standardized
                  format.
        """
        pass

    def request_to_csv(self, filename, *args, **kwargs):
        """Saves a specified request call to disk in csv format."""
        df = self.request(*args, **args)
        df.to_csv(path_or_buf=filename)
