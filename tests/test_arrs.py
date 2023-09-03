import pytest

from utils import arrs

@pytest.fixture
def get_fixture():
    return [1, 2, 3]

@pytest.fixture
def slice_fixture():
    return [1, 2, 3, 4]

def test_get(get_fixture):
    assert arrs.get(get_fixture, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(slice_fixture):
    assert arrs.my_slice(slice_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(slice_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(slice_fixture) == [1, 2, 3, 4]
