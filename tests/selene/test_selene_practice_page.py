import pytest
from selene import be, by, have


@pytest.mark.selene
def test_login_page_is_opened(browser):
    browser.open("https://practicetestautomation.com/practice")

    browser.element(
        "//div[contains(@class,'post-content')]//a[text()='Test Login Page']"
    ).click()

    browser.should(have.url_containing("practice-test-login"))


@pytest.mark.selene
def test_login_success(browser):
    browser.open("https://practicetestautomation.com/practice-test-login/")

    browser.element("#username").type("student")
    browser.element("#password").type("Password123")
    browser.element("#submit").click()

    browser.should(have.url_containing("logged-in-successfully"))

    browser.element(".post-content").should(
        have.text("Congratulations student. You successfully logged in!")
    )

    logout_button = browser.element(by.text("Log out"))
    logout_button.should(be.visible)


@pytest.mark.selene
def test_incorrect_username(browser):
    browser.open("https://practicetestautomation.com/practice-test-login/")

    browser.element("#username").type("incorrectUser")
    browser.element("#password").type("Password123")
    browser.element("#submit").click()

    error = browser.element("#error")
    error.should(be.visible)
    error.should(have.text("Your username is invalid!"))


@pytest.mark.selene
def test_incorrect_password(browser):
    browser.open("https://practicetestautomation.com/practice-test-login/")

    browser.element("#username").type("student")
    browser.element("#password").type("incorrectPassword")
    browser.element("#submit").click()

    error = browser.element("#error")
    error.should(be.visible)
    error.should(have.text("Your password is invalid!"))
