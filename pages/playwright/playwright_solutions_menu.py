from pages.playwright.playwright_base_page import PlaywrightGithubBasePage


class PlaywrightGithubSolutionMenu(PlaywrightGithubBasePage):

    def select_cicd(self):
        self.page.get_by_role("link", name="CI/CD").click()
