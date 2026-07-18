from pages.playwright.duckduckgo.playwright_duckduckgo_base_page import (
    PlaywrightDuckduckgoBasePage,
)


class PlaywrightDuckduckgoSearchPage(PlaywrightDuckduckgoBasePage):

    SEARCH_FORM = "#searchbox_input"
    SEARCH_BUTTON = 'button[data-mode="search"]'
    RESULTS_TEST_ID = "result-title-a"

    def open(self):
        self.page.goto(self.base_url)

    def search(self, query):
        self.page.locator(self.SEARCH_FORM).fill(query)
        self.page.locator(self.SEARCH_BUTTON).click()

    def get_results(self):
        return self.page.get_by_test_id(self.RESULTS_TEST_ID)
