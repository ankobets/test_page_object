from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button.click()

    def check_right_title(self):
        right_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT).text
        print(right_product, added_product)
        assert right_product == added_product, 'You added another product'

    def check_right_price(self):
        right_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        added_price = self.browser.find_element(*ProductPageLocators.ADDED_PRICE).text
        print(right_price, added_price)
        assert right_price == added_price, 'Wrong price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT),\
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT), \
            "Success message is presented, but should disappear"
