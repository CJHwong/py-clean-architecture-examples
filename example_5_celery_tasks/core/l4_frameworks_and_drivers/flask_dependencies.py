import redis
from celery_config import app as celery_app
from core.l2_use_cases.get_task_status_use_case import GetTaskStatusUseCase
from core.l2_use_cases.submit_task_use_case import SubmitTaskUseCase
from core.l3_interface_adapters.gateways.celery_task_queue import CeleryTaskQueue
from core.l3_interface_adapters.gateways.redis_task_repository import RedisTaskRepository

# In a real app, these would come from a config file
REDIS_URL = "redis://localhost:6379/0"

# Singleton instances for dependencies
redis_client = redis.Redis.from_url(REDIS_URL)
task_repository = RedisTaskRepository(redis_client)
task_queue = CeleryTaskQueue(celery_app)


def create_submit_task_use_case() -> SubmitTaskUseCase:
    return SubmitTaskUseCase(task_queue=task_queue, task_repository=task_repository)


def create_get_task_status_use_case() -> GetTaskStatusUseCase:
    return GetTaskStatusUseCase(task_repository=task_repository)
