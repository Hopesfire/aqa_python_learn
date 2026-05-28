from selenium.webdriver.common.by import By
from practice.base_page import BasePage


class SaucedemoLocators:
    SAUCEDEMO_USER_NAME_FIELD = (By.ID, "user-name")
    SAUCEDEMO_PASSWORD_FIELD = (By.ID, "password")
    SAUCEDEMO_LOGIN_BUTTON = (By.ID, "login-button")
    SAUCEDEMO_INVENTORY_DIV = (By.ID, "inventory_container")


class LoginPage(BasePage):

    def open(self):
        return self.driver.get(self.base_url)

    def login(self, user_name, password):
        self.find_element(SaucedemoLocators.SAUCEDEMO_USER_NAME_FIELD).send_keys(
            user_name
        )
        self.find_element(SaucedemoLocators.SAUCEDEMO_PASSWORD_FIELD).send_keys(
            password
        )
        self.find_element(SaucedemoLocators.SAUCEDEMO_LOGIN_BUTTON).click()

    def is_login_successful(self):
        return self.find_element(
            SaucedemoLocators.SAUCEDEMO_INVENTORY_DIV
        ).is_displayed()
