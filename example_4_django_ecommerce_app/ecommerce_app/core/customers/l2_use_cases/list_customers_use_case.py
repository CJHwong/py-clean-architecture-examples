from ecommerce_app.core.customers.l1_entities.customer import Customer
from ecommerce_app.core.customers.l2_use_cases.boundaries import (
    ICustomerPresenter,
    ICustomerRepository,
)


class ListCustomersUseCase:
    def __init__(
        self,
        customer_repository: ICustomerRepository,
        customer_presenter: ICustomerPresenter,
    ):
        self.customer_repository = customer_repository
        self.customer_presenter = customer_presenter

    def execute(self) -> list[Customer]:
        customers = self.customer_repository.list_customers()
        return self.customer_presenter.present_customer_list(customers)
