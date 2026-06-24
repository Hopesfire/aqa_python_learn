import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_login_page_is_opened(browser):
    browser.get("https://practicetestautomation.com/practice")

    browser.find_element(
        By.XPATH, "//div[contains(@class,'post-content')]//a[text()='Test Login Page']"
    ).click()

    assert (
        browser.current_url == "https://practicetestautomation.com/practice-test-login/"
    )


def test_login_success(browser):
    browser.get("https://practicetestautomation.com/practice-test-login/")

    browser.find_element(By.ID, "username").send_keys("student")
    browser.find_element(By.ID, "password").send_keys("Password123")
    browser.find_element(By.ID, "submit").click()

    WebDriverWait(browser, 5).until(EC.url_contains("logged-in-successfully"))

    assert "logged-in-successfully" in browser.current_url

    success_login_text = browser.find_element(By.CLASS_NAME, "post-content")
    assert (
        "Congratulations student. You successfully logged in!"
        in success_login_text.text
    )

    logout_button = browser.find_element(By.LINK_TEXT, "Log out")
    assert logout_button.is_displayed()


def test_incorrect_username(browser):
    browser.get("https://practicetestautomation.com/practice-test-login/")

    browser.find_element(By.ID, "username").send_keys("incorrectUser")
    browser.find_element(By.ID, "password").send_keys("Password123")
    browser.find_element(By.ID, "submit").click()

    error_element = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )
    assert error_element.is_displayed()

    assert "Your username is invalid!" in error_element.text


def test_incorrect_password(browser):
    browser.get("https://practicetestautomation.com/practice-test-login/")

    browser.find_element(By.ID, "username").send_keys("student")
    browser.find_element(By.ID, "password").send_keys("incorrectPassword")
    browser.find_element(By.ID, "submit").click()

    error_element = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )
    assert error_element.is_displayed()

    assert "Your password is invalid!" in error_element.text
