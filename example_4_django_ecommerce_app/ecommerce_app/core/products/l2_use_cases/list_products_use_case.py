from ecommerce_app.core.products.l1_entities.product import Product
from ecommerce_app.core.products.l2_use_cases.boundaries import (
    IProductPresenter,
    IProductRepository,
)


class ListProductsUseCase:
    def __init__(
        self,
        product_repository: IProductRepository,
        product_presenter: IProductPresenter,
    ):
        self.product_repository = product_repository
        self.product_presenter = product_presenter

    def execute(self) -> list[Product]:
        products = self.product_repository.list_products()
        return self.product_presenter.present_product_list(products)
