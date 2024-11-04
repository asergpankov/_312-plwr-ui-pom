import pytest

from pages.scrollbars_page import ScrollbarsPage
from playwright.sync_api import Page, expect


# @pytest.mark.skip_browser("firefox")
class TestScrollbars:
    def test_scrollbar(self, page: Page):
        page1 = ScrollbarsPage(page, '/scrollbars')
        page1.open_browser()
        page1.hiding_button_click()
        page1.check_hiding_button_is_visible()

    def test_sampleapp_fill_data_(self, page: Page):
        page1 = ScrollbarsPage(page, '/sampleapp')
        page1.open_browser()
        name = 'padre'
        page1.set_login_password(name, 'pwd')
        page1.check_login_was_success(f"Welcome, {name}!")

# @pytest.mark.skip_browser("firefox")
# def test_client_site_delay(page):
#     page.goto('/clientdelay')
#     page.click('//button[@id="ajaxButton"]')
#     page.click('text=Data calculated on the client side.')
#
#
# def test_sample_app(page):
#     page.goto('/sampleapp')
#     page.click('[name="UserName"]')
#     page.fill('[name="UserName"]', 'Randy1')
#     page.press('[name="UserName"]', 'Tab')
#     page.fill('[placeholder="********"]', 'pwdd')
#     page.click('text=Log In')
#     page.click(f'text=Welcome, Randy1')

# @pytest.mark.skip_browser("firefox")
# def test_has_title(page: Page):
#     page.goto("/")
#     expect(page).to_have_title(re.compile("Swag Labs"))


# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")
#
#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()
#
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()
