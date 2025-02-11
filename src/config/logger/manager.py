from typing import Dict, List

from loguru import logger

from config.logger.handlers.base import BaseLoggerHandler


class LoggerManager:
    """Logger manager that accepts multiple log handlers."""

    _handlers: Dict[str, BaseLoggerHandler] = {}

    @classmethod
    def clear_handlers(cls) -> None:
        logger.remove()
        cls._handlers.clear()

    @classmethod
    def register_handler(
        cls, handler_name: str, handler_instance: BaseLoggerHandler
    ) -> None:
        cls._handlers[handler_name] = handler_instance

    @classmethod
    def load_handlers(cls, use_handlers: List[str]) -> None:
        logger.remove()
        for handler_name in use_handlers:
            handler_instance = cls._handlers.get(handler_name)
            if not handler_instance:
                raise ValueError(f"Handler {handler_name} not found")

            handler_instance.setup()
