from pathlib import Path

from loguru import logger

from config.logger.handlers.base import BaseLoggerHandler


class FileLogHandler(BaseLoggerHandler):
    """File log handler using loguru."""

    def __init__(
        self,
        fmt: str,
        log_file_path: Path,
        log_filename: str,
        log_level: str = "DEBUG",
    ):
        super().__init__(fmt, log_level)
        self._log_file_path = log_file_path
        self._log_filename = log_filename

    def setup(self) -> None:
        logger.add(
            sink=self._log_file_path / self._log_filename,
            level=self._log_level,
            format=self._fmt,
            backtrace=True,
            diagnose=True,
        )
