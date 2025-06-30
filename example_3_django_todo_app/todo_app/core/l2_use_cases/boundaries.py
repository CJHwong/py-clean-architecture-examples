from abc import ABC, abstractmethod

from todo_app.core.l1_entities.todo_item import TodoItem


# --- Input Ports ---
class ListTodosUseCase(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class CreateTodoUseCase(ABC):
    @abstractmethod
    def execute(self, title: str) -> None:
        pass


# --- Output Port (Presenter) ---
class ITodoListPresenter(ABC):
    view_model: dict

    @abstractmethod
    def present(self, todos: list[TodoItem]) -> None:
        pass


# --- Gateway Interface ---
class ITodoRepository(ABC):
    @abstractmethod
    def list_all(self) -> list[TodoItem]:
        pass

    @abstractmethod
    def create(self, title: str) -> TodoItem:
        pass
