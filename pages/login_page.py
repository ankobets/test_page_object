from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self, login_url):
        assert 'login' in login_url, "Url has no 'login' "

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Registration form is not present'

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        password_check_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CHECK_FIELD)
        password_check_field.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        button.click()
