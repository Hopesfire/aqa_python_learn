import pytest


def calculate(a, b):
    return a + b


@pytest.mark.parametrize(
    "first_value, second_value, result", [(1, 2, 3), (-1, -2, -3), (1, -2, -1)]
)
def test_calculator(first_value, second_value, result):
    assert calculate(first_value, second_value) == result


def test_without_smoke_marker():
    print("Will not print with pytest -m smoke")
    assert calculate(1, 1) == 2


@pytest.mark.smoke
def test_with_smoke_marker1():
    print("Will print with pytest -m smoke")
    assert calculate(2, 2) == 4


@pytest.mark.smoke
@pytest.mark.parametrize(
    "first_value, second_value, result", [(5, 5, 10), (5, 6, 11), (100, 100, 200)]
)
def test_with_smoke_and_parametrize(first_value, second_value, result):
    print("Will print with pytest -m smoke")
    assert calculate(first_value, second_value) == result


@pytest.mark.skip(reason="Feature not ready")
def test_skip1():
    print("Will not print")
    assert True


@pytest.mark.smoke
@pytest.mark.skip(reason="skipping because of mark.skip")
def test_skip_with_smoke_marker():
    print("Will not print")
    assert True


@pytest.mark.xfail(reason="Bug #11 not fixed yet")
def test_old_bug():
    assert 1 == 2


@pytest.mark.xfail(reason="Bug should still exist")
def test_old_bug_xpass():
    assert 3 == 3
