from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from tempfile import mkdtemp

@pytest.fixture(scope='session')
def web_driver():
    # options = Options()
    # options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    # options.add_argument('--disable-dev-shm-usage')

    # options.add_argument("start-maximized")
    # options.add_argument("disable-infobars")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--no-sandbox")
    # options.add_argument('--headless')
    # options.binary_location = "/usr/bin/chromium-browser"
    #
    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/bin/chromium-browser'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome("chromedriver",
                              options=options, service_args=["--verbose", "--log-path=/home/valerya/PycharmProjects/qc1.log"])

    # driver = webdriver.Chrome( options=options, service_args=["--verbose", "--log-path=/home/valerya/PycharmProjects/qc1.log"])
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
