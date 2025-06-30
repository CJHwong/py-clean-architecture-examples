from abc import ABC, abstractmethod

from ecommerce_app.core.customers.l1_entities.customer import Customer


class ICustomerRepository(ABC):
    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def get_customer_by_id(self, customer_id: int) -> Customer | None:
        pass

    @abstractmethod
    def list_customers(self) -> list[Customer]:
        pass


class ICustomerPresenter(ABC):
    @abstractmethod
    def present_customer_list(self, customers: list[Customer]) -> dict:
        pass
