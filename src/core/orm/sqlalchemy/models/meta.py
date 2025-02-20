from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeMeta, relationship


class TranslatableMeta(DeclarativeMeta):
    def __new__(mcs, name, bases, dct):
        cls = super().__new__(mcs, name, bases, dct)

        if getattr(cls, "__abstract__", False):
            return cls

        translation_class = getattr(cls, "__translation_class__", None)
        if translation_class:
            cls.translations = relationship(
                translation_class,
                back_populates="entity",
                cascade="all, delete-orphan",
            )

        return cls


class TranslationMeta(DeclarativeMeta):
    def __new__(mcs, name, bases, dct):
        cls = super().__new__(mcs, name, bases, dct)

        if getattr(cls, "__abstract__", False):
            return cls

        parent_class = getattr(cls, "__parent_class__", None)
        if parent_class:
            cls.entity = relationship(
                parent_class, back_populates="translations"
            )
            cls.entity_id = Column(
                Integer,
                ForeignKey(
                    f"{parent_class.__tablename__}.id", ondelete="CASCADE"
                ),
            )

        return cls
