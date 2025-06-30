from l2_use_cases.create_user_use_case import CreateUserUseCase
from l2_use_cases.request_models import CreateUserRequestModel


class UserCliController:
    """Controller:
    - Belongs to the interface adapters layer.
    - Its responsibility is to receive raw input from the outside world (here, CLI).
    - Converts raw input into a Request Model for the Use Case.
    - Calls the Use Case to execute business logic.
    """

    def __init__(self, use_case: CreateUserUseCase):
        self.use_case = use_case

    def create_user(self, args: list) -> None:
        try:
            username = args[0]
            password = args[1]
        except IndexError:
            print("Usage: python main.py <username> <password>")
            return

        request = CreateUserRequestModel(username=username, password=password)
        self.use_case.execute(request)
