import pytest
from selenium import webdriver

from test_j_info import *
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import warnings
from dynamic_controls_page import *


@pytest.fixture(scope='class')
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
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
