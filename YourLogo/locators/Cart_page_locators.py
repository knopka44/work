from selenium.webdriver.common.by import By


class CartPageLocators:

    CART_EMPTY = (By.CSS_SELECTOR, "p.alert")
    T_SHIRTS = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a')
    VIEW = (By.CLASS_NAME, 'product_img_link')
    ADD_TO_CART = (By.NAME, 'Submit')
    PROCEED = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')
    QUANTITY = (By.ID, 'summary_products_quantity')
