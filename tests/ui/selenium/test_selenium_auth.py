import pytest

from config import PASSWORD, USERNAME
from pages.selenium.selenium_login_page import SeleniumGithubLoginPage


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.skipif(
    not USERNAME or not PASSWORD, reason="Username/Password is not provided"
)
def test_success_login(browser):

    login_page = SeleniumGithubLoginPage(browser)

    login_page.open_login_page()
    login_page.login(USERNAME, PASSWORD)

    assert login_page.is_login_successful()


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.skipif(
    not USERNAME or not PASSWORD, reason="Username/Password is not provided"
)
@pytest.mark.parametrize("username, password", [
    pytest.param(USERNAME, "wrong_password", id="wrong-password"),
    pytest.param("Test", PASSWORD, id="wrong-user")
])
def test_invalid_login(browser, username, password):

    login_page = SeleniumGithubLoginPage(browser)

    login_page.open_login_page()
    login_page.login(username, password)

    assert login_page.is_alert_present()
    assert (
        SeleniumGithubLoginPage.EXPECTED_ERROR_TEXT in login_page.get_alert_text()
    )
