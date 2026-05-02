from todo_app.core.l2_use_cases.create_todo_use_case import CreateTodoUseCase
from todo_app.core.l2_use_cases.list_todos_use_case import ListTodosUseCase

from ..l3_interface_adapters.gateways.in_memory_todo_repository import (
    InMemoryTodoRepository,
)
from ..l3_interface_adapters.presenters.todo_json_presenter import TodoJsonPresenter

# Singleton repository to maintain state across requests
repository = InMemoryTodoRepository()


def get_list_todos_use_case() -> ListTodosUseCase:
    return ListTodosUseCase(repository=repository, presenter=TodoJsonPresenter())


def get_create_todo_use_case() -> CreateTodoUseCase:
    return CreateTodoUseCase(repository=repository, presenter=TodoJsonPresenter())
