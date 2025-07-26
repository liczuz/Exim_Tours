import pytest
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

@pytest.fixture
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page

def test_main_menu_visible(page):
    page.goto("https://www.eximtours.cz/")
    menu = page.locator("nav")
    assert menu.is_visible()

def test_title_eximtours(page):
    page.goto("https://www.eximtours.cz/")
    assert "EXIM tours" in page.title()

def test_click_on_pardubice(page):
    page.goto("https://www.eximtours.cz/")
    try:
        accept_button = page.locator("button:has-text('Přijmout vše')")
        accept_button.wait_for(timeout=2000)
        accept_button.click()
    except PlaywrightTimeoutError:
        pass
    pardubice_link = page.locator("a", has_text="Pardubice").first
    pardubice_link.click()
    page.wait_for_timeout(1000)
    assert "/odlety-pardubice" in page.url