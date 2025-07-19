from typing import Any

from core.l1_entities.task import Task


class TaskPresenter:
    @staticmethod
    def to_dict(task: Task) -> dict[str, Any]:
        return {
            "task_id": task.task_id,
            "status": task.status,
            "payload": task.payload,
            "result": task.result,
        }
