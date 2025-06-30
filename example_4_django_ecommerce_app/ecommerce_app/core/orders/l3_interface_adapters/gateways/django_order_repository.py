from ecommerce_app.core.orders.l1_entities.order import Order
from ecommerce_app.core.orders.l2_use_cases.boundaries import IOrderRepository
from ecommerce_app.models import (
    Customer as DjangoCustomer,
)
from ecommerce_app.models import (
    Order as DjangoOrder,
)
from ecommerce_app.models import (
    Product as DjangoProduct,
)


class DjangoOrderRepository(IOrderRepository):
    def create_order(self, order: Order) -> Order:
        django_customer = DjangoCustomer.objects.get(id=order.customer_id)
        django_product = DjangoProduct.objects.get(id=order.product_id)
        django_order = DjangoOrder.objects.create(
            customer=django_customer,
            product=django_product,
            quantity=order.quantity,
        )
        return Order(
            id=django_order.id,
            customer_id=django_order.customer.id,
            product_id=django_order.product.id,
            quantity=django_order.quantity,
            order_date=django_order.order_date,
        )

    def get_order_by_id(self, order_id: int) -> Order | None:
        try:
            django_order = DjangoOrder.objects.get(id=order_id)
            return Order(
                id=django_order.id,
                customer_id=django_order.customer.id,
                product_id=django_order.product.id,
                quantity=django_order.quantity,
                order_date=django_order.order_date,
            )
        except DjangoOrder.DoesNotExist:
            return None

    def list_orders(self) -> list[Order]:
        django_orders = DjangoOrder.objects.all()
        return [
            Order(
                id=o.id,
                customer_id=o.customer.id,
                product_id=o.product.id,
                quantity=o.quantity,
                order_date=o.order_date,
            )
            for o in django_orders
        ]
