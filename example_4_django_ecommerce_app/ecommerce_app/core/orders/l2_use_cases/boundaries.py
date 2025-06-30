from abc import ABC, abstractmethod

from ecommerce_app.core.orders.l1_entities.order import Order


class IOrderRepository(ABC):
    @abstractmethod
    def create_order(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get_order_by_id(self, order_id: int) -> Order | None:
        pass

    @abstractmethod
    def list_orders(self) -> list[Order]:
        pass


class IOrderPresenter(ABC):
    @abstractmethod
    def present_order_list(self, orders: list[Order]) -> dict:
        pass
