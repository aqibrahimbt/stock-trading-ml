"""API abstract base class interface that normalizes data gathering."""

from abc import ABC, abstractmethod

from datetime import datetime


class APIBaseClass(ABC):
    """Abstract Base Class that implements an data gathering interface ."""
    def __init__():
        ...

    @abstractmethod
    def request_stock_data(name: str, start: datetime, end: datetime):
        ...
