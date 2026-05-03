from ...l2_use_cases.boundaries.i_entity_presenter import IEntityPresenter


class EntityPresenter(IEntityPresenter):
    def present(self, data: dict) -> None:
        print(data)
