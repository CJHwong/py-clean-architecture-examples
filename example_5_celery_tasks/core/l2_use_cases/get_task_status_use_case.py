from core.l1_entities.task import Task
from core.l2_use_cases.boundaries.i_task_repository import ITaskRepository


class GetTaskStatusUseCase:
    def __init__(self, task_repository: ITaskRepository):
        self._task_repository = task_repository

    def execute(self, task_id: str) -> Task | None:
        return self._task_repository.get_by_id(task_id)
