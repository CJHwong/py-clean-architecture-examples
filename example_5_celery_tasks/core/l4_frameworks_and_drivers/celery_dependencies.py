import redis
from core.l2_use_cases.process_data_use_case import ProcessDataUseCase
from core.l3_interface_adapters.gateways.redis_task_repository import RedisTaskRepository

# In a real app, these would come from a config file
REDIS_URL = "redis://localhost:6379/0"

# Singleton instances for dependencies
redis_client = redis.Redis.from_url(REDIS_URL)
task_repository = RedisTaskRepository(redis_client)


def create_process_data_use_case() -> ProcessDataUseCase:
    return ProcessDataUseCase(task_repository=task_repository)
