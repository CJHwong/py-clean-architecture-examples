import uuid
from typing import Any

from todo_app.core.l1_entities.todo_item import TodoItem

from .boundaries import ITodoListPresenter, ITodoRepository


class CreateTodoUseCase:
    def __init__(self, repository: ITodoRepository, presenter: ITodoListPresenter):
        self.repository = repository
        self.presenter = presenter

    def execute(self, title: str) -> Any:
        todo = TodoItem(id=uuid.uuid4(), title=title, completed=False)
        self.repository.save(todo)
        all_todos = self.repository.list_all()
        return self.presenter.present(all_todos)
