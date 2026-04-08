import re


def test_unsuccessful_authorization(login_page):
    login_page.check_login_page_presence()
    login_page.fill_login_form(user_name="test", password="test")
    login_page.click_submit_button()
    login_page.check_error_text("Invalid credentials")


def test_successful_authorization(login_page, main_page):
    login_page.check_login_page_presence()
    login_page.fill_login_form(user_name="user", password="password")
    login_page.click_submit_button()
    main_page.check_current_url(re.compile(r"https://www\.example\.com/?$"))
    main_page.check_user_logged_in('user')

