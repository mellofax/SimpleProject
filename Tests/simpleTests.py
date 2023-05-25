import re
import time

from playwright.sync_api import expect
from Core.Utils.loggingUtils import LoggingUtils
from Core.Utils.screenshotUtils import ScreenshotUtils
from Core.Config import configurePlaywright
class firstTests:
    def test_first(self, page):
        LoggingUtils.log("Open URL %s" % configurePlaywright.URL)
        page.goto(configurePlaywright.URL)
        ScreenshotUtils.make_screenshot(page, "Test screenshot")
        expect(page).to_have_title(re.compile("Playwright"))
        get_started = page.get_by_role("link", name="Get started")
        expect(get_started).to_have_attribute("href", "/docs/intro")
        get_started.click()
        time.sleep(4)
        expect(page).to_have_url(re.compile(".*intro"))

    def test_second(self, page):
        LoggingUtils.log("Open URL %s" % configurePlaywright.URL)
        page.goto(configurePlaywright.URL)
        ScreenshotUtils.make_screenshot(page, "Test screenshot")
        expect(page).to_have_title(re.compile("Playwright"))
        get_started = page.get_by_role("link", name="Get started")
        expect(get_started).to_have_attribute("href", "/docs/intro")
        get_started.click()
        time.sleep(4)
        expect(page).to_have_url(re.compile(".*intro"))
