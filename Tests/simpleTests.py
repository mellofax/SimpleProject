import re
import time

from playwright.sync_api import expect
from Core.Config import configurePlaywright
class firstTests:
    def test_first(self, page):
        page.goto(configurePlaywright.URL)
        expect(page).to_have_title(re.compile("Playwright"))
        get_started = page.get_by_role("link", name="Get started")
        expect(get_started).to_have_attribute("href", "/docs/intro")
        get_started.click()
        time.sleep(4)
        expect(page).to_have_url(re.compile(".*intro"))
