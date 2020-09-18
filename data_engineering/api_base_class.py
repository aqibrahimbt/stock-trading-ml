"""API abstract base class interface that normalizes data gathering."""

from abc import ABC, abstractmethod

from datetime import datetime


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
    def request_stock_data(self, name: str, start: datetime, end: datetime):
        ...
