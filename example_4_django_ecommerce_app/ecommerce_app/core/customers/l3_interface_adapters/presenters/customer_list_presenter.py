from ecommerce_app.core.customers.l1_entities.customer import Customer
from ecommerce_app.core.customers.l2_use_cases.boundaries import ICustomerPresenter


class CustomerListPresenter(ICustomerPresenter):
    def present_customer_list(self, customers: list[Customer]) -> dict:
        return {"customers": [{"id": c.id, "name": c.name, "email": c.email} for c in customers]}
