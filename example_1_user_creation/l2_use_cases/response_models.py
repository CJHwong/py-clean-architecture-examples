from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUserResponseModel:
    """Data structure output from the Use Case."""

    username: str
    is_successful: bool
    error_message: str = ""
