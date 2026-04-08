import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Pattern
import re


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def open(self, url):
        step = f'Opening the url: {url}'
        with allure.step(step):
            self.browser.get(url)

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that url matches pattern "{expected_url.pattern}":'
        with allure.step(step):
            current_url = self.browser.current_url
            assert re.match(expected_url, current_url), f"URL '{current_url}' does not match pattern '{expected_url.pattern}'"

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        element = self.wait_for_visibility(locator)
        return element.text
