import pytest


@pytest.fixture(scope="module")
def counter():
    print("CREATE")
    return []


def test_a(counter):
    counter.append(1)
    print(counter)
    assert counter == [1]


def test_b(counter):
    counter.append(2)
    print(counter)
    assert counter == [1, 2]


def test_c(counter):
    counter.append(2)
    print(counter)
    assert counter == []


def test_number_from_conftest(number_from_conftest):
    assert number_from_conftest == 12
