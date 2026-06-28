import pytest
from playwright.sync_api import sync_playwright
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        yield page

        browser.close()
