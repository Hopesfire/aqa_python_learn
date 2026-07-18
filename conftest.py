import os

import pytest
from faker import Faker
from playwright.sync_api import sync_playwright
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    options = Options()
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=bool(os.getenv("CI")))

        page = browser.new_page()

        yield page

        browser.close()


@pytest.fixture
def fake():
    return Faker()
