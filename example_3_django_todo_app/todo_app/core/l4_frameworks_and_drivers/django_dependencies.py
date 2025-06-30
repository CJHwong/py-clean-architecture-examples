from todo_app.core.l2_use_cases.create_todo_use_case import CreateTodo
from todo_app.core.l2_use_cases.list_todos_use_case import ListTodos
from todo_app.core.l3_interface_adapters.gateways.django_todo_repository import (
    DjangoTodoRepository,
)
from todo_app.core.l3_interface_adapters.presenters.todo_list_presenter import (
    TodoListPresenter,
)


def get_list_todos_use_case() -> ListTodos:
    presenter = TodoListPresenter()
    repository = DjangoTodoRepository()
    return ListTodos(repository=repository, presenter=presenter)


def get_create_todo_use_case() -> CreateTodo:
    presenter = TodoListPresenter()
    repository = DjangoTodoRepository()
    return CreateTodo(repository=repository, presenter=presenter)
