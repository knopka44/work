from selenium.webdriver.common.by import By
from task_1_info import *


class TestTask1:

    def test_successful_login(self, driver1):
        sign_in = driver1.find_element(by=By.CLASS_NAME, value="login")
        sign_in.click()
        email = driver1.find_element(by=By.ID, value="email")
        email.click()
        email.send_keys(email1)
        password = driver1.find_element(by=By.ID, value="passwd")
        password.click()
        password.send_keys(password1)
        submit = driver1.find_element(by=By.ID, value="SubmitLogin")
        submit.click()
        account_info = driver1.find_element(by=By.CLASS_NAME,
                                            value="info-account").text
        assert account_info == text_info

    def test_unsuccessful_login(self, driver1):
        sign_out = driver1.find_element(by=By.CLASS_NAME, value="logout")
        sign_out.click()
        email = driver1.find_element(by=By.ID, value="email")
        email.click()
        email.send_keys(email1_negative)
        password = driver1.find_element(by=By.ID, value="passwd")
        password.click()
        password.send_keys(password1)
        submit = driver1.find_element(by=By.ID, value="SubmitLogin")
        submit.click()
        error = driver1.find_element(by=By.XPATH,
                                     value="//*[@id='center_column']/div[1]/p")
        assert error.text == error_text
