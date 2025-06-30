from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUserRequestModel:
    """Data structure for input to the Use Case."""

    username: str
    password: str
