from sqlalchemy import BigInteger, Column, String

from core.models.sqlalchemy.translation import TranslationBase


class BlogTranslation(TranslationBase):
    __tablename__ = "blog_translation"
    __entity_class__ = "blog"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    name = Column(String(400), nullable=False)
    description = Column(String(1000), nullable=True)
    content = Column(String(5000), nullable=True)
