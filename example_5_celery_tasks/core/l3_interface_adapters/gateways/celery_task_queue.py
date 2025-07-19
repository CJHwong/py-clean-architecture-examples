from typing import Any

from celery import Celery
from core.l2_use_cases.boundaries.i_task_queue import ITaskQueue


class CeleryTaskQueue(ITaskQueue):
    def __init__(self, celery_app: Celery):
        self._celery_app = celery_app

    def enqueue(self, task_name: str, payload: dict[str, Any]) -> str:
        task = self._celery_app.send_task(
            task_name,
            args=[payload],
        )
        return task.id
