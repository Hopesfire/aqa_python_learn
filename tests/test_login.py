import pytest
from practice.login_page import LoginPage


@pytest.mark.parametrize(
    "user_name, password",
    [("standard_user", "secret_sauce"), ("visual_user", "secret_sauce")],
)
def test_login_success(browser, user_name, password):
    saucedemo_main_page = LoginPage(browser)
    saucedemo_main_page.open()
    saucedemo_main_page.login(user_name, password)
    assert saucedemo_main_page.is_login_successful()
