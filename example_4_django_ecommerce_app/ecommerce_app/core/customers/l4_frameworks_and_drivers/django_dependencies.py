from ecommerce_app.core.customers.l2_use_cases.boundaries import (
    ICustomerPresenter,
    ICustomerRepository,
)
from ecommerce_app.core.customers.l2_use_cases.create_customer_use_case import (
    CreateCustomerUseCase,
)
from ecommerce_app.core.customers.l2_use_cases.list_customers_use_case import (
    ListCustomersUseCase,
)
from ecommerce_app.core.customers.l3_interface_adapters.gateways.django_customer_repository import (
    DjangoCustomerRepository,
)
from ecommerce_app.core.customers.l3_interface_adapters.presenters.customer_list_presenter import (
    CustomerListPresenter,
)


def get_customer_repository() -> ICustomerRepository:
    return DjangoCustomerRepository()


def get_customer_presenter() -> ICustomerPresenter:
    return CustomerListPresenter()


def get_create_customer_use_case() -> CreateCustomerUseCase:
    return CreateCustomerUseCase(get_customer_repository(), get_customer_presenter())


def get_list_customers_use_case() -> ListCustomersUseCase:
    return ListCustomersUseCase(get_customer_repository(), get_customer_presenter())
