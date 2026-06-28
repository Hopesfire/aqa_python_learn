import pytest
from playwright.sync_api import expect

from config import PASSWORD, USERNAME
from pages.playwright.playwright_login_page import PlaywrightGithubLoginPage


@pytest.mark.ui
@pytest.mark.playwright
@pytest.mark.skipif(
    not USERNAME or not PASSWORD, reason="Username/Password is not provided"
)
def test_success_login(page):

    login_page = PlaywrightGithubLoginPage(page)

    login_page.open_login_page()
    login_page.login(USERNAME, PASSWORD)

    avatar = login_page.avatar_locator()
    expect(avatar).to_be_visible()
    expect(avatar).to_be_enabled()


@pytest.mark.ui
@pytest.mark.playwright
@pytest.mark.skipif(
    not USERNAME or not PASSWORD, reason="Username/Password is not provided"
)
def test_invalid_login(page):

    login_page = PlaywrightGithubLoginPage(page)

    login_page.open_login_page()
    login_page.login(USERNAME, "wrong_password")

    error = login_page.alert_locator()
    expect(error).to_be_visible()
    expect(error).to_contain_text(PlaywrightGithubLoginPage.EXPECTED_ERROR_TEXT)
