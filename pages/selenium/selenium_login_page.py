from selenium.webdriver.common.by import By

from pages.selenium.selenium_base_page import SeleniumGithubBasePage


class SeleniumGithubLoginPage(SeleniumGithubBasePage):

    USERNAME_LABEL = (By.ID, "login_field")
    PASSWORD_LABEL = (By.ID, "password")
    SIGNIN_SELECTOR = (By.CSS_SELECTOR, "input[name='commit']")
    AVATAR_TEST_ID = (By.CSS_SELECTOR, "[data-testid='github-avatar']")
    ALERT_SELECTOR = (By.CSS_SELECTOR, "[role='alert']")
    EXPECTED_ERROR_TEXT = "Incorrect username or password"

    def open_login_page(self):
        self.driver.get(self.base_url + "/login")

    def login(self, username, password):
        self.find_element(self.USERNAME_LABEL).send_keys(username)
        self.find_element(self.PASSWORD_LABEL).send_keys(password)
        self.find_clickable_element(self.SIGNIN_SELECTOR).click()

    def alert_locator(self):
        return self.find_element(self.ALERT_SELECTOR)

    def avatar_locator(self):
        return self.find_element(self.AVATAR_TEST_ID)

    def is_login_succesful(self):
        return self.avatar_locator().is_displayed()

    def is_alert_present(self):
        return self.alert_locator().is_displayed()
