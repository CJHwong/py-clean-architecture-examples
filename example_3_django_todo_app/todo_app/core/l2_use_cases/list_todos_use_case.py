from .boundaries import ITodoListPresenter, ITodoRepository


class ListTodosUseCase:
    def __init__(self, repository: ITodoRepository, presenter: ITodoListPresenter):
        self.repository = repository
        self.presenter = presenter

    def execute(self) -> None:
        all_todos = self.repository.list_all()
        self.presenter.present(all_todos)
