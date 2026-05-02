from dataclasses import dataclass
from datetime import datetime


@dataclass
class Product:
    id: int | None
    name: str
    description: str
    price: float
    created_at: datetime | None

    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError("Product name cannot be empty.")
        if self.price <= 0:
            raise ValueError(f"Product price must be positive, got {self.price}.")
