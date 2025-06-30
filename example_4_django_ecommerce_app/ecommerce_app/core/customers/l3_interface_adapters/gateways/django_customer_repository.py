from ecommerce_app.core.customers.l1_entities.customer import Customer
from ecommerce_app.core.customers.l2_use_cases.boundaries import ICustomerRepository
from ecommerce_app.models import Customer as DjangoCustomer


class DjangoCustomerRepository(ICustomerRepository):
    def create_customer(self, customer: Customer) -> Customer:
        django_customer = DjangoCustomer.objects.create(name=customer.name, email=customer.email)
        return Customer(
            id=django_customer.id,
            name=django_customer.name,
            email=django_customer.email,
            created_at=django_customer.created_at,
        )

    def get_customer_by_id(self, customer_id: int) -> Customer | None:
        try:
            django_customer = DjangoCustomer.objects.get(id=customer_id)
            return Customer(
                id=django_customer.id,
                name=django_customer.name,
                email=django_customer.email,
                created_at=django_customer.created_at,
            )
        except DjangoCustomer.DoesNotExist:
            return None

    def list_customers(self) -> list[Customer]:
        django_customers = DjangoCustomer.objects.all()
        return [Customer(id=c.id, name=c.name, email=c.email, created_at=c.created_at) for c in django_customers]
