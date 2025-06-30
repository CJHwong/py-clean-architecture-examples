from typing import Any

from todo_app.core.l1_entities.todo_item import TodoItem
from todo_app.core.l2_use_cases.boundaries import ITodoListPresenter


class TodoJsonPresenter(ITodoListPresenter):
    """Presenter Implementation: Prepares a list of dictionaries,
    which FastAPI will automatically convert to a JSON response.
    """

    def present(self, todos: list[TodoItem]) -> list[dict[str, Any]]:
        return [{"id": str(todo.id), "title": todo.title, "completed": todo.completed} for todo in todos]
