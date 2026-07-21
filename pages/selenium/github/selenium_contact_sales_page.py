import allure
from selenium.webdriver.common.by import By

from pages.selenium.github.selenium_base_page import SeleniumGithubBasePage


class SeleniumGithubContactSalesPage(SeleniumGithubBasePage):

    FIRST_NAME_FIELD = (By.ID, "form-field-first_name")
    LAST_NAME_FIELD = (By.ID, "form-field-last_name")

    def open_contact_sales_page(self):
        self.driver.get(self.base_url + "/enterprise/contact")

    @allure.step("Fill contact sales form")
    def fill_form(self, first_name, last_name):
        self.find_element(self.FIRST_NAME_FIELD).send_keys(first_name)
        self.find_element(self.LAST_NAME_FIELD).send_keys(last_name)

    def get_field_value(self, locator):
        return self.find_element(locator).get_attribute("value")
