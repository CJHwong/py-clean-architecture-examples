import uuid

from pydantic import BaseModel, RootModel


class TodoViewModel(BaseModel):
    """The JSON response model for a single To-Do item."""

    id: uuid.UUID
    title: str
    completed: bool

    class Config:
        from_attributes = True  # Renamed from orm_mode in Pydantic v2


# Pydantic V2 uses RootModel for models that are just a list or dict at the root
class TodoListViewModel(RootModel[list[TodoViewModel]]):
    """The JSON response model for a list of To-Do items."""

    pass
