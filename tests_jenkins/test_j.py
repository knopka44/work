import pytest
from selenium import webdriver

from test_j_info import *
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import warnings


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicControlsPageLocators:

    CHECKBOX = (By.ID, 'checkbox')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '#checkbox-example > button')
    MESSAGE = (By.ID, 'message')
    INPUT_FIELD = (By.CSS_SELECTOR, '#input-example > input')
    ENABLE_BUTTON = (By.CSS_SELECTOR, '#input-example > button')


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def current_url(self):
        return self.browser.current_url

    def find_element(self, locator, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        elements = WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def send_keys(self, locator, keys):
        element = self.find_element(locator)
        element.send_keys(keys)

    def wait_for_visibility_of_element(self, locator):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of(self.find_element(locator)))

    def is_element_present(self, *locator):
        return len(self.browser.find_elements(*locator))

    def get_count_of_elements(self, locator):
        elements = self.find_elements(locator)
        return len(elements)

    def get_text_of_elements(self, locator):
        elements = self.find_elements(locator)
        result = []
        for element in elements:
            result.append(element.text)
        return result

    def get_text_of_element(self, locator):
        element = self.find_element(locator)
        return element.text

    def select(self, locator, value):
        Select(self.find_element(locator)).select_by_value(value)


class DynamicControlsPage(BasePage):

    def remove_checkbox(self):
        self.find_element(DynamicControlsPageLocators.REMOVE_BUTTON).click()
        self.wait_for_visibility_of_element(DynamicControlsPageLocators.MESSAGE)

    def is_checkbox_present(self):
        return self.is_element_present(*DynamicControlsPageLocators.CHECKBOX)

    def is_element_disabled(self):
        return self.find_element(DynamicControlsPageLocators.INPUT_FIELD).get_property('disabled')

    def click_on_enable_button(self):
        self.find_element(DynamicControlsPageLocators.ENABLE_BUTTON).click()
        self.wait_for_visibility_of_element(DynamicControlsPageLocators.MESSAGE)



@pytest.fixture(scope='class')
def driver():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    browser.set_window_size(1920, 1080)
    
    browser.get(url)
    browser.implicitly_wait(2)
    yield browser
    browser.quit()


def test_remove_checkbox(driver):
    page = DynamicControlsPage(driver)
    page.remove_checkbox()
    assert page.is_checkbox_present() == 0


def test_disabled_input(driver):
    page = DynamicControlsPage(driver)
    assert page.is_element_disabled() is True


def test_enabled_input(driver):
    page = DynamicControlsPage(driver)
    page.click_on_enable_button()
    assert page.is_element_disabled() is False
