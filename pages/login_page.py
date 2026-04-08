from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class LoginPage(BasePage):
    URL = 'https://www.example.com/login'

    USER_NAME_FIELD = (By.ID, 'user_name')
    PASSWORD_FIELD = (By.ID, 'password')
    SUBMIT_BUTTON = (By.ID, 'submit')
    ERROR_TEXT_AREA = (By.ID, 'error_box')

    def check_login_page_presence(self):
        elements = {
            "User name": self.USER_NAME_FIELD,
            "Password": self.PASSWORD_FIELD,
            "Submit": self.SUBMIT_BUTTON
        }

        for name, locator in elements.items():
            step = f'Checking that element {name} is presented on the page'
            with allure.step(step):
                element = self.wait_for_visibility(locator)
                assert element.is_displayed(), f"Element {name} is not visible"

    def fill_login_form(self, user_name, password):
        step = f'Fill login form'
        with allure.step(step):
            user_field = self.wait_for_visibility(self.USER_NAME_FIELD)
            password_field = self.wait_for_visibility(self.PASSWORD_FIELD)
            user_field.send_keys(user_name)
            password_field.send_keys(password)

    def click_submit_button(self):
        step = f'Click Submit button'
        with allure.step(step):
            submit_button = self.wait_for_visibility(self.SUBMIT_BUTTON)
            submit_button.click()

    def check_error_text(self, text):
        step = f'Check that error text "{text}" is presented when bad credentials'
        with allure.step(step):
            error_text_area = self.wait_for_visibility(self.ERROR_TEXT_AREA)
            error_text = self.get_text(self.ERROR_TEXT_AREA)
            assert error_text_area.is_displayed(), "Error text box is not visible"
            assert error_text == text, f"Expected {text}, got {error_text} instead"


