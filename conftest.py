import pytest
from selene import browser as selene_browser
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def browser(driver):

    selene_browser.config.driver = driver

    return selene_browser
