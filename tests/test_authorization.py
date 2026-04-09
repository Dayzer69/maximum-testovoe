import re
import allure


@allure.title('Unsuccessful authorization with invalid credentials')
def test_unsuccessful_authorization(login_page):
    login_page.check_login_page_presence()
    login_page.fill_login_form(user_name="test", password="test")
    login_page.click_submit_button()
    login_page.check_error_text("Invalid credentials")


@allure.title('Successful authorization with valid credentials')
def test_successful_authorization(login_page, main_page):
    login_page.check_login_page_presence()
    login_page.fill_login_form(user_name="user", password="password")
    login_page.click_submit_button()
    main_page.check_current_url(re.compile(r"https://www\.example\.com/?$"))
    main_page.check_user_logged_in('user')


@allure.title('Logout by clicking logout button')
def test_user_logout(login_page, main_page):
    login_page.check_login_page_presence()
    login_page.fill_login_form(user_name="user", password="password")
    login_page.click_submit_button()
    main_page.click_logout()
    main_page.check_current_url(re.compile(r"https://www\.example\.com/?$"))
    main_page.check_main_page_presence()



