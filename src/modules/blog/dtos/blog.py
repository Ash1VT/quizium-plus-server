from dataclasses import dataclass
from typing import Optional


@dataclass
class Blog:
    id: int
    slug: str
    locale: str
    name: str
    description: Optional[str]
    content: Optional[str]
    image_url: str
