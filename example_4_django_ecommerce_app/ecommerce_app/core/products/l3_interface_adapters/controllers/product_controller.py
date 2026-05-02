from ecommerce_app.core.products.l2_use_cases.create_product_use_case import (
    CreateProductRequest,
    CreateProductResponse,
    CreateProductUseCase,
)
from ecommerce_app.core.products.l2_use_cases.list_products_use_case import (
    ListProductsUseCase,
)


class ProductController:
    def __init__(
        self,
        create_use_case: CreateProductUseCase,
        list_use_case: ListProductsUseCase,
    ):
        self._create_use_case = create_use_case
        self._list_use_case = list_use_case

    def create(self, name: str, description: str, price: float) -> CreateProductResponse:
        request = CreateProductRequest(name=name, description=description, price=price)
        return self._create_use_case.execute(request)

    def list_all(self) -> dict:
        return self._list_use_case.execute()
