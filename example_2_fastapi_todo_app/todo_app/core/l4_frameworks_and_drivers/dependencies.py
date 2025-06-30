from todo_app.core.l2_use_cases.create_todo_use_case import CreateTodo
from todo_app.core.l2_use_cases.list_todos_use_case import ListTodos

from ..l3_interface_adapters.gateways.in_memory_todo_repository import (
    InMemoryTodoRepository,
)
from ..l3_interface_adapters.presenters.todo_json_presenter import TodoJsonPresenter

# Use a singleton pattern for the repository to maintain state across requests
repository = InMemoryTodoRepository()


def get_list_todos_use_case() -> ListTodos:
    """Dependency Provider for the ListTodos use case."""
    presenter = TodoJsonPresenter()
    # Note: We reuse the singleton repository instance
    return ListTodos(repository=repository, presenter=presenter)


def get_create_todo_use_case() -> CreateTodo:
    """Dependency Provider for the CreateTodo use case."""
    presenter = TodoJsonPresenter()
    # Note: We reuse the singleton repository instance
    return CreateTodo(repository=repository, presenter=presenter)
