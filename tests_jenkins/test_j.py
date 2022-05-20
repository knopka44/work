import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_j_info import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome("homework/chromedriver")
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(10)
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
