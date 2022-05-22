import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from test_j_info import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='class')
def driver():
    driver_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications: 2"}
    driver_options.add_experimental_option('prefs', prefs)
    driver_options.add_argument("user-agent=Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Mobile Safari/537.36 Edge/12.10166")
    driver_options.headless = True
    s = Service("chromedriver")
    driver = webdriver.Chrome(service=s, options=driver_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    yield driver
    driver.quit()


class TestDynamicControls:

    def test_checkbox_is_gone(self, driver):
        checkbox = driver.find_element(by=By.XPATH, value=f'{checkbox_site}')
        checkbox.click()
        remove = driver.find_element(by=By.XPATH, value=f'{remove_site}')
        remove.click()
        message = driver.find_element(by=By.ID, value=f'{message_site}')
        WebDriverWait(driver, 15).until(EC.visibility_of(message))
        invisibility = WebDriverWait(driver, 15).until(
            EC.invisibility_of_element(checkbox))
        assert invisibility is True

    def test_input_disabled(self, driver):
        input_text = driver.find_element(by=By.XPATH, value=f'{input_site}')
        assert input_text.get_attribute('disabled') == 'true'

    def test_input_enabled(self, driver):
        enable = driver.find_element(by=By.XPATH, value=f'{enable_site}')
        enable.click()
        message = driver.find_element(by=By.ID, value=f'{message_site}')
        WebDriverWait(driver, 15).until(EC.visibility_of(message))
        input_text = driver.find_element(by=By.XPATH, value=f'{input_site}')
        assert input_text.get_attribute('disabled') is None
