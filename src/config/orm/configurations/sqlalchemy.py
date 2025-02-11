from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config.orm.configurations.base import BaseOrmConfig
from core.uow.generic import GenericUnitOfWork
from core.uow.sqlalchemy import SqlAlchemyUnitOfWork


class AsyncSqlAlchemyOrmConfig(BaseOrmConfig):
    def __init__(
        self, database_url: str, expire_session_on_commit: bool = False
    ):
        super().__init__(database_url)
        self._expire_session_on_commit = expire_session_on_commit
        self._init_engine()
        self._init_session_maker()

    def get_uow(self) -> GenericUnitOfWork:
        return SqlAlchemyUnitOfWork(self._async_session_maker)

    def _init_engine(self):
        self._async_engine = create_async_engine(
            self._database_url, poolclass=NullPool
        )

    def _init_session_maker(self):
        if self._async_engine is None:
            raise ValueError(
                "Async engine has not been initialized. "
                "Call '_init_engine' first"
            )

        self._async_session_maker = async_sessionmaker(
            bind=self._async_engine,
            expire_on_commit=self._expire_session_on_commit,
        )
