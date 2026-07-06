from selenium.webdriver.common.by import By

from pages.selenium.github.selenium_base_page import SeleniumGithubBasePage


class SeleniumGithubTopicsPage(SeleniumGithubBasePage):

    TOPICS_HEADING = (By.XPATH, "//h2[normalize-space()='Popular topics']")
    TOPICS_SELECTOR = "a.topic-tag[href^='/topics/']"
    EXPECTED_TOPICS = {"python", }

    def open_topics_page(self):
        self.driver.get(self.base_url + "/topics")

    def get_topics(self):
        heading = self.find_element(self.TOPICS_HEADING)
        container = heading.find_element(By.XPATH, "./following-sibling::ul")

        return {
            link.get_attribute("href").replace("https://github.com/topics/", "").strip()
            for link in container.find_elements(By.CSS_SELECTOR, self.TOPICS_SELECTOR)
        }
