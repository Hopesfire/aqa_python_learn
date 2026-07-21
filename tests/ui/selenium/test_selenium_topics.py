import allure
import pytest

from pages.selenium.github.selenium_topics_page import SeleniumGithubTopicsPage


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.github
@allure.tag("flaky")
def test_topics_subset(browser):
    topics_page = SeleniumGithubTopicsPage(browser)
    topics_page.open_topics_page()

    with allure.step("Verify expected topics are present"):
        assert SeleniumGithubTopicsPage.EXPECTED_TOPICS.issubset(
            topics_page.get_topics()
        )
