from ecommerce_app.core.orders.l2_use_cases.boundaries import (
    IOrderPresenter,
    IOrderRepository,
)
from ecommerce_app.core.orders.l2_use_cases.create_order_use_case import (
    CreateOrderUseCase,
)
from ecommerce_app.core.orders.l2_use_cases.list_orders_use_case import (
    ListOrdersUseCase,
)
from ecommerce_app.core.orders.l3_interface_adapters.gateways.django_order_repository import (
    DjangoOrderRepository,
)
from ecommerce_app.core.orders.l3_interface_adapters.presenters.order_list_presenter import (
    OrderListPresenter,
)


def get_order_repository() -> IOrderRepository:
    return DjangoOrderRepository()


def get_order_presenter() -> IOrderPresenter:
    return OrderListPresenter()


def get_create_order_use_case() -> CreateOrderUseCase:
    return CreateOrderUseCase(get_order_repository(), get_order_presenter())


def get_list_orders_use_case() -> ListOrdersUseCase:
    return ListOrdersUseCase(get_order_repository(), get_order_presenter())
