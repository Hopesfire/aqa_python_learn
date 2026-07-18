from pages.playwright.github.playwright_base_page import PlaywrightGithubBasePage


class PlaywrightGithubTopicsPage(PlaywrightGithubBasePage):

    TOPICS_HEADING = "Popular topics"
    TOPICS_SELECTOR = "a.topic-tag[href^='/topics/']"
    EXPECTED_TOPICS = {
        "python",
    }

    def open_topics_page(self):
        self.page.goto(self.base_url + "/topics")

    def get_topics(self):
        container = self.page.get_by_role("heading", name=self.TOPICS_HEADING).locator(
            "~ ul"
        )
        return {
            link.get_attribute("href").replace("/topics/", "").strip()
            for link in container.locator(self.TOPICS_SELECTOR).all()
        }
