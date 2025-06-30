from l2_use_cases.boundaries.i_user_presenter import IUserPresenter
from l2_use_cases.response_models import CreateUserResponseModel


class UserCliPresenter(IUserPresenter):
    """A concrete implementation of the Presenter (for CLI).
    - Implements the interface defined by the Use Case layer.
    - Its responsibility is to convert the pure Response Model from the Use Case
      into a format suitable for the outside world (here, the CLI).
    """

    def present(self, response: CreateUserResponseModel) -> None:
        if response.is_successful:
            print(f"✅ SUCCESS: User '{response.username}' created successfully.")
        else:
            print(f"❌ FAILURE: {response.error_message}")
