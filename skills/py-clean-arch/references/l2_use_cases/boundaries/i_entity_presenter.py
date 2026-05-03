from abc import ABC, abstractmethod


class IEntityPresenter(ABC):
    @abstractmethod
    def present(self, data: dict) -> None: ...
