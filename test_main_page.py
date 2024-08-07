from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators
from pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, MainPageLocators.MAIN_LINK)
    main_page.open()
    main_page.go_to_login_page()
    login_url = browser.current_url
    guest_can_see_login_and_regist_forms(browser, login_url)


def guest_can_see_login_and_regist_forms(browser, login_url):
    login_page = LoginPage(browser, login_url)
    login_page.open()
    login_page.should_be_login_url(login_url)
    login_page.should_be_login_form()
    login_page.should_be_register_form()


def test_guest_should_see_login_link(browser):
    main_page = MainPage(browser, MainPageLocators.LOGIN_LINK)
    main_page.open()
    main_page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, MainPageLocators.MAIN_LINK)
    main_page.open()
    main_page.go_to_basket()
    basket_url = browser.current_url
    guest_see_empty_basket(browser, basket_url)


def guest_see_empty_basket(browser, basket_url):
    basket_page = BasketPage(browser, basket_url)
    basket_page.open()
    basket_page.basket_is_empty()
    basket_page.should_be_empty_basket_message()










