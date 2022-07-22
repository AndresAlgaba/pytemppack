"""PyPack class."""

from typing import List, Optional

import numpy as np
import pandas as pd

from pytemppack.utils import is_valid_ndarray


class PyPack:
    """PyPack object for transforming ``np.ndarray`` to ``pd.DataFrame``.

    This class contains methods to transform an ``np.ndarray`` to
    ``pd.DataFrame``.

    Attributes
    ----------
    results : pd.DataFrame
        A dataframe with the canonical inputs.

    Examples
    --------
    >>> pypack = PyPack(data)
    >>> pypack.transform(columns)
    """

    results: pd.DataFrame

    def __init__(self, data: np.ndarray):
        """Initialize with ``np.ndarray`` data.

        Parameters
        ----------
        data : np.ndarray
            The data that has to be transformed into a ``pd.DataFrame``.

        Raises
        ------
        ValueError
            If the data is not an ``np.ndarray``.
        """
        if not is_valid_ndarray(data):
            raise ValueError("The data has to be an ndarray.")

        self.data = data

    def transform_results(self, columns: Optional[List[str]] = None) -> None:
        """Transform the ``data`` into a ``pd.DataFrame``.

        The ``np.ndarray`` will be transposed as the rows are considered to be
        columns, and vice versa.

        Parameters
        ----------
        columns : Optional[List[str]]
            The column names that can be used in the ``pd.DataFrame``.

        Returns
        -------
        None

        Note
        ----
        The transformed ``data`` is not returned but attributed to ``results``.
        """
        self.results = pd.DataFrame(self.data.T, columns=columns)
