import pytest
import random


@pytest.fixture(scope="function")
def even_number():
    number = random.randrange(2, 1000, 2)
    print(number)
    return number


def test_number_is_even1(even_number):
    assert even_number % 2 == 0

def test_number_is_even2(even_number):
    assert even_number % 2 == 0

def test_number_is_even3(even_number):
    assert even_number % 2 == 0

def test_number_from_conftest(number_from_conftest):
    assert number_from_conftest == 12