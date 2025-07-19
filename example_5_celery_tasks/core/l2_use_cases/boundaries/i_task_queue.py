from abc import ABC, abstractmethod
from typing import Any


class ITaskQueue(ABC):
    @abstractmethod
    def enqueue(self, task_name: str, payload: dict[str, Any]) -> str: ...
