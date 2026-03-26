import pytest
from playwright.sync_api import sync_playwright
from pages.blog_home_page import BlogHomePage

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture()
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture()
def blog_home(page):
    blog_page = BlogHomePage(page)
    blog_page.open()
    return blog_page