from tests.YourLogo.pages.Base_page import BasePage
from tests.YourLogo.locators.Cart_page_locators import CartPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):

    cart_url = BasePage.main_url + '?controller=order'

    def open_cart_page(self):
        self.open(self.cart_url)

    def it_is_cart_page(self):
        current_url = self.driver.current_url
        return current_url

    def cart_is_empty(self):
        empty = self.find_element(CartPageLocators.CART_EMPTY)
        return empty.text

    def cart_with_clothes(self):
        t_shirts = self.find_element(CartPageLocators.T_SHIRTS)
        t_shirts.click()
        view = self.find_element(CartPageLocators.VIEW)
        view.click()
        add_to_cart = self.find_element(CartPageLocators.ADD_TO_CART)
        add_to_cart.click()
        proceed = self.find_element(CartPageLocators.PROCEED)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of(proceed))
        proceed.click()
        quantity = self.find_element(CartPageLocators.QUANTITY)
        return quantity.text
