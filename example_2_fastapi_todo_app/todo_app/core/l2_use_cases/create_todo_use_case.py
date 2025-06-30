from typing import Any

from .boundaries import CreateTodoUseCase, ITodoListPresenter, ITodoRepository


class CreateTodo(CreateTodoUseCase):
    def __init__(self, repository: ITodoRepository, presenter: ITodoListPresenter):
        self.repository = repository
        self.presenter = presenter

    def execute(self, title: str) -> Any:
        self.repository.create(title)
        # Present the entire updated list after creation
        all_todos = self.repository.list_all()
        return self.presenter.present(all_todos)
