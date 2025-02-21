from dataclasses import dataclass
from typing import Optional


@dataclass
class BlogTranslation:
    id: int
    name: str
    description: Optional[str]
    content: Optional[str]
