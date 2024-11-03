class BasePage:
    def __init__(self, page, url):
        self.page = page
        self.url = url

    def open_browser(self):
        self.page.goto(self.url)

    def button_click(self, locator):
        self.page.click(locator)
