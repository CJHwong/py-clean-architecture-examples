from ...l2_use_cases.action_entity_use_case import ActionEntityUseCase


class EntityController:
    def __init__(self, use_case: ActionEntityUseCase) -> None:
        self._use_case = use_case

    def handle(self) -> None:
        self._use_case.execute()
