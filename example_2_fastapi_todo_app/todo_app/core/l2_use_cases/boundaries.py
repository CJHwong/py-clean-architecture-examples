from abc import ABC, abstractmethod
from typing import Any

from todo_app.core.l1_entities.todo_item import TodoItem


class ITodoListPresenter(ABC):
    @abstractmethod
    def present(self, todos: list[TodoItem]) -> Any:
        pass


class ITodoRepository(ABC):
    @abstractmethod
    def list_all(self) -> list[TodoItem]:
        pass

    @abstractmethod
    def save(self, todo: TodoItem) -> None:
        pass
