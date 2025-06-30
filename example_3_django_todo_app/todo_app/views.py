from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .core.l4_frameworks_and_drivers.django_dependencies import (
    get_create_todo_use_case,
    get_list_todos_use_case,
)


class TodoListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        list_todos_use_case = get_list_todos_use_case()
        list_todos_use_case.execute()
        presenter = list_todos_use_case.presenter
        context = presenter.view_model
        return render(request, "todo_app/todo_list.html", context)

    def post(self, request: HttpRequest) -> HttpResponse:
        create_todo_use_case = get_create_todo_use_case()
        title = request.POST.get("title", "")
        if title:
            create_todo_use_case.execute(title=title)
        return redirect("todo_list")
