from abc import ABC, abstractmethod

from todo_app.core.l1_entities.todo_item import TodoItem


# --- Output Port (Presenter) ---
class ITodoListPresenter(ABC):
    @abstractmethod
    def present(self, todos: list[TodoItem]) -> None:
        pass


# --- Gateway Interface ---
class ITodoRepository(ABC):
    @abstractmethod
    def list_all(self) -> list[TodoItem]:
        pass

    @abstractmethod
    def save(self, todo: TodoItem) -> None:
        pass
