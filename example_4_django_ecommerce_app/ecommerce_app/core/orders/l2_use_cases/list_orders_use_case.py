from ecommerce_app.core.orders.l1_entities.order import Order
from ecommerce_app.core.orders.l2_use_cases.boundaries import (
    IOrderPresenter,
    IOrderRepository,
)


class ListOrdersUseCase:
    def __init__(self, order_repository: IOrderRepository, order_presenter: IOrderPresenter):
        self.order_repository = order_repository
        self.order_presenter = order_presenter

    def execute(self) -> list[Order]:
        orders = self.order_repository.list_orders()
        return self.order_presenter.present_order_list(orders)
