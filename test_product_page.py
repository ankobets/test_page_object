import time
import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

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
#     prod_page = ProductPage(browser, link)
#     prod_page.open()
#     prod_page.add_to_basket()
#     prod_page.solve_quiz_and_get_code()
#     time.sleep(5)
#     prod_page.check_right_title()
#     prod_page.check_right_price()


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
