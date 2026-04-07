import allure
from typing import Pattern
import re


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        step = f'Opening the url: {url}'
        with allure.step(step):
            self.browser.get(url)

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that url matches pattern "{expected_url.pattern}":'
        with allure.step(step):
            current_url = self.browser.current_url
            assert re.match(expected_url, current_url), f"URL '{current_url}' does not match pattern '{expected_url.pattern}'"