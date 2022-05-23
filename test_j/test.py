import allure
from selenium import webdriver
import pytest


@pytest.fixture(scope='session')
def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1420,1080')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestGoogle:

    @allure.story("Check Google's url")
    def test_url(self, web_driver):
        with allure.step("Define current url"):
            current_url = web_driver.current_url
        with allure.step("Assert current url equals Google's url"):
            assert current_url == "https://www.google.com/"

    @allure.story("Check title of the Google's site")
    def test_title(self, web_driver):
        with allure.step("Define url's title"):
            title = web_driver.title
        with allure.step("Assert current title equals Google's title"):
            assert title == "Google"
