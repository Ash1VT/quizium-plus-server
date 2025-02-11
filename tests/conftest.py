import os

import pytest

from config.orm.configurations.sqlalchemy import AsyncSqlAlchemyOrmConfig
from config.orm.manager import OrmManager
from config.settings.configurations.develop import DevelopSettings
from config.settings.configurations.production import ProductionSettings
from config.settings.configurations.test import TestSettings
from config.settings.manager import SettingsManager
from core.uow.generic import GenericUnitOfWork

configuration = os.getenv("CONFIGURATION", "develop")
env_file = os.getenv("ENV_FILE", ".env")

SettingsManager.register_config("development", DevelopSettings)
SettingsManager.register_config("production", ProductionSettings)
SettingsManager.register_config("test", TestSettings)
SettingsManager.load_settings(configuration, env_file=env_file)

settings = SettingsManager.get_settings()

OrmManager.register_orm_config(
    "sqlalchemy",
    AsyncSqlAlchemyOrmConfig(
        database_url=settings.database_url, expire_session_on_commit=False
    ),
)
OrmManager.load_orm_config(settings.orm)

orm_config = OrmManager.get_orm_config()


@pytest.fixture(scope="session")
def uow() -> GenericUnitOfWork:
    return orm_config.get_uow()
