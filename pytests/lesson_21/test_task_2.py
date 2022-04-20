from selenium.webdriver.common.by import By
from task_2_info import *


class TestTask2:

    def test_name_surname_positive(self, driver2, precondition):
        site_name_surname = driver2.find_element(
            by=By.XPATH,
            value=".//tr//table//p[1]/font/b"
        ).text
        assert site_name_surname.find(user_name_surname) != -1

    def test_name_surname_negative(self, driver2, precondition):
        site_name_surname = driver2.find_element(
            by=By.XPATH,
            value=".//tr//table//p[1]/font/b"
        ).text
        assert site_name_surname.find(not_user_name_surname) == -1

    def test_username_positive(self, driver2, precondition):
        site_username = driver2.find_element(
            by=By.XPATH,
            value=".//tr//table//p[3]/font/b"
        ).text
        assert site_username.find(user_username) != -1

    def test_username_negative(self, driver2, precondition):
        site_username = driver2.find_element(
            by=By.XPATH,
            value=".//tr//table//p[3]/font/b"
        ).text
        assert site_username.find(not_user_username) == -1
