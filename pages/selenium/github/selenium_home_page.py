import allure
from selenium.webdriver.common.by import By

from pages.selenium.github.selenium_base_page import SeleniumGithubBasePage


class SeleniumGithubHomePage(SeleniumGithubBasePage):

    SOLUTIONS_MENU = (By.XPATH, "//button[normalize-space()='Solutions']")

    @allure.step("Open GitHub home page")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Go to Solutions menu")
    def go_to_solutions(self):
        self.open()
        self.hover(self.SOLUTIONS_MENU)
