import allure
from selenium.webdriver.common.by import By

from pages.selenium.duckduckgo.selenium_duckduckgo_base_page import (
    SeleniumDuckduckgoBasePage,
)


class SeleniumDuckduckgoSearchPage(SeleniumDuckduckgoBasePage):

    SEARCH_FORM = (By.ID, "searchbox_input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[data-mode="search"]')
    RESULTS_TEST_ID = (By.CSS_SELECTOR, '[data-testid="result-title-a"]')

    @allure.step("Open DuckDuckGo home page")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Search for '{query}'")
    def search(self, query):
        self.find_element(self.SEARCH_FORM).send_keys(query)
        self.find_clickable_element(self.SEARCH_BUTTON).click()

    def get_results(self):
        return self.find_elements(self.RESULTS_TEST_ID)
