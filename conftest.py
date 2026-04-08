import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage


@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def main_page(browser):
    page = MainPage(browser)
    page.open(page.URL)
    return page
