from abc import ABC, abstractmethod

from ...l1_entities.entity import Entity


class IEntityRepository(ABC):
    @abstractmethod
    def save(self, entity: Entity) -> Entity: ...

    @abstractmethod
    def find_by_id(self, entity_id: str) -> Entity | None: ...
