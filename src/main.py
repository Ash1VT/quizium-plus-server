import os

from loguru import logger

from config.app.manager import AppManager
from config.constants.logger import SIMPLE_LOG_FORMAT, COMPREHENSIVE_LOG_FORMAT
from config.logger.handlers.console import ConsoleLogHandler
from config.logger.handlers.file import FileLogHandler
from config.logger.handlers.graylog import GraylogLogHandler
from config.orm.configurations.sqlalchemy import AsyncSqlAlchemyOrmConfig
from config.orm.manager import OrmManager
from config.settings.configurations.test import TestSettings
from config.settings.manager import SettingsManager
from config.logger.manager import LoggerManager
from config.settings.configurations.develop import DevelopSettings
from config.settings.configurations.production import ProductionSettings

configuration = os.getenv("CONFIGURATION", "development")
env_file = os.getenv("ENV_FILE", ".env")

# SETTINGS
SettingsManager.register_config("development", DevelopSettings)
SettingsManager.register_config("production", ProductionSettings)
SettingsManager.register_config("test", TestSettings)
SettingsManager.load_settings(configuration, env_file=env_file)

settings = SettingsManager.get_settings()

# LOGGER
LoggerManager.register_handler(
    "console", ConsoleLogHandler(COMPREHENSIVE_LOG_FORMAT, settings.log_level)
)

LoggerManager.register_handler(
    "file",
    FileLogHandler(
        COMPREHENSIVE_LOG_FORMAT,
        settings.file_path,
        settings.filename,
        settings.log_level,
    ),
)

LoggerManager.register_handler(
    "graylog",
    GraylogLogHandler(
        SIMPLE_LOG_FORMAT,
        settings.graylog_host,
        settings.graylog_udp_port,
        settings.log_level,
    ),
)

LoggerManager.load_handlers(settings.log_handlers)

logger.info(
    f"Logger initialized with level: {settings.log_level}. "
    f"Using handlers: {settings.log_handlers}"
)
logger.info(f"Using settings: {configuration}")

# ORM
OrmManager.register_orm_config(
    "sqlalchemy",
    AsyncSqlAlchemyOrmConfig(
        database_url=settings.database_url, expire_session_on_commit=False
    ),
)
OrmManager.load_orm_config(settings.orm)

logger.info(f"Orm initialized: {settings.orm}")


# APP
AppManager.setup_app()
logger.info(f"App created: {settings.app_name}")
AppManager.register_cors(
    settings.cors_allowed_origins,
    settings.cors_allowed_methods,
    settings.cors_allowed_headers,
)
logger.info(
    f"CORS initialized. "
    f"Allowed origins: {settings.cors_allowed_origins}. "
    f"Allowed methods: {settings.cors_allowed_methods}. "
    f"Allowed headers: {settings.cors_allowed_headers}"
)
app = AppManager.get_app()


@app.get("/ping")
async def ping():
    return "pong"
