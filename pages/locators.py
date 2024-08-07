from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_LINK = "http://selenium1py.pythonanywhere.com/"

class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    BUTTON_ADD_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    ADDED_PRODUCT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > p.price_color')
    ADDED_PRICE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, 'div #content_inner > p')
    BASKET_ITEMS = (By.CLASS_NAME, 'basket_summary')




