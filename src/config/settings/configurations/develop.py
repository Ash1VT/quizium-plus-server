from pathlib import Path
from typing import List, Optional

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from config.constants.directory import ENV_DIRECTORY, LOGS_DIRECTORY
from config.settings.configurations.base import BaseSettings


class DevelopSettings(BaseSettings):
    # APP SETTINGS
    app_version: str = "develop"
    workers: int = Field(default=0)

    # DATABASE
    database_url: str

    # CORS
    cors_allowed_origins: List[str] = ["*"]
    cors_allowed_methods: List[str] = ["*"]
    cors_allowed_headers: List[str] = ["*"]

    # LOGGER
    log_level: str = "DEBUG"
    log_handlers: List[str] = ["console", "file"]

    # FILE LOGGER
    file_path: Path = LOGS_DIRECTORY
    filename: str = "develop.logs"

    # GRAYLOG
    graylog_host: str = Field(default="")
    graylog_udp_port: int = Field(default=0)
