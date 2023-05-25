import logging
import sys
from reportportal_client import RPLogger


class LoggingUtils:
    logging.setLoggerClass(RPLogger)
    __logger = logging.getLogger(__name__)
    __logger.setLevel(logging.DEBUG)
    __logger.addHandler(logging.StreamHandler(sys.stdout))

    @classmethod
    def log(cls, message):
        cls.__logger.info(message)

    @classmethod
    def log_screenshot(cls, file, message):
        with open(file, "rb") as image_file:
            file_data = image_file.read()
        cls.__logger.info("RP_MESSAGE#FILE#" + file + "#" + message,
                          extra=dict(attachment={"data": file_data, "mime": "image/png"}))
