import time
from typing import Any

from core.l2_use_cases.boundaries.i_task_repository import ITaskRepository


class ProcessDataUseCase:
    def __init__(self, task_repository: ITaskRepository):
        self._task_repository = task_repository

    def execute(self, task_id: str, payload: dict[str, Any]) -> str:
        # Simulate a long-running task
        print(f"Processing data for task {task_id}: {payload}")
        time.sleep(5)
        result = f"Processed data: {payload.get('data', '')}"
        print(f"Processing finished for task {task_id}")

        # Update the task status in the repository
        task = self._task_repository.get_by_id(task_id)
        if task:
            task.status = "SUCCESS"
            task.result = result
            self._task_repository.save(task)

        return result
