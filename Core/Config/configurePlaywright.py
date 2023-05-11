import os
class ConfigurePlaywright:
    PAGE_VIEWPORT_SIZE = {"width": 1700, "height": 1100}
    BROWSER = os.getenv("browser", default="chrome")
    IS_HEADLESS = os.getenv('headless', default=True)
    LOCALE = 'en-US'
    URL = "https://playwright.dev/"
    TIMEOUT = 60000


