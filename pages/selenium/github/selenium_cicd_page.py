import allure
from selenium.webdriver.common.by import By

from pages.selenium.github.selenium_base_page import SeleniumGithubBasePage


class SeleniumGithubCiCdPage(SeleniumGithubBasePage):

    CONTACT_SALES_LOCATOR = (By.LINK_TEXT, "Contact sales")

    def open_cicd_page(self):
        self.driver.get(self.base_url + "/solutions/use-case/ci-cd")

    def contact_sales_button(self):
        return self.find_clickable_element(self.CONTACT_SALES_LOCATOR)

    @allure.step("Click Contact sales button")
    def click_contact_sales(self):
        self.contact_sales_button().click()
