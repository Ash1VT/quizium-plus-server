import graypy
from loguru import logger

from config.logger.handlers.base import BaseLoggerHandler


class GraylogLogHandler(BaseLoggerHandler):
    """Graylog handler using graypy."""

    def __init__(
        self,
        fmt: str,
        graylog_host: str,
        graylog_udp_port: int,
        log_level: str = "DEBUG",
    ):
        super().__init__(fmt, log_level)
        self.graylog_host = graylog_host
        self.graylog_udp_port = graylog_udp_port

    def setup(self) -> None:
        graylog_handler = graypy.GELFUDPHandler(
            self.graylog_host, self.graylog_udp_port
        )
        logger.add(
            sink=graylog_handler,
            level=self._log_level,
            format=self._fmt,
            backtrace=True,
            diagnose=True,
        )
