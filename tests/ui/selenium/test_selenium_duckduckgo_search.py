import allure
import pytest

from pages.selenium.duckduckgo.selenium_duckduckgo_search_page import (
    SeleniumDuckduckgoSearchPage,
)


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.duckduckgo
@pytest.mark.parametrize("query", ["qa", "aqa", "python"])
def test_duckduckgo_search(browser, query):

    # Site: duckduckgo.com — chosen for stability, fewer CAPTCHAs than Google
    search_page = SeleniumDuckduckgoSearchPage(browser)
    search_page.open()
    search_page.search(query)

    if search_page.is_captcha_present():
        pytest.xfail("DuckDuckGo bot challenge appeared")

    with allure.step("Verify search results are displayed"):
        results = search_page.get_results()
        assert len(results) > 5
