from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):


    def should_be_login_url(self, login_url):
        # реализуйте проверку на корректный url адрес
        assert 'login' in login_url, "url has no 'login' "

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'registration form is not present'
