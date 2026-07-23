import allure

from pages.playwright.duckduckgo.playwright_duckduckgo_base_page import (
    PlaywrightDuckduckgoBasePage,
)


class PlaywrightDuckduckgoSearchPage(PlaywrightDuckduckgoBasePage):

    SEARCH_FORM = "input[data-ssg-id='ai-searchbox-input']"
    SEARCH_BUTTON = 'button[data-mode="search"]'
    RESULTS_TEST_ID = "result-title-a"
    CAPTCHA_TEST_ID = "anomaly-modal"

    @allure.step("Open DuckDuckGo home page")
    def open(self):
        self.page.goto(self.base_url)

    @allure.step("Search for '{query}'")
    def search(self, query):
        self.page.locator(self.SEARCH_FORM).fill(query)
        self.page.locator(self.SEARCH_BUTTON).click()
        self.page.wait_for_load_state("domcontentloaded")

    def get_results(self):
        return self.page.get_by_test_id(self.RESULTS_TEST_ID)

    def captcha_locator(self):
        return self.page.get_by_test_id(self.CAPTCHA_TEST_ID)
