from selenium.webdriver.common.by import By

from pages.selenium.selenium_base_page import SeleniumGithubBasePage


class SeleniumGithubHomePage(SeleniumGithubBasePage):

    SOLUTIONS_MENU = (
        By.XPATH,
        "//button[contains(@class, 'js-details-target') and normalize-space(text())='Solutions']",
    )

    def open(self):
        self.driver.get(self.base_url)

    def go_to_solutions(self):
        self.open()
        self.hover(self.SOLUTIONS_MENU)
