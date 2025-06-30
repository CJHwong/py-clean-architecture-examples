from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    id: int | None
    customer_id: int
    product_id: int
    quantity: int
    order_date: datetime | None
