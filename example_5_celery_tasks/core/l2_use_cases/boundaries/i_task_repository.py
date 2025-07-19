from abc import ABC, abstractmethod

from core.l1_entities.task import Task


class ITaskRepository(ABC):
    @abstractmethod
    def get_by_id(self, task_id: str) -> Task | None: ...

    @abstractmethod
    def save(self, task: Task) -> None: ...
