"""Utilities for py_pack."""

from typing import Tuple

import numpy as np
from numpy.random import default_rng


def is_valid_ndarray(array: np.ndarray) -> bool:
    """Check whether the array is an ``np.ndarray``.

    Parameters
    ----------
    array : np.ndarray
        The array to check.

    Returns
    -------
    bool
        True if the array is an ``np.ndarray``.

    Examples
    --------
    >>> is_valid_ndarray(np.array([1, 2, 3]))
    """
    return isinstance(array, np.ndarray)


def generate_random_array(dims: Tuple[int], seed: int = 1234) -> np.ndarray:
    """Generate a random ``np.ndarray``.

    Parameters
    ----------
    dims : Tuple[int]
        The dimensions of the array.

    Returns
    -------
    np.ndarray
        The random array.

    Examples
    --------
    >>> generate_random_array((3, 3))

    Note
    ----
    For more information on the randomness, see `here
    <https://numpy.org/doc/stable/reference/random/
    generated/numpy.random.Generator.random.html>`__.
    """
    rng = default_rng(seed)

    return rng.random(dims)
