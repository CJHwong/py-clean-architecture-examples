import uuid

from todo_app.core.l1_entities.todo_item import TodoItem
from todo_app.core.l2_use_cases.boundaries import ITodoRepository


class InMemoryTodoRepository(ITodoRepository):
    """Gateway Implementation using a simple in-memory dictionary."""

    def __init__(self):
        self._todos: dict[uuid.UUID, TodoItem] = {}

    def list_all(self) -> list[TodoItem]:
        return sorted(list(self._todos.values()), key=lambda todo: todo.title)

    def save(self, todo: TodoItem) -> None:
        self._todos[todo.id] = todo
