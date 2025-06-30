from abc import ABC, abstractmethod

from ecommerce_app.core.products.l1_entities.product import Product


class IProductRepository(ABC):
    @abstractmethod
    def create_product(self, product: Product) -> Product:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product | None:
        pass

    @abstractmethod
    def list_products(self) -> list[Product]:
        pass


class IProductPresenter(ABC):
    @abstractmethod
    def present_product_list(self, products: list[Product]) -> dict:
        pass
