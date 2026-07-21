import allure
from selenium.webdriver.common.by import By

from pages.selenium.github.selenium_base_page import SeleniumGithubBasePage


class SeleniumGithubSolutionMenu(SeleniumGithubBasePage):

    CICD_LOCATOR = (By.LINK_TEXT, "CI/CD")

    @allure.step("Select CI/CD from Solutions menu")
    def select_cicd(self):
        self.find_clickable_element(self.CICD_LOCATOR).click()
