from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def web_driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestGoogle:

    def test_url(self, web_driver):
        current_url = web_driver.current_url
        assert current_url == "https://www.google.com/"

    def test_title(self, web_driver):
        title = web_driver.title
        assert title == "Google"
