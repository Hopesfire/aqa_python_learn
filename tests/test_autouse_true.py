import pytest

@pytest.fixture(autouse=True)
def setup_db():
    print("Setting up database...")
    print("Loading...")
    print("Database loaded!")


def test_a():
    assert 1 == 1

def test_b():
    assert 2 == 2

def test_c():
    assert 3 == 3

def test_number_from_conftest(number_from_conftest):
    assert number_from_conftest == 12