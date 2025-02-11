from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from core.uow.generic import GenericUnitOfWork


class SqlAlchemyUnitOfWork(GenericUnitOfWork):
    """
    Unit of work context manager for SQLAlchemy.

    This class provides a context manager for managing
    transactions with SQLAlchemy. It initializes the
    necessary repositories and session for database operations.
    It should be used in conjunction with the
    `uow_transaction` or `uow_transaction_with_commit` context managers.
    """

    def __init__(self, session_factory: Callable[[], AsyncSession]):
        self._session_factory = session_factory
        super().__init__()

    # def _init_repositories(self, session: AsyncSession):
    #     pass

    async def __aenter__(self):
        self._session = self._session_factory()
        # self._init_repositories(self._session)
        return await super().__aenter__()

    async def __aexit__(self, *args):
        await super().__aexit__(*args)
        await self._session.close()

    async def commit(self):
        """
        Commit the transaction.
        """

        await self._session.commit()

    async def rollback(self):
        """
        Rollback the transaction.
        """

        await self._session.rollback()
