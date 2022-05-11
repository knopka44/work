from tests.YourLogo.pages.Main_page import MainPage
from tests.YourLogo.pages.Login_page import LoginPage
from tests.YourLogo.pages.Cart_page import CartPage
from tests.YourLogo.configs.config_parser import *


class TestYourLogo:

    def test_main_page(self, browser):
        main_page = MainPage(browser)
        main_page.main_page()
        result = main_page.it_is_main_page()
        assert result == MainPage.main_url

    def test_search_bar(self, browser):
        main_page = MainPage(browser)
        main_page.main_page()
        result = main_page.search_field()
        assert result == search_string

    def test_tabs(self, browser):
        main_page = MainPage(browser)
        main_page.main_page()
        result = main_page.tabs()
        assert result == tabs_names

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

    def test_cart_page(self, browser):
        cart_page = CartPage(browser)
        cart_page.open_cart_page()
        result = cart_page.it_is_cart_page()
        assert result == CartPage.cart_url

    def test_cart_is_empty(self, browser):
        cart_page = CartPage(browser)
        cart_page.open_cart_page()
        result = cart_page.cart_is_empty()
        assert result == cart_empty

    def test_cart_with_clothes(self, browser):
        cart_page = CartPage(browser)
        cart_page.open_cart_page()
        result = cart_page.cart_with_clothes()
        assert result == quantity
