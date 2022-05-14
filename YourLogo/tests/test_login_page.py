from tests.YourLogo.pages.Login_page import LoginPage
from tests.YourLogo.configs.config_parser import email_true, password_true
from tests.YourLogo.configs.config_parser import account_info, password_false
from tests.YourLogo.configs.config_parser import error_text


class TestLoginPage:

    def test_login_page(self, browser):
        login_page = LoginPage(browser)
        login_page.open_login_page()
        result = login_page.it_is_login_page()
        assert result == LoginPage.login_url

    def test_login_true(self, browser):
        login_page = LoginPage(browser)
        login_page.open_login_page()
        result = login_page.login_true(email_true, password_true)
        assert result == account_info

    def test_login_false(self, browser):
        login_page = LoginPage(browser)
        login_page.open_login_page()
        result = login_page.login_false(email_true, password_false)
        assert result == error_text
