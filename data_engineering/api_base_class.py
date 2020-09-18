"""API abstract base class interface that normalizes data gathering."""

from abc import ABC, abstractmethod

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
    def request(self,
                name: str,
                start: datetime = datetime.today() - timedelta(days=1000),
                end: datetime = datetime.today()):
        """Request stock data from a given stock in a standardized format.

        :name:  Identifier token for the requested stock.
        :start: Starting date for the requested stock data time seriers.
        :end: End date for the requested stock data time series.
        :returns: Stock data for given identifier token in a standardized
                  format.
        """
