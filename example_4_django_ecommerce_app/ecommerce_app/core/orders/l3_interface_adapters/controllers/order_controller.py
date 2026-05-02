from ecommerce_app.core.orders.l2_use_cases.create_order_use_case import (
    CreateOrderRequest,
    CreateOrderResponse,
    CreateOrderUseCase,
)
from ecommerce_app.core.orders.l2_use_cases.list_orders_use_case import (
    ListOrdersUseCase,
)


class OrderController:
    def __init__(
        self,
        create_use_case: CreateOrderUseCase,
        list_use_case: ListOrdersUseCase,
    ):
        self._create_use_case = create_use_case
        self._list_use_case = list_use_case

    def create(self, customer_id: int, product_id: int, quantity: int) -> CreateOrderResponse:
        request = CreateOrderRequest(customer_id=customer_id, product_id=product_id, quantity=quantity)
        return self._create_use_case.execute(request)

    def list_all(self) -> dict:
        return self._list_use_case.execute()
