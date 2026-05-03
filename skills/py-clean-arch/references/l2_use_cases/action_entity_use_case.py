from ..l1_entities.entity import Entity
from .boundaries.i_entity_presenter import IEntityPresenter
from .boundaries.i_entity_repository import IEntityRepository


class ActionEntityUseCase:
    def __init__(
        self,
        repository: IEntityRepository,
        presenter: IEntityPresenter,
    ) -> None:
        self._repository = repository
        self._presenter = presenter

    def execute(self) -> None:
        entity = Entity()
        saved = self._repository.save(entity)
        self._presenter.present({"id": saved.id})
