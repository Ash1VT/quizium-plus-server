from pathlib import Path
from typing import List

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from config.constants.directory import ENV_DIRECTORY
from config.settings.configurations.base import BaseSettings


class TestSettings(BaseSettings):
    # APP SETTINGS
    app_version: str = "test"
    workers: int = Field(default=0)

    # CORS
    cors_allowed_origins: List[str] = ["*"]
    cors_allowed_methods: List[str] = ["*"]
    cors_allowed_headers: List[str] = ["*"]

    # LOGGER
    log_level: str = "DEBUG"
    log_handlers: List[str] = []

    file_path: Path = Field(
        default=Path(), validate_default=False, exclude=True
    )
    filename: str = Field(default="", validate_default=False, exclude=True)

    graylog_host: str = Field(default="")
    graylog_udp_port: int = Field(default=0)
