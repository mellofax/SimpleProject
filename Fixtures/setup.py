import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
from Core.Config import configurePlaywright

@pytest.fixture(autouse=True, scope="function")
def page() -> Page:
    playwright = sync_playwright().start()
    browser = get_browser(playwright)
    context = get_context(browser)
    page_data = context.new_page()
    yield page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()

def get_browser(playwright) -> Browser:
    if configurePlaywright.BROWSER == "firefox":
        return playwright.firefox.launch(
            headless=configurePlaywright.IS_HEADLESS,
            timeout=configurePlaywright.TIMEOUT
        )
    elif configurePlaywright.BROWSER == "chrome":
        return playwright.chromium.launch(
            headless=configurePlaywright.IS_HEADLESS,
            timeout=configurePlaywright.TIMEOUT
        )

def get_context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport=configurePlaywright.PAGE_VIEWPORT_SIZE,
        locale=configurePlaywright.LOCALE
    )
    context.set_default_timeout(
        timeout=configurePlaywright.TIMEOUT
    )
    return context


