from tests.YourLogo.locators.Login_page_locators import LoginPageLocators
from tests.YourLogo.pages.Base_page import BasePage


class LoginPage(BasePage):

    login_url = BasePage.main_url + '?controller=authentication&back' \
                                     '=my-account'

    def open_login_page(self):
        self.open(self.login_url)

    def it_is_login_page(self):
        current_url = self.driver.current_url
        return current_url

    def get_email_field(self):
        field = self.find_element(LoginPageLocators.EMAIL)
        return field

    def fill_email_field(self, email):
        field = self.get_email_field()
        field.send_keys(email)
        return field

    def get_password_field(self):
        field = self.find_element(LoginPageLocators.PASSWORD)
        return field

    def fill_password_field(self, password):
        field = self.get_password_field()
        field.send_keys(password)
        return field

    def get_submit_field(self):
        field = self.find_element(LoginPageLocators.SUBMIT)
        return field

    def click_submit_field(self):
        field = self.get_submit_field()
        field.click()
        return field

    def login_true(self, email, password):
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_submit_field()
        acc_info = self.find_element(LoginPageLocators.ACCOUNT_INFO)
        return acc_info.text

    def login_false(self, email, password):
        self.find_element(LoginPageLocators.SIGN_OUT).click()
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_submit_field()
        error_info = self.find_element(LoginPageLocators.ERROR)
        return error_info.text
