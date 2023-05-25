from Core.Utils.loggingUtils import LoggingUtils
from Core.Utils.randomUtils import RandomUtils


class ScreenshotUtils:
    @classmethod
    def make_screenshot(cls, page, message):
        image_path = ".pytest_cache/screenshots/" + RandomUtils.generate_random_numbers(10) + ".png"
        page.screenshot(path=image_path, full_page=True)
        LoggingUtils.log_screenshot(image_path, message)
