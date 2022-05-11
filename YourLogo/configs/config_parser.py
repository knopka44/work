import configparser


config = configparser.ConfigParser()
config.read('/home/valerya/PycharmProjects/My_homework/tests/YourLogo/configs'
            '/config.ini')

email_true = config.get("login_info", "email")
password_true = config.get("login_info", "password")
password_false = config.get("login_info", "password_false")
search_bar = config.get("main_page", "search_bar")
search_string = config.get("main_page", "search_str")
tabs_names = config.get("main_page", "tabs_names")
account_info = config.get("login_page", "account_info")
error_text = config.get("login_page", "error_text")
cart_empty = config.get("cart_page", "cart_empty")
quantity = config.get("cart_page", "quantity_of_goods")
