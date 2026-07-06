from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumDuckduckgoBasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://duckduckgo.com"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_clickable_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Element not clickable by locator {locator}",
        )

    def find_elements(self, locator, time=10):
        WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )
        return self.driver.find_elements(*locator)

    def hover(self, locator):
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
