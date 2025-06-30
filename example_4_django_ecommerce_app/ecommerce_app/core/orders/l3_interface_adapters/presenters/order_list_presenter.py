from ecommerce_app.core.orders.l1_entities.order import Order
from ecommerce_app.core.orders.l2_use_cases.boundaries import IOrderPresenter


class OrderListPresenter(IOrderPresenter):
    def present_order_list(self, orders: list[Order]) -> dict:
        return {
            "orders": [
                {
                    "id": o.id,
                    "customer_id": o.customer_id,
                    "product_id": o.product_id,
                    "quantity": o.quantity,
                }
                for o in orders
            ],
        }
