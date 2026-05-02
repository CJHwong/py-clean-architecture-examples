from todo_app.core.l2_use_cases.boundaries import ITodoListPresenter
from todo_app.core.l2_use_cases.create_todo_use_case import CreateTodoUseCase
from todo_app.core.l2_use_cases.list_todos_use_case import ListTodosUseCase
from todo_app.core.l3_interface_adapters.gateways.django_todo_repository import (
    DjangoTodoRepository,
)


def get_list_todos_use_case(presenter: ITodoListPresenter) -> ListTodosUseCase:
    return ListTodosUseCase(repository=DjangoTodoRepository(), presenter=presenter)


def get_create_todo_use_case(presenter: ITodoListPresenter) -> CreateTodoUseCase:
    return CreateTodoUseCase(repository=DjangoTodoRepository(), presenter=presenter)
