from l1_entities.user import User
from l2_use_cases.boundaries.i_user_presenter import IUserPresenter
from l2_use_cases.boundaries.i_user_repository import IUserRepository
from l2_use_cases.request_models import CreateUserRequestModel
from l2_use_cases.response_models import CreateUserResponseModel


class CreateUserUseCase:
    """Use Case:
    - This is the application-specific business rule.
    - It coordinates Entities to get the job done.
    - Its dependencies only point inward (Entities) or to boundary interfaces at the same layer.
    - It knows nothing about the Controller, Presenter, or DB implementations.
    """

    def __init__(self, user_repository: IUserRepository, presenter: IUserPresenter):
        self.user_repository = user_repository
        self.presenter = presenter

    def execute(self, request: CreateUserRequestModel) -> None:
        # 1. Application business rule: check if user already exists
        if self.user_repository.find_by_username(request.username):
            response = CreateUserResponseModel(
                username=request.username,
                is_successful=False,
                error_message=f"User '{request.username}' already exists.",
            )
            self.presenter.present(response)
            return

        # 2. Call Entity to perform core business rule (e.g., validation)
        try:
            user = User(username=request.username, password=request.password)
        except ValueError as e:
            response = CreateUserResponseModel(username=request.username, is_successful=False, error_message=str(e))
            self.presenter.present(response)
            return

        # 3. Save entity through Gateway
        self.user_repository.save(user)

        # 4. Output result through Presenter
        response = CreateUserResponseModel(username=user.username, is_successful=True)
        self.presenter.present(response)
