from abc import ABC, abstractmethod

from l2_use_cases.response_models import CreateUserResponseModel


class IUserPresenter(ABC):
    """Abstract output interface (Presenter) defined by the Use Case.
    The Use Case passes results through this interface, without knowing who is on the other end.
    """

    @abstractmethod
    def present(self, response: CreateUserResponseModel) -> None:
        pass
