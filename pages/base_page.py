from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page, url):
        self.page = page
        self.url = url

    def open_browser(self):
        self.page.goto(self.url)

    def click_on_element(self, locator):
        self.page.click(locator)

    def check_element_is_visible(self, elem_locator):
        expect(self.page.locator(elem_locator)).to_be_visible()

    def check_element_has_text(self, elem_locator, target_text):
        expect(self.page.locator(elem_locator)).to_have_text(target_text)

    def set_value(self, elem_locator, value):
        self.page.fill(elem_locator, value)

    def get_elem_text(self, elem_locator):
        return self.page.locator(elem_locator).inner_text()

