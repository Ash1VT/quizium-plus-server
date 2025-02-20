import sys

from loguru import logger

from config.logger.handlers.base import BaseLoggerHandler


class ConsoleLogHandler(BaseLoggerHandler):
    """Console log handler using loguru."""

    def __init__(self, fmt: str, log_level: str = "DEBUG"):
        super().__init__(fmt, log_level)

    def setup(self) -> None:
        logger.add(
            sink=sys.stderr,
            level=self._log_level,
            format=self._fmt,
            colorize=True,
            backtrace=True,
            diagnose=True,
        )
