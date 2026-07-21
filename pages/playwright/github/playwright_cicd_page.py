import allure

from pages.playwright.github.playwright_base_page import PlaywrightGithubBasePage


class PlaywrightGithubCiCdPage(PlaywrightGithubBasePage):

    def open_cicd_page(self):
        self.page.goto(self.base_url + "/solutions/use-case/ci-cd")

    def contact_sales_button(self):
        return self.page.get_by_role("link", name="Contact sales").first

    @allure.step("Click Contact sales button")
    def click_contact_sales(self):
        self.contact_sales_button().click()
        self.page.wait_for_url("**/enterprise/contact**")
