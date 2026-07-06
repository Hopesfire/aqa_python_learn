from pages.playwright.github.playwright_base_page import \
    PlaywrightGithubBasePage


class PlaywrightGithubContactSalesPage(PlaywrightGithubBasePage):

    FIRST_NAME_FIELD = "#form-field-first_name"
    LAST_NAME_FIELD = "#form-field-last_name"

    def open_contact_sales_page(self):
        self.page.goto(self.base_url + "/enterprise/contact")

    def fill_form(self, first_name, last_name):
        self.page.locator(self.FIRST_NAME_FIELD).fill(first_name)
        self.page.locator(self.LAST_NAME_FIELD).fill(last_name)

    def get_field_value(self, locator):
        return self.page.locator(locator).input_value()
