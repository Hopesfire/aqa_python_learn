import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.selenium
def test_login_page_is_opened(driver):
    driver.get("https://practicetestautomation.com/practice")

    driver.find_element(
        By.XPATH, "//div[contains(@class,'post-content')]//a[text()='Test Login Page']"
    ).click()

    assert (
        driver.current_url == "https://practicetestautomation.com/practice-test-login/"
    )


@pytest.mark.selenium
def test_login_success(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    WebDriverWait(driver, 5).until(EC.url_contains("logged-in-successfully"))

    assert "logged-in-successfully" in driver.current_url

    success_login_text = driver.find_element(By.CLASS_NAME, "post-content")
    assert (
        "Congratulations student. You successfully logged in!"
        in success_login_text.text
    )

    logout_button = driver.find_element(By.LINK_TEXT, "Log out")
    assert logout_button.is_displayed()


@pytest.mark.selenium
def test_incorrect_username(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("incorrectUser")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    error_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )
    assert error_element.is_displayed()

    assert "Your username is invalid!" in error_element.text


@pytest.mark.selenium
def test_incorrect_password(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("incorrectPassword")
    driver.find_element(By.ID, "submit").click()

    error_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )
    assert error_element.is_displayed()

    assert "Your password is invalid!" in error_element.text
