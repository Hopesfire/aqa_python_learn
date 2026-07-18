from selenium.webdriver.common.by import By

from pages.selenium.github.selenium_base_page import SeleniumGithubBasePage


class SeleniumGithubHomePage(SeleniumGithubBasePage):

    SOLUTIONS_MENU = (By.XPATH, "//button[normalize-space()='Solutions']")

    def open(self):
        self.driver.get(self.base_url)

    def go_to_solutions(self):
        self.open()
        self.hover(self.SOLUTIONS_MENU)
