import pytest

shared = []


@pytest.fixture
def data():
    shared.extend([1, 2, 3])

    yield shared

    shared.clear()


def test_data_exists(data):
    assert len(data) == 3


def test_data_is_clean():
    assert shared == []
