from abc import ABC, abstractmethod
from typing import Any

from todo_app.core.l1_entities.todo_item import TodoItem


class ListTodosUseCase(ABC):
    @abstractmethod
    def execute(self) -> Any:
        pass


class CreateTodoUseCase(ABC):
    @abstractmethod
    def execute(self, title: str) -> Any:
        pass


class ITodoListPresenter(ABC):
    @abstractmethod
    def present(self, todos: list[TodoItem]) -> Any:
        pass


class ITodoRepository(ABC):
    @abstractmethod
    def list_all(self) -> list[TodoItem]:
        pass

    @abstractmethod
    def create(self, title: str) -> TodoItem:
        pass
