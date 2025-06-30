from fastapi import Depends, FastAPI, Form

from .todo_app.core.l2_use_cases.create_todo_use_case import CreateTodoUseCase
from .todo_app.core.l2_use_cases.list_todos_use_case import ListTodosUseCase
from .todo_app.core.l4_frameworks_and_drivers.dependencies import (
    get_create_todo_use_case,
    get_list_todos_use_case,
)
from .todo_app.core.l4_frameworks_and_drivers.view_models import TodoViewModel

app = FastAPI(title="Clean Architecture To-Do API")


@app.get("/todos/", response_model=list[TodoViewModel], tags=["To-Do"])
def list_todos(
    use_case: ListTodosUseCase = Depends(get_list_todos_use_case),  # noqa: B008
):
    """API endpoint to list all To-Do items.
    The response model ensures the output matches our defined schema.
    """
    return use_case.execute()


@app.post("/todos/", response_model=list[TodoViewModel], tags=["To-Do"])
def create_todo(
    title: str = Form(...),  # Using Form for standard HTML form posts
    use_case: CreateTodoUseCase = Depends(get_create_todo_use_case),  # noqa: B008
):
    """API endpoint to create a new To-Do item."""
    return use_case.execute(title)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
