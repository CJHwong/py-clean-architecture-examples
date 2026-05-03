import uuid

from ...l1_entities.entity import Entity
from ...l2_use_cases.boundaries.i_entity_repository import IEntityRepository


class InMemoryEntityRepository(IEntityRepository):
    def __init__(self) -> None:
        self._store: dict[str, Entity] = {}

    def save(self, entity: Entity) -> Entity:
        if entity.id is None:
            entity.id = str(uuid.uuid4())
        self._store[entity.id] = entity
        return entity

    def find_by_id(self, entity_id: str) -> Entity | None:
        return self._store.get(entity_id)
