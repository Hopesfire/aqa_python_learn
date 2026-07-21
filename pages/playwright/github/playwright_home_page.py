import allure

from pages.playwright.github.playwright_base_page import PlaywrightGithubBasePage


class PlaywrightGithubHomePage(PlaywrightGithubBasePage):

    @allure.step("Open GitHub home page")
    def open(self):
        self.page.goto(self.base_url)

    @allure.step("Go to Solutions menu")
    def go_to_solutions(self):
        self.open()
        self.page.get_by_role("button", name="Solutions").hover()
