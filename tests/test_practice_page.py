import pytest
from playwright.sync_api import expect


def test_login_page_is_opened(page):
    page.goto("https://practicetestautomation.com/practice")

    page.locator(
        "//div[contains(@class,'post-content')]//a[text()='Test Login Page']"
    ).click()

    expect(page).to_have_url("https://practicetestautomation.com/practice-test-login/")


def test_login_success(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.locator("#username").fill("student")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()

    expect(page).to_have_url(
        "https://practicetestautomation.com/logged-in-successfully/"
    )

    expect(page.locator(".post-content")).to_contain_text(
        "Congratulations student. You successfully logged in!"
    )

    expect(page.get_by_text("Log out")).to_be_visible()


def test_incorrect_username(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.locator("#username").fill("incorrectUser")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()

    expect(page.locator("#error")).to_be_visible()
    expect(page.locator("#error")).to_contain_text("Your username is invalid!")


def test_incorrect_password(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.locator("#username").fill("student")
    page.locator("#password").fill("incorrectPassword")
    page.locator("#submit").click()

    expect(page.locator("#error")).to_be_visible()
    expect(page.locator("#error")).to_contain_text("Your password is invalid!")
