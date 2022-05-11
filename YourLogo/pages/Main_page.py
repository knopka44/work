from tests.YourLogo.pages.Base_page import BasePage
from tests.YourLogo.locators.Main_page_locators import MainPageLocators
from tests.YourLogo.configs.config_parser import search_bar


class MainPage(BasePage):

    def main_page(self):
        self.open_main_page()

    def it_is_main_page(self):
        current_url = self.driver.current_url
        return current_url

    def search_field(self):
        search_field = self.find_element(MainPageLocators.SEARCH)
        search_field.send_keys(search_bar)
        search_field.clear()
        value_field = search_field.text
        return value_field

    def tabs(self):
        pop = self.find_element(MainPageLocators.POPULAR)
        best = self.find_element(MainPageLocators.BESTSELLER)
        names = f'{pop.text}, {best.text}'
        return names
