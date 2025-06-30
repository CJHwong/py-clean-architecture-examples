from ecommerce_app.core.products.l1_entities.product import Product
from ecommerce_app.core.products.l2_use_cases.boundaries import IProductPresenter


class ProductListPresenter(IProductPresenter):
    def present_product_list(self, products: list[Product]) -> dict:
        return {
            "products": [
                {
                    "id": p.id,
                    "name": p.name,
                    "description": p.description,
                    "price": p.price,
                }
                for p in products
            ],
        }
