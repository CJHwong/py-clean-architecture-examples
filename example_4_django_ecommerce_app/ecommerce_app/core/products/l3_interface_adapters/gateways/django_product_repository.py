from ecommerce_app.core.products.l1_entities.product import Product
from ecommerce_app.core.products.l2_use_cases.boundaries import IProductRepository
from ecommerce_app.models import Product as DjangoProduct


class DjangoProductRepository(IProductRepository):
    def create_product(self, product: Product) -> Product:
        django_product = DjangoProduct.objects.create(
            name=product.name,
            description=product.description,
            price=product.price,
        )
        return Product(
            id=django_product.id,
            name=django_product.name,
            description=django_product.description,
            price=float(django_product.price),
            created_at=django_product.created_at,
        )

    def get_product_by_id(self, product_id: int) -> Product | None:
        try:
            django_product = DjangoProduct.objects.get(id=product_id)
            return Product(
                id=django_product.id,
                name=django_product.name,
                description=django_product.description,
                price=float(django_product.price),
                created_at=django_product.created_at,
            )
        except DjangoProduct.DoesNotExist:
            return None

    def list_products(self) -> list[Product]:
        django_products = DjangoProduct.objects.all()
        return [
            Product(
                id=p.id,
                name=p.name,
                description=p.description,
                price=float(p.price),
                created_at=p.created_at,
            )
            for p in django_products
        ]
