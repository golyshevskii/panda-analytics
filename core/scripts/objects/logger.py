import inspect
import logging

LOG_FORMAT = "%(filename)s:%(lineno)d → %(func_name)s | %(levelname)s: %(message)s"


class CustomFormatter(logging.Formatter):
    def __init__(self, fmt):
        super().__init__(fmt)
        self.base_fmt = fmt

    def format(self, record):
        _, _, _, func_name, _, _ = inspect.getouterframes(inspect.currentframe())[8]
        record.func_name = func_name
        self._style._fmt = self.base_fmt
        return super().format(record)


# Set up the stream handler with custom formatter
handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter(LOG_FORMAT))
handler.setLevel(logging.INFO)

# Set up the logger
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.propagate = False
