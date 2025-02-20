from sqlalchemy import BigInteger, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from core.orm.sqlalchemy.models.base import Base
from core.orm.sqlalchemy.models.meta import TranslatableMeta, TranslationMeta


class Locale(Base):
    locale = Column(String(10), nullable=False)


class TranslatableBase(Base, metaclass=TranslatableMeta):
    __abstract__ = True


class TranslationBase(Base, metaclass=TranslationMeta):
    __abstract__ = True

    locale_id = Column(BigInteger, ForeignKey("Locale.id"), nullable=False)

    locale = relationship("Locale")
