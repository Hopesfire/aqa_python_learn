import allure
import pytest
from playwright.sync_api import expect

from config import PASSWORD, USERNAME
from pages.playwright.github.playwright_login_page import PlaywrightGithubLoginPage


@pytest.mark.ui
@pytest.mark.playwright
@pytest.mark.github
@pytest.mark.skipif(
    not USERNAME or not PASSWORD, reason="Username/Password is not provided"
)
def test_success_login(page):

    login_page = PlaywrightGithubLoginPage(page)

    login_page.open_login_page()
    login_page.login(USERNAME, PASSWORD)

    with allure.step("Verify avatar is visible after login"):
        avatar = login_page.avatar_locator()
        expect(avatar).to_be_visible()
        expect(avatar).to_be_enabled()


@pytest.mark.ui
@pytest.mark.playwright
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
def test_invalid_login(page, username, use_correct_password):
    password = PASSWORD if use_correct_password else "wrong_password"

    login_page = PlaywrightGithubLoginPage(page)

    login_page.open_login_page()
    login_page.login(username, password)

    with allure.step("Verify error message is shown"):
        error = login_page.alert_locator()
        expect(error).to_be_visible()
        expect(error).to_contain_text(PlaywrightGithubLoginPage.EXPECTED_ERROR_TEXT)
