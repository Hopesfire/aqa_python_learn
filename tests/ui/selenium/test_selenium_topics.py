import pytest

from pages.selenium.github.selenium_topics_page import SeleniumGithubTopicsPage


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.github
def test_topics_subset(browser):
    topics_page = SeleniumGithubTopicsPage(browser)
    topics_page.open_topics_page()

    assert SeleniumGithubTopicsPage.EXPECTED_TOPICS.issubset(topics_page.get_topics())
