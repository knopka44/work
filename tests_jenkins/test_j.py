import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_j_info import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@pytest.fixture(scope='class')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1420,1080')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestDynamicControls:

    @allure.feature("Checkbox")
    @allure.story("Check checkbox is gone")
    def test_checkbox_is_gone(self, driver):
        with allure.step("Find checkbox locator"):
            checkbox = driver.find_element(by=By.XPATH, value=f'{checkbox_site}')
            checkbox.click()
        with allure.step("Find remove button locator"):
            remove = driver.find_element(by=By.XPATH, value=f'{remove_site}')
            remove.click()
        with allure.step("Find message text locator"):
            message = driver.find_element(by=By.ID, value=f'{message_site}')
        with allure.step("Wait until message is visible"):
            WebDriverWait(driver, 15).until(EC.visibility_of(message))
        with allure.step("Wait until checkbox is invisible"):
            invisibility = WebDriverWait(driver, 15).until(
                EC.invisibility_of_element(checkbox))
        with allure.step("Assertion invisibility it true "):
            assert invisibility is True

    @allure.feature("Input")
    @allure.story("Check input is disabled")
    def test_input_disabled(self, driver):
        with allure.step("Find input locator"):
            input_text = driver.find_element(by=By.XPATH, value=f'{input_site}')
        with allure.step("Assertion input is disabled "):
            assert input_text.get_attribute('disabled') == 'true'

    @allure.feature("Input")
    @allure.story("Check input is enabled")
    def test_input_enabled(self, driver):
        with allure.step("Find enable button locator"):
            enable = driver.find_element(by=By.XPATH, value=f'{enable_site}')
            enable.click()
        with allure.step("Find message text locator"):
            message = driver.find_element(by=By.ID, value=f'{message_site}')
        with allure.step("Wait until message is visible"):
            WebDriverWait(driver, 15).until(EC.visibility_of(message))
        with allure.step("Find input locator"):
            input_text = driver.find_element(by=By.XPATH, value=f'{input_site}')
        with allure.step("Assertion input is not disabled "):
            assert input_text.get_attribute('disabled') is None
