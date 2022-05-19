import allure
from selenium import webdriver
import unittest


class GoogleTest(unittest.TestCase):
    browser = None
    google_title = "Google"
    google_url = "https://www.google.com/"

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome("/home/valerya/PycharmProjects/My_homework/chromedriver")
        cls.browser.maximize_window()
        cls.browser.get(cls.google_url)
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()

    @allure.story("Check Google's url")
    def test_url(self):
        with allure.step("Define current url"):
            current_url = self.browser.current_url
        with allure.step("Assert current url equals Google's url"):
            self.assertEqual(current_url, self.google_url)

    @allure.story("Check title of the Google's site")
    def test_title(self):
        with allure.step("Define url's title"):
            title = self.browser.title
        with allure.step("Assert current title equals Google's title"):
            self.assertEqual(title, self.google_title)


if __name__ == "__main__":
    unittest.main()
