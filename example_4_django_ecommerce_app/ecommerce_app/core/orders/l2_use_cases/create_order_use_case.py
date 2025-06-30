from dataclasses import dataclass

from ecommerce_app.core.orders.l1_entities.order import Order
from ecommerce_app.core.orders.l2_use_cases.boundaries import (
    IOrderPresenter,
    IOrderRepository,
)


@dataclass
class CreateOrderRequest:
    customer_id: int
    product_id: int
    quantity: int


@dataclass
class CreateOrderResponse:
    order_id: int
    customer_id: int
    product_id: int
    quantity: int


class CreateOrderUseCase:
    def __init__(self, order_repository: IOrderRepository, order_presenter: IOrderPresenter):
        self.order_repository = order_repository
        self.order_presenter = order_presenter

    def execute(self, request: CreateOrderRequest) -> CreateOrderResponse:
        order = Order(
            id=None,
            customer_id=request.customer_id,
            product_id=request.product_id,
            quantity=request.quantity,
            order_date=None,
        )
        created_order = self.order_repository.create_order(order)
        return CreateOrderResponse(
            order_id=created_order.id,
            customer_id=created_order.customer_id,
            product_id=created_order.product_id,
            quantity=created_order.quantity,
        )
