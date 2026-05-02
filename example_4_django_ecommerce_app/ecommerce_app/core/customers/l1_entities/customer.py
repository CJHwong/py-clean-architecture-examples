import re
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Customer:
    id: int | None
    name: str
    email: str
    created_at: datetime | None

    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError("Customer name cannot be empty.")
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", self.email):
            raise ValueError(f"Invalid email address: {self.email}")
