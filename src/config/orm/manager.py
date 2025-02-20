from typing import Dict, Optional

from config.orm.configurations.base import BaseOrmConfig


class OrmManager:
    _orm_configs: Dict[str, BaseOrmConfig] = {}
    _current_orm_config: Optional[BaseOrmConfig] = None

    @classmethod
    def register_orm_config(
        cls, orm_name: str, orm_config_instance: BaseOrmConfig
    ):
        cls._orm_configs[orm_name.lower()] = orm_config_instance

    @classmethod
    def load_orm_config(cls, orm_name: str):
        cls._current_orm_config = cls._orm_configs.get(orm_name.lower(), None)
        if not cls._current_orm_config:
            raise ValueError(
                f"Configuration for orm '{orm_name}' not found. "
                f"Available configurations: {list(cls._orm_configs.keys())}"
            )

    @classmethod
    def get_orm_config(cls) -> BaseOrmConfig:
        if not cls._current_orm_config:
            raise ValueError(
                "Orm configuration has not been loaded. "
                "Call 'load_orm_config' first"
            )
        return cls._current_orm_config
