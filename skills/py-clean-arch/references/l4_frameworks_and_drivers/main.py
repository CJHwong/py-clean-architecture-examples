from ..l2_use_cases.action_entity_use_case import ActionEntityUseCase
from ..l3_interface_adapters.controllers.entity_controller import EntityController
from ..l3_interface_adapters.gateways.in_memory_entity_repository import (
    InMemoryEntityRepository,
)
from ..l3_interface_adapters.presenters.entity_presenter import EntityPresenter


def create_controller() -> EntityController:
    repository = InMemoryEntityRepository()
    presenter = EntityPresenter()
    use_case = ActionEntityUseCase(repository, presenter)
    return EntityController(use_case)
