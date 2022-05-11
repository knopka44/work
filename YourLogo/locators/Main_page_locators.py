from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH = (By.ID, 'search_query_top')
    TABS = (By.ID, 'home-page-tabs')
    POPULAR = (By.CLASS_NAME, 'homefeatured')
    BESTSELLER = (By.CLASS_NAME, 'blockbestsellers')
