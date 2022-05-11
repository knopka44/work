from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL = (By.ID, "email")
    LOGIN = (By.CLASS_NAME, "login")
    PASSWORD = (By.ID, "passwd")
    SUBMIT = (By.ID, "SubmitLogin")
    ACCOUNT_INFO = (By.CLASS_NAME, 'info-account')
    ERROR = (By.XPATH, '//*[@id="center_column"]/div[1]/p')
