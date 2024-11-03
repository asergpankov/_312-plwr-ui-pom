import pytest
from pages.scrollbars_page import ScrollbarsPage


# @pytest.mark.skip_browser("firefox")
class TestScrollbars:
    def test_scrollbar(self, page):
        page = ScrollbarsPage(page, '/scrollbars')
        page.open_browser()
        page.hiding_button_click()


@pytest.mark.skip_browser("firefox")
def test_client_site_delay(page):
    page.goto('/clientdelay')
    page.click('//button[@id="ajaxButton"]')
    page.click('text=Data calculated on the client side.')


def test_sample_app(page):
    page.goto('/sampleapp')
    page.click('[name="UserName"]')
    page.fill('[name="UserName"]', 'Randy1')
    page.press('[name="UserName"]', 'Tab')
    page.fill('[placeholder="********"]', 'pwdd')
    page.click('text=Log In')
    page.click(f'text=Welcome, Randy1')

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
