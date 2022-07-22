import numpy as np
import pandas as pd
import pytest

from pytemppack import PyPack


def test_pytemppack_init():
    data = np.array([[1, 2, 3], [4, 5, 6]])
    pypack = PyPack(data)

    assert isinstance(pypack.data, np.ndarray)
    assert pypack.data.shape[0] == 2
    assert pypack.data.shape[1] == 3


def test_pytemppack_init_fail():
    data = [[1, 2, 3], [4, 5, 6]]

    with pytest.raises(ValueError, match="The data has to be an ndarray."):
        PyPack(data)


def test_ppytemppack_transform_results():
    data = np.array([[1, 2, 3], [4, 5, 6]])
    pypack = PyPack(data)

    columns = ["a", "b"]
    pypack.transform_results(columns)

    assert isinstance(pypack.results, pd.DataFrame)
    assert all(pypack.results.columns == columns)
    assert pypack.results.shape[0] == 3
    assert pypack.results.shape[1] == 2
