from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        try:
            self.click_alert()
        except NoAlertPresentException:
            return False
        else:
            return True

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


    def click_alert(self):
        alert = self.browser.switch_to.alert
        alert.access()
