import allure
import pytest
from playwright.sync_api import expect

from pages.playwright.duckduckgo.playwright_duckduckgo_search_page import (
    PlaywrightDuckduckgoSearchPage,
)


@pytest.mark.ui
@pytest.mark.playwright
@pytest.mark.duckduckgo
@pytest.mark.parametrize("query", ["qa", "aqa", "python"])
def test_duckduckgo_search(page, query):

    # Site: duckduckgo.com — chosen for stability, fewer CAPTCHAs than Google
    search_page = PlaywrightDuckduckgoSearchPage(page)
    search_page.open()
    search_page.search(query)

    if search_page.captcha_locator().is_visible():
        pytest.xfail("DuckDuckGo bot challenge appeared")

    with allure.step("Verify search results are displayed"):
        results = search_page.get_results()
        expect(results.nth(5)).to_be_visible()
        assert results.count() > 5
