import numpy as np

from pytemppack.utils import generate_random_array, is_valid_ndarray


def test_is_valid_ndarray_true():
    data = np.array([1, 2, 3])
    output = is_valid_ndarray(data)

    assert output is True


def test_is_valid_ndarray_false():
    data = [1, 2, 3]
    output = is_valid_ndarray(data)

    assert output is False


def test_generate_random_array():
    data = generate_random_array((3, 3))

    assert isinstance(data, np.ndarray)
    assert data.shape[0] == 3
    assert data.shape[1] == 3
