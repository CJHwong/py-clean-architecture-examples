from l1_entities.user import User
from l2_use_cases.boundaries.i_user_repository import IUserRepository


class InMemoryUserRepository(IUserRepository):
    """A concrete implementation of the Gateway (in-memory storage).
    - Its responsibility is to implement the interface defined by the Use Case layer.
    - This is key to decoupling database details from core business logic.
    """

    def __init__(self):
        self._users: dict[str, User] = {}

    def find_by_username(self, username: str) -> User | None:
        return self._users.get(username)

    def save(self, user: User) -> None:
        self._users[user.username] = user
        print(f"Gateway: User '{user.username}' saved in memory.")
