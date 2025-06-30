from abc import ABC, abstractmethod

from l1_entities.user import User


class IUserRepository(ABC):
    """Abstract interface (Gateway/Repository) defined by the Use Case.
    This is the "port" through which the Use Case layer communicates with the outside.
    """

    @abstractmethod
    def find_by_username(self, username: str) -> User | None:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
