import pytest

from pages.playwright.github.playwright_cicd_page import \
    PlaywrightGithubCiCdPage
from pages.playwright.github.playwright_contact_sales_page import \
    PlaywrightGithubContactSalesPage
from pages.playwright.github.playwright_home_page import \
    PlaywrightGithubHomePage
from pages.playwright.github.playwright_solutions_menu import \
    PlaywrightGithubSolutionMenu


@pytest.mark.ui
@pytest.mark.playwright
@pytest.mark.github
def test_contact_sales_form(page, fake):

    home_page = PlaywrightGithubHomePage(page)
    home_page.go_to_solutions()

    solutions_menu = PlaywrightGithubSolutionMenu(page)
    solutions_menu.select_cicd()

    cicd_page = PlaywrightGithubCiCdPage(page)
    cicd_page.click_contact_sales()

    contact_page = PlaywrightGithubContactSalesPage(page)

    first_name = fake.first_name()
    last_name = fake.last_name()
    contact_page.fill_form(first_name, last_name)

    assert (
        contact_page.get_field_value(PlaywrightGithubContactSalesPage.FIRST_NAME_FIELD)
        == first_name
    )
    assert (
        contact_page.get_field_value(PlaywrightGithubContactSalesPage.LAST_NAME_FIELD)
        == last_name
    )
