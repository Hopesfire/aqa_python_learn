import pytest


@pytest.fixture
def number_from_conftest():
    number = 12
    print(number)
    return number


class Database:
    def __init__(self):
        print("INIT DB")


@pytest.fixture(scope="session")
def db():
    print("CONNECT")
    return Database()
