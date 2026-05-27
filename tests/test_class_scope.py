import pytest


def create_user():
    print("CREATE USER")
    return {"id": 1, "name": "Alice", "logged_in": False, "deleted": False}


@pytest.fixture(scope="class")
def user():
    return create_user()


class TestUser:
    def test_user_created(self, user):
        assert user["name"] == "Alice"

    def test_user_login(self, user):
        user["logged_in"] = True
        assert user["logged_in"] is True

    def test_user_still_logged_in(self, user):
        assert user["logged_in"] is True


def test_user_still_logged_in(user):
    assert user["logged_in"] is True


def test_number_from_conftest(number_from_conftest):
    assert number_from_conftest == 12
