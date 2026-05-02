from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .core.l3_interface_adapters.presenters.todo_list_presenter import TodoListPresenter
from .core.l4_frameworks_and_drivers.django_dependencies import (
    get_create_todo_use_case,
    get_list_todos_use_case,
)


class TodoListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        presenter = TodoListPresenter()
        use_case = get_list_todos_use_case(presenter)
        use_case.execute()
        return render(request, "todo_app/todo_list.html", presenter.view_model)

    def post(self, request: HttpRequest) -> HttpResponse:
        title = request.POST.get("title", "")
        if title:
            presenter = TodoListPresenter()
            use_case = get_create_todo_use_case(presenter)
            use_case.execute(title=title)
        return redirect("todo_list")
