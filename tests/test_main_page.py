import re


def test_unauthorized_main_page_presence(main_page):
    main_page.check_main_page_presence()


def test_redirect_after_click_login_button(main_page):
    main_page.click_login()
    main_page.check_current_url(re.compile(".*/#/login$"))