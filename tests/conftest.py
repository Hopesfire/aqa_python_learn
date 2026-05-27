import pytest

@pytest.fixture
def number_from_conftest():
    number = 12
    print(number)
    return number