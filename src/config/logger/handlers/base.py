from abc import ABC, abstractmethod


class BaseLoggerHandler(ABC):
    """Abstract base class for log handlers."""

    def __init__(self, fmt: str, log_level: str):
        self._log_level = log_level
        self._fmt = fmt

    @abstractmethod
    def setup(self) -> None:
        raise NotImplementedError
