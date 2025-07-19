import json

import redis
from core.l1_entities.task import Task
from core.l2_use_cases.boundaries.i_task_repository import ITaskRepository


class RedisTaskRepository(ITaskRepository):
    def __init__(self, redis_client: redis.Redis):
        self._redis_client = redis_client

    def get_by_id(self, task_id: str) -> Task | None:
        task_data = self._redis_client.get(task_id)
        if task_data:
            task_dict = json.loads(task_data)
            return Task(**task_dict)
        return None

    def save(self, task: Task) -> None:
        task_dict = {
            "task_id": task.task_id,
            "status": task.status,
            "payload": task.payload,
            "result": task.result,
        }
        self._redis_client.set(task.task_id, json.dumps(task_dict))
