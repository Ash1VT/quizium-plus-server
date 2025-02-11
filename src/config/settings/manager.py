from typing import Dict, Type

from config.settings.configurations.base import BaseSettings


class SettingsManager:
    """Manages application settings dynamically."""

    _settings_classes: Dict[str, Type[BaseSettings]] = {}
    _current_settings: BaseSettings

    @classmethod
    def register_config(
        cls, name: str, config_class: Type[BaseSettings]
    ) -> None:
        """Registers a new configuration class dynamically."""

        cls._settings_classes[name.lower()] = config_class

    @classmethod
    def load_settings(
        cls,
        configuration: str = "development",
        env_file: str = ".env",
        env_file_encoding: str = "utf-8",
    ) -> None:
        """Loads the settings based on the provided configuration name."""

        settings_class = cls._settings_classes.get(configuration.lower(), None)

        if not settings_class:
            raise ValueError(
                f"Settings '{configuration}' not found. "
                f"Available settings: {list(cls._settings_classes.keys())}"
            )

        cls._current_settings = settings_class(
            _env_file=env_file, _env_file_encoding=env_file_encoding
        )

    @classmethod
    def get_settings(cls) -> BaseSettings:
        """Returns the loaded settings instance."""

        if not hasattr(cls, "_current_settings"):
            raise ValueError(
                "Settings have not been loaded. Call 'load_settings' first."
            )

        return cls._current_settings
