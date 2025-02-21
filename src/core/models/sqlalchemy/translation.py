from sqlalchemy import BigInteger, Column, ForeignKey, Integer
from sqlalchemy.orm import declared_attr, relationship

from core.models.sqlalchemy.base import Base


class TranslatableBase(Base):
    __abstract__ = True

    @declared_attr
    def translations(cls):
        translation_class = getattr(cls, "__translation_class__", None)

        if not translation_class:
            raise ValueError(
                "TranslatableBase must be a subclass of TranslationBase"
            )

        return relationship(
            translation_class,
            back_populates="entity",
            cascade="all, delete-orphan",
        )


class TranslationBase(Base):
    __abstract__ = True

    locale_id = Column(BigInteger, ForeignKey("locale.id", ondelete="CASCADE"))

    @declared_attr
    def locale(cls):
        return relationship("locale", back_populates="translations")

    @declared_attr
    def entity_id(cls):
        entity_class = getattr(cls, "__entity_class__", None)

        if not entity_class:
            raise ValueError(
                "TranslationBase must be a subclass of TranslatableBase"
            )

        return Column(
            Integer, ForeignKey(f"{entity_class}.id", ondelete="CASCADE")
        )

    @declared_attr
    def entity(cls):
        entity_class = getattr(cls, "__entity_class__", None)

        if not entity_class:
            raise ValueError(
                "TranslationBase must be a subclass of TranslatableBase"
            )

        return relationship(entity_class, back_populates="translations")
