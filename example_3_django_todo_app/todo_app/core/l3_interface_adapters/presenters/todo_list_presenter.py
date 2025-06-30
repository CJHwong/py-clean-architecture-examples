from typing import Any

from todo_app.core.l1_entities.todo_item import TodoItem
from todo_app.core.l2_use_cases.boundaries import ITodoListPresenter


class TodoListPresenter(ITodoListPresenter):
    def __init__(self):
        self.view_model = {}

    def present(self, todos: list[TodoItem]) -> None:
        self.view_model = {"todos": [self._todo_to_dict(todo) for todo in todos]}

    def _todo_to_dict(self, todo: TodoItem) -> dict[str, Any]:
        return {"id": str(todo.id), "title": todo.title, "completed": todo.completed}
