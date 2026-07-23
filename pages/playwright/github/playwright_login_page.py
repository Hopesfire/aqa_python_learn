import allure

from pages.playwright.github.playwright_base_page import PlaywrightGithubBasePage


class PlaywrightGithubLoginPage(PlaywrightGithubBasePage):

    USERNAME_LABEL = "Username or email address"
    PASSWORD_LABEL = "Password"
    SIGNIN_SELECTOR = "input[name='commit']"
    AVATAR_TEST_ID = "github-avatar"
    ALERT_SELECTOR = "[role='alert']"
    EXPECTED_ERROR_TEXT = "Incorrect username or password"
    DEVICE_VERIFICATION_SELECTOR = "#device-verification-prompt"

    @allure.step("Open GitHub login page")
    def open_login_page(self):
        self.page.goto(self.base_url + "/login")

    def login(self, username, password):
        with allure.step(f"Login with username '{username}'"):
            self.page.get_by_label(self.USERNAME_LABEL).fill(username)
            self.page.get_by_label(self.PASSWORD_LABEL).fill(password)
            self.page.locator(self.SIGNIN_SELECTOR).click()

    def alert_locator(self):
        return self.page.locator(self.ALERT_SELECTOR)

    def avatar_locator(self):
        return self.page.get_by_test_id(self.AVATAR_TEST_ID)

    def device_verification_locator(self):
        return self.page.locator(self.DEVICE_VERIFICATION_SELECTOR)
