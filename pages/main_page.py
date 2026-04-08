from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):
    URL = 'https://www.example.com'

    TOOL_BAR = (By.ID, "tool_bar")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Login')]")
    SEARCH_FIELD = (By.ID, 'desktop_search')
    INFO_BOX_1 = (By.CSS_SELECTOR, "#info_box1")
    INFO_BOX_2 = (By.CSS_SELECTOR, "#info_box2")
    PROMO_FIELD = (By.CLASS_NAME, "promo")
    FOOTER = (By.CSS_SELECTOR, '.py-3.bg-grey')
    WELCOME_TEXT = (By.ID, 'welcome_text')

    def check_main_page_presence(self):
        elements = {
            "Tool bar": self.TOOL_BAR,
            "Login button": self.LOGIN_BUTTON,
            "Search field": self.SEARCH_FIELD,
            "Info box 1": self.INFO_BOX_1,
            "Info box 2": self.INFO_BOX_2,
            "Promo field": self.PROMO_FIELD,
            "Footer": self.FOOTER
        }

        for name, locator in elements.items():
            step = f'Checking that element {name} is presented on the page'
            with allure.step(step):
                element = self.wait_for_visibility(locator)
                assert element.is_displayed(), f"Element {name} is not visible"

    def click_login(self):
        step = f'Click Login button'
        with allure.step(step):
            login_button = self.wait_for_visibility(self.LOGIN_BUTTON)
            login_button.click()

    def check_user_logged_in(self, user_name):
        step = f'Check that user {user_name} has logged in'
        with allure.step(step):
            actual_text = self.get_text(self.WELCOME_TEXT)
            expected_text = f"Welcome, {user_name}"
            assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"


