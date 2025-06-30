import uuid
from dataclasses import dataclass


@dataclass
class TodoItem:
    """Entity: Core business object"""

    id: uuid.UUID
    title: str
    completed: bool

    def __post_init__(self):
        if not self.title:
            raise ValueError("Title cannot be empty.")
