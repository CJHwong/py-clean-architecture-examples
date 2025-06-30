import sys

from l2_use_cases.create_user_use_case import CreateUserUseCase
from l3_interface_adapters.controllers.user_cli_controller import UserCliController
from l3_interface_adapters.gateways.in_memory_user_repository import (
    InMemoryUserRepository,
)
from l3_interface_adapters.presenters.user_cli_presenter import UserCliPresenter


def main():
    print("--- System Startup: Assembling components ---")
    user_repo = InMemoryUserRepository()
    presenter = UserCliPresenter()
    create_user_use_case = CreateUserUseCase(user_repository=user_repo, presenter=presenter)
    controller = UserCliController(use_case=create_user_use_case)
    print("--- Assembly complete. Handing control to Controller ---\n")
    controller.create_user(sys.argv[1:])
