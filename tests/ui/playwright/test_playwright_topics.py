import pytest

from pages.playwright.github.playwright_topics_page import PlaywrightGithubTopicsPage


@pytest.mark.ui
@pytest.mark.playwright
@pytest.mark.github
def test_topics_subset(page):
    topics_page = PlaywrightGithubTopicsPage(page)
    topics_page.open_topics_page()

    assert PlaywrightGithubTopicsPage.EXPECTED_TOPICS.issubset(topics_page.get_topics())
