from dataclasses import dataclass
from datetime import datetime


@dataclass
class Product:
    id: int | None
    name: str
    description: str
    price: float
    created_at: datetime | None
