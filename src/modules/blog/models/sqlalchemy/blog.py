from sqlalchemy import BigInteger, Column, String

from core.models.sqlalchemy.base import TimestampMixin
from core.models.sqlalchemy.translation import TranslatableBase


class Blog(TranslatableBase, TimestampMixin):
    __tablename__ = "blog"
    __translation_class__ = "blog_translation"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    slug = Column(String(200), nullable=False, unique=True, index=True)
    image_url = Column(String(300), nullable=True)
