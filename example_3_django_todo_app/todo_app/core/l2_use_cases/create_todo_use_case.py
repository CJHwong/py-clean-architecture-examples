from .boundaries import CreateTodoUseCase, ITodoListPresenter, ITodoRepository


class CreateTodo(CreateTodoUseCase):
    def __init__(self, repository: ITodoRepository, presenter: ITodoListPresenter):
        self.repository = repository
        self.presenter = presenter

    def execute(self, title: str) -> None:
        self.repository.create(title)
        all_todos = self.repository.list_all()
        self.presenter.present(all_todos)
