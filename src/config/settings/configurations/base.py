from abc import ABC, abstractclassmethod, abstractmethod
from pathlib import Path
from typing import List, Optional

from pydantic import Field
from pydantic_settings import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings, ABC):
    # APP SETTINGS
    app_name: str = "Quizium Plus"
    app_version: str
    app_description: str = "App description"
    web_app_host: str
    web_app_port: int
    workers: int

    # DATABASE
    database_url: str
    orm: str

    # CORS
    cors_allowed_origins: List[str]
    cors_allowed_methods: List[str]
    cors_allowed_headers: List[str]

    # LOGGER
    log_level: str
    log_handlers: List[str]

    file_path: Path
    filename: str

    graylog_host: str
    graylog_udp_port: int
