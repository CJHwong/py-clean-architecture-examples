from typing import Any

from .boundaries import ITodoListPresenter, ITodoRepository, ListTodosUseCase


class ListTodos(ListTodosUseCase):
    def __init__(self, repository: ITodoRepository, presenter: ITodoListPresenter):
        self.repository = repository
        self.presenter = presenter

    def execute(self) -> Any:
        all_todos = self.repository.list_all()
        return self.presenter.present(all_todos)
