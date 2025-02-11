from pathlib import Path
from typing import List, Optional

from pydantic import Field, PrivateAttr
from pydantic_settings import SettingsConfigDict

from config.constants.directory import ENV_DIRECTORY
from config.settings.configurations.base import BaseSettings


class ProductionSettings(BaseSettings):
    # APP SETTINGS
    app_version: str = "1.0.0"

    # DATABASE
    database_url: str

    # CORS (from env)

    # LOGGER
    log_level: str = "INFO"
    log_handlers: List[str] = ["graylog"]

    file_path: Path = Field(default=Path(), validate_default=False, exclude=True)
    filename: str = Field(default="", validate_default=False, exclude=True)

    # GRAYLOG LOGGER
    graylog_host: str
    graylog_udp_port: int
