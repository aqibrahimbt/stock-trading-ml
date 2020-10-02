"""Collection of classes implementing the PandasDatareaderBase interface."""

from api_pandas_datareader_base import PandasDatareaderBase

from pandas import DataFrame


class PandasDatareaderYahoo(PandasDatareaderBase):
    """Provides access to yahoo finance data in a normalized data format."""
    def __init__(self):
        super().__init__(api_name='yahoo')

    @staticmethod
    def normalize_data_format(df: DataFrame) -> DataFrame:
        """Normalizes the from yahoo finance returned data format."""
        return df  # for now: the yahoo finance format is the standard version
