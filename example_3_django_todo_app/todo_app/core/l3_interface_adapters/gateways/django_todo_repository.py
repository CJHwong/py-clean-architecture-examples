from todo_app.core.l1_entities.todo_item import TodoItem
from todo_app.core.l2_use_cases.boundaries import ITodoRepository
from todo_app.models import TodoDjangoModel


class DjangoTodoRepository(ITodoRepository):
    def list_all(self) -> list[TodoItem]:
        django_todos = TodoDjangoModel.objects.all().order_by("-created_at")
        return [self._to_entity(django_model) for django_model in django_todos]

    def create(self, title: str) -> TodoItem:
        django_todo = TodoDjangoModel.objects.create(title=title)
        return self._to_entity(django_todo)

    def _to_entity(self, django_model: TodoDjangoModel) -> TodoItem:
        return TodoItem(
            id=django_model.id,
            title=django_model.title,
            completed=django_model.completed,
        )
