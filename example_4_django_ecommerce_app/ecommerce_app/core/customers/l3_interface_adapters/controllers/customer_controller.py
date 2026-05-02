from ecommerce_app.core.customers.l2_use_cases.create_customer_use_case import (
    CreateCustomerRequest,
    CreateCustomerResponse,
    CreateCustomerUseCase,
)
from ecommerce_app.core.customers.l2_use_cases.list_customers_use_case import (
    ListCustomersUseCase,
)


class CustomerController:
    def __init__(
        self,
        create_use_case: CreateCustomerUseCase,
        list_use_case: ListCustomersUseCase,
    ):
        self._create_use_case = create_use_case
        self._list_use_case = list_use_case

    def create(self, name: str, email: str) -> CreateCustomerResponse:
        request = CreateCustomerRequest(name=name, email=email)
        return self._create_use_case.execute(request)

    def list_all(self) -> dict:
        return self._list_use_case.execute()
