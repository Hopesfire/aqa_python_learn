import os

import allure
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


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    playwright_page = item.funcargs.get("page")
    if playwright_page:
        allure.attach(
            playwright_page.screenshot(full_page=True),
            name=f"screenshot_{item.name}",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            playwright_page.content(),
            name="page_html",
            attachment_type=allure.attachment_type.HTML,
        )

    selenium_driver = item.funcargs.get("browser")
    if selenium_driver:
        allure.attach(
            selenium_driver.get_screenshot_as_png(),
            name=f"screenshot_{item.name}",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            selenium_driver.page_source,
            name="page_html",
            attachment_type=allure.attachment_type.HTML,
        )
