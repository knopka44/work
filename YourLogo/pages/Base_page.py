from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    main_url = 'http://automationpractice.com/index.php'

    def __init__(self, driver):
        self.driver = driver
        self.url = None

    def find_element(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(locator))

    def open_main_page(self):
        return self.driver.get(self.main_url)

    def open(self, url):
        return self.driver.get(url)
