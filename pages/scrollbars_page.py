from locators.scrollbars_page_locators import ScrollbarsPageLocators
from pages.base_page import BasePage


class ScrollbarsPage(BasePage):
    locator = ScrollbarsPageLocators()

    def hiding_button_click(self):
        self.click_on_element(self.locator.HIDING_BTN)

    def check_hiding_button_is_visible(self):
        self.check_element_is_visible(self.locator.HIDING_BTN)

    def set_login_password(self, login, password):
        self.set_value(self.locator.LOGIN_FLD, login)
        self.set_value(self.locator.PASSWORD_FLD, password)
        self.click_on_element(self.locator.LOGIN_BTN)

    def check_login_was_success(self, login_msg):
        self.check_element_has_text(self.locator.LOGIN_MSG, login_msg)
