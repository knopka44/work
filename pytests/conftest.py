import pytest
from School.school_py import *
from lesson_21.task_2_info import *
from lesson_21.task_1_info import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# School
@pytest.fixture(scope='class')
def students():
    print('\nAdding students to school')
    school = School()
    lera = Students("Agrest", 1, [10, 10, 9, 10, 9])
    nikita = Students("Popov", 2, [6, 6, 7, 6, 7])
    sveta = Students('Larina', 2, [5, 5, 6, 5, 5])
    kate = Students("Kozlova", 3, [6, 6, 7, 6, 7])
    school.add_student(lera)
    school.add_student(nikita)
    school.add_student(sveta)
    school.add_student(kate)
    yield school
    del school.students[:]
    print('\nThere is no any student at school')


# lesson 21 task 1
@pytest.fixture(scope='class')
def driver1():
    print('\nOpen browser with site for test')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url1)
    driver.implicitly_wait(3)
    yield driver
    print('\nQuit browser')
    driver.quit()


# lesson 21 task 2
@pytest.fixture(scope='class')
def driver2():
    print('\nOpen browser with site for test')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url2)
    driver.implicitly_wait(3)
    yield driver
    print('\nQuit browser')
    driver.quit()


@pytest.fixture(scope='class')
def precondition(driver2):
    first_name = driver2.find_element(by=By.NAME, value="firstName")
    first_name.click()
    first_name.send_keys(user_first_name)
    last_name = driver2.find_element(by=By.NAME, value="lastName")
    last_name.click()
    last_name.send_keys(user_last_name)
    phone = driver2.find_element(by=By.NAME, value="phone")
    phone.click()
    phone.send_keys(user_phone)
    email = driver2.find_element(by=By.ID, value="userName")
    email.click()
    email.send_keys(user_email)
    address = driver2.find_element(by=By.NAME, value="address1")
    address.click()
    address.send_keys(user_address)
    city = driver2.find_element(by=By.NAME, value="city")
    city.click()
    city.send_keys(user_city)
    state_province = driver2.find_element(by=By.NAME, value="state")
    state_province.click()
    state_province.send_keys(user_state_province)
    postal_code = driver2.find_element(by=By.NAME, value="postalCode")
    postal_code.click()
    postal_code.send_keys(user_postal_code)
    country = Select(driver2.find_element(by=By.NAME, value="country"))
    country.select_by_value(country_value)
    my_user_name = driver2.find_element(by=By.ID, value="email")
    my_user_name.click()
    my_user_name.send_keys(user_name)
    password = driver2.find_element(by=By.NAME, value="password")
    password.click()
    password.send_keys(user_password)
    conf_passw = driver2.find_element(by=By.NAME, value="confirmPassword")
    conf_passw.click()
    conf_passw.send_keys(user_password)
    submit = driver2.find_element(by=By.NAME, value="submit")
    submit.click()
