from typing import List

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


class AppManager:
    _app_instance: FastAPI

    @classmethod
    def setup_app(cls) -> None:
        cls._app_instance = FastAPI()

    @classmethod
    def load_app(cls, app: FastAPI) -> None:
        cls._app_instance = app

    @classmethod
    def register_cors(
        cls, origins: List[str], methods: List[str], headers: List[str]
    ) -> None:
        cls._app_instance.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=methods,
            allow_headers=headers,
        )

    @classmethod
    def get_app(cls) -> FastAPI:
        if not cls._app_instance:
            raise ValueError(
                "App has not been loaded. "
                "Call 'setup_app' or 'load_app' first."
            )
        return cls._app_instance
