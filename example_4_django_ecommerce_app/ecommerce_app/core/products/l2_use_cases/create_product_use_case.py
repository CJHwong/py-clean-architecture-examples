from dataclasses import dataclass

from ecommerce_app.core.products.l1_entities.product import Product
from ecommerce_app.core.products.l2_use_cases.boundaries import (
    IProductPresenter,
    IProductRepository,
)


@dataclass
class CreateProductRequest:
    name: str
    description: str
    price: float


@dataclass
class CreateProductResponse:
    product_id: int
    name: str
    description: str
    price: float


class CreateProductUseCase:
    def __init__(
        self,
        product_repository: IProductRepository,
        product_presenter: IProductPresenter,
    ):
        self.product_repository = product_repository
        self.product_presenter = product_presenter

    def execute(self, request: CreateProductRequest) -> CreateProductResponse:
        product = Product(
            id=None,
            name=request.name,
            description=request.description,
            price=request.price,
            created_at=None,
        )
        created_product = self.product_repository.create_product(product)
        return CreateProductResponse(
            product_id=created_product.id,
            name=created_product.name,
            description=created_product.description,
            price=created_product.price,
        )
