import re
import allure


@allure.title('Check visibility of elements on main page')
def test_unauthorized_main_page_presence(main_page):
    main_page.check_main_page_presence()


@allure.title('Check redirect after click login button')
def test_redirect_after_click_login_button(main_page, login_page):
    main_page.click_login()
    main_page.check_current_url(re.compile(".*/#/login$"))
    login_page.check_login_page_presence()