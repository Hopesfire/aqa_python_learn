import pytest

from pages.selenium.github.selenium_cicd_page import SeleniumGithubCiCdPage
from pages.selenium.github.selenium_contact_sales_page import \
    SeleniumGithubContactSalesPage
from pages.selenium.github.selenium_home_page import SeleniumGithubHomePage
from pages.selenium.github.selenium_solutions_menu import \
    SeleniumGithubSolutionMenu


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.github
def test_contact_sales_form(browser, fake):

    home_page = SeleniumGithubHomePage(browser)
    home_page.go_to_solutions()

    solutions_menu = SeleniumGithubSolutionMenu(browser)
    solutions_menu.select_cicd()

    cicd_page = SeleniumGithubCiCdPage(browser)
    cicd_page.click_contact_sales()

    contact_page = SeleniumGithubContactSalesPage(browser)

    first_name = fake.first_name()
    last_name = fake.last_name()
    contact_page.fill_form(first_name, last_name)

    assert (
        contact_page.get_field_value(SeleniumGithubContactSalesPage.FIRST_NAME_FIELD)
        == first_name
    )
    assert (
        contact_page.get_field_value(SeleniumGithubContactSalesPage.LAST_NAME_FIELD)
        == last_name
    )
