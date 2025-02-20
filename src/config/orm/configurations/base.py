from abc import ABC, abstractmethod

from core.uow.generic import GenericUnitOfWork


class BaseOrmConfig(ABC):
    def __init__(self, database_url: str):
        self._database_url = database_url

    @abstractmethod
    def get_uow(self) -> GenericUnitOfWork:
        raise NotImplementedError
