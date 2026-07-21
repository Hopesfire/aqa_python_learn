import allure
import pytest

from config import PASSWORD, USERNAME
from pages.selenium.github.selenium_login_page import SeleniumGithubLoginPage


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.github
@pytest.mark.skipif(
    not USERNAME or not PASSWORD, reason="Username/Password is not provided"
)
def test_success_login(browser):

    login_page = SeleniumGithubLoginPage(browser)

    login_page.open_login_page()
    login_page.login(USERNAME, PASSWORD)

    with allure.step("Verify login was successful"):
        assert login_page.is_login_successful()


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.github
@pytest.mark.skipif(
    not USERNAME or not PASSWORD, reason="Username/Password is not provided"
)
@pytest.mark.parametrize(
    "username, use_correct_password",
    [
        pytest.param(USERNAME, False, id="wrong-password"),
        pytest.param("Test", True, id="wrong-user"),
    ],
)
def test_invalid_login(browser, username, use_correct_password):
    password = PASSWORD if use_correct_password else "wrong_password"

    login_page = SeleniumGithubLoginPage(browser)

    login_page.open_login_page()
    login_page.login(username, password)

    with allure.step("Verify error message is shown"):
        assert login_page.is_alert_present()
        assert (
            SeleniumGithubLoginPage.EXPECTED_ERROR_TEXT in login_page.get_alert_text()
        )
