from locators.scrollbars_page_locators import ScrollbarsPageLocators
from pages.base_page import BasePage


class ScrollbarsPage(BasePage):
    locator = ScrollbarsPageLocators()

    def hiding_button_click(self):
        self.button_click(self.locator.HIDING_BTN)
