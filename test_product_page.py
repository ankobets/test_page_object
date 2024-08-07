import time
import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators, BasePageLocators
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


# Parameterized test to verify the addition of an item to the cart with a captcha
# Uncomment if you want to take the test for the captcha page

# list_of_failed_num = [7]
# tested_links = [f"{ProductPageLocators.LINK}?promo=offer{i}" if i not in list_of_failed_num else
#                 pytest.param(f"{ProductPageLocators.LINK}?promo=offer{i}",
#                              marks=pytest.mark.xfail(reason="some bug", strict=True)
#                              )
#                 for i in range(6,10)]
#
# @pytest.mark.parametrize("link", tested_links)
# def test_guest_can_add_product_to_basket(browser, link):
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    # prod_page = ProductPage(browser, link)
    prod_page = ProductPage(browser, ProductPageLocators.LINK_PROMO)
    prod_page.open()
    prod_page.add_to_basket()
    prod_page.solve_quiz_and_get_code()
    time.sleep(5)
    prod_page.check_right_title()
    prod_page.check_right_price()


@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPageLocators.LINK
    prod_page = ProductPage(browser, link, 0)
    prod_page.open()
    prod_page.add_to_basket()
    prod_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.LINK
    prod_page = ProductPage(browser, link, 0)
    prod_page.open()
    prod_page.should_not_be_success_message()


@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.LINK
    prod_page = ProductPage(browser, link, 0)
    prod_page.open()
    prod_page.add_to_basket()
    prod_page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    prod_page = ProductPage(browser, ProductPageLocators.LINK)
    prod_page.open()
    prod_page.should_be_login_link()
    prod_page.go_to_login_page()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, ProductPageLocators.LINK)
    product_page.open()
    product_page.go_to_login_page()

    login_url = browser.current_url
    login_page = LoginPage(browser, login_url)
    login_page.open()
    login_page.should_be_login_url(login_url)
    login_page.should_be_login_form()
    login_page.should_be_register_form()
    time.sleep(3)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    prod_page = ProductPage(browser, ProductPageLocators.LINK)
    prod_page.open()
    prod_page.go_to_basket()

    basket_url = browser.current_url
    basket_page = BasketPage(browser, basket_url)
    basket_page.open()
    basket_page.basket_is_empty()
    basket_page.should_be_empty_basket_message()


@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, BasePageLocators.LOGIN_URL)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLocators.LINK
        prod_page = ProductPage(browser, link, 0)
        prod_page.open()
        prod_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        prod_page = ProductPage(browser, ProductPageLocators.LINK_PROMO)
        prod_page.open()
        prod_page.add_to_basket()
        prod_page.solve_quiz_and_get_code()
        time.sleep(5)
        prod_page.check_right_title()
        prod_page.check_right_price()
