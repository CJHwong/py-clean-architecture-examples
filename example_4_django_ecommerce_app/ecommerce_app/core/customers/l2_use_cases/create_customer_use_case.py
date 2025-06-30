from dataclasses import dataclass

from ecommerce_app.core.customers.l1_entities.customer import Customer
from ecommerce_app.core.customers.l2_use_cases.boundaries import (
    ICustomerPresenter,
    ICustomerRepository,
)


@dataclass
class CreateCustomerRequest:
    name: str
    email: str


@dataclass
class CreateCustomerResponse:
    customer_id: int
    name: str
    email: str


class CreateCustomerUseCase:
    def __init__(
        self,
        customer_repository: ICustomerRepository,
        customer_presenter: ICustomerPresenter,
    ):
        self.customer_repository = customer_repository
        self.customer_presenter = customer_presenter

    def execute(self, request: CreateCustomerRequest) -> CreateCustomerResponse:
        customer = Customer(id=None, name=request.name, email=request.email, created_at=None)
        created_customer = self.customer_repository.create_customer(customer)
        return CreateCustomerResponse(
            customer_id=created_customer.id,
            name=created_customer.name,
            email=created_customer.email,
        )
