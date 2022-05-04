import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from info import *
import logging
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestLogin:

    logging.getLogger('urllib3').setLevel('CRITICAL')
    logging.getLogger('selenium').setLevel('CRITICAL')

    def test_loging(self, driver):
        username_site = driver.find_element(by=By.ID,
                                            value=f'{user_name_locator}')
        username_site.click()
        username_site.send_keys(f'{user_name}')
        password_site = driver.find_element(by=By.ID,
                                            value=f'{password_locator}')
        password_site.click()
        password_site.send_keys(f'{password}')
        login_site = driver.find_element(by=By.ID,
                                         value=f'{login_button_locator}')
        login_site.click()

        items = [el.text for el in driver.find_elements(by=By.CLASS_NAME,
                                                        value=f'{item_block}')]
        prices = [el.text for el in driver.find_elements(
            by=By.CLASS_NAME,
            value=f'{prices_block}')]
        titles_and_prices = dict(zip(items, prices))
        for item, price in titles_and_prices.items():
            logging.debug(f'{item}, price: {price}\n')

        current_url = driver.current_url
        assert current_url == url_after_login

    def test_shop_cart_click(self, driver):
        shop_cart = driver.find_element(by=By.CLASS_NAME,
                                        value=f'{shopcart_locator}')
        shop_cart.click()
        current_url = driver.current_url
        contin_shop = driver.find_element(by=By.ID,
                                          value=f'{contin_shop_locator}')
        contin_shop.click()
        assert current_url == shopcart_url

    def test_check_title(self, driver):
        title = driver.find_element(by=By.XPATH, value=f'{title_loc}')
        assert title.text == title_name

    def test_sort_items_hilo(self, driver):
        sort_hilo = Select(driver.find_element(by=By.CLASS_NAME,
                                               value=f'{sort_locator}'))
        sort_hilo.select_by_value('hilo')
        items = [el.text for el in driver.find_elements(
            by=By.CLASS_NAME,
            value='inventory_item_name')]
        hilo_items = items[0], items[-1]
        assert hilo_items == hilo_names

    def test_add_to_cart(self, driver):
        add_to_cart = driver.find_element(by=By.ID, value=f'{add_to_cart0_loc}')
        add_to_cart.click()
        badge = driver.find_element(by=By.CLASS_NAME, value=f'{badge_loc}')
        assert badge.text == badge_text

    def test_remove_from_cart(self, driver):
        remove = driver.find_element(by=By.ID, value=f'{remove_loc}')
        remove.click()
        add_to_cart = driver.find_element(by=By.ID,
                                          value=f'{add_to_cart0_loc}')
        assert add_to_cart.is_enabled()

    def test_twitter(self, driver):
        twiter = driver.find_element(by=By.LINK_TEXT, value=f'{twitter}')
        assert twiter.text == twitter

    def test_img(self, driver):
        img = driver.find_element(by=By.ID, value=f'{img_loc}')
        img.click()
        title = driver.find_element(by=By.CLASS_NAME, value=f'{title_img_loc}')
        assert title.text == img_name

    def test_menu_about(self, driver):
        menu = driver.find_element(by=By.CLASS_NAME, value=f'{menu_locator}')
        menu.click()
        about = driver.find_element(by=By.ID, value=f'{about_loc}')
        about.click()
        current_url = driver.current_url
        assert current_url == about_url
