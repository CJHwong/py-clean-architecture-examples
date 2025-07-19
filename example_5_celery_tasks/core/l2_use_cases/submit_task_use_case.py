from typing import Any

from core.l1_entities.task import Task
from core.l2_use_cases.boundaries.i_task_queue import ITaskQueue
from core.l2_use_cases.boundaries.i_task_repository import ITaskRepository


class SubmitTaskUseCase:
    def __init__(self, task_queue: ITaskQueue, task_repository: ITaskRepository):
        self._task_queue = task_queue
        self._task_repository = task_repository

    def execute(self, payload: dict[str, Any]) -> Task:
        task_name = "process_data_task"  # This could be dynamic
        task_id = self._task_queue.enqueue(task_name, payload)

        task = Task(
            task_id=task_id,
            status="PENDING",
            payload=payload,
        )
        self._task_repository.save(task)
        return task
