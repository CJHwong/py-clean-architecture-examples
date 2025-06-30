from ecommerce_app.core.products.l2_use_cases.boundaries import (
    IProductPresenter,
    IProductRepository,
)
from ecommerce_app.core.products.l2_use_cases.create_product_use_case import (
    CreateProductUseCase,
)
from ecommerce_app.core.products.l2_use_cases.list_products_use_case import (
    ListProductsUseCase,
)
from ecommerce_app.core.products.l3_interface_adapters.gateways.django_product_repository import (
    DjangoProductRepository,
)
from ecommerce_app.core.products.l3_interface_adapters.presenters.product_list_presenter import (
    ProductListPresenter,
)


def get_product_repository() -> IProductRepository:
    return DjangoProductRepository()


def get_product_presenter() -> IProductPresenter:
    return ProductListPresenter()


def get_create_product_use_case() -> CreateProductUseCase:
    return CreateProductUseCase(get_product_repository(), get_product_presenter())


def get_list_products_use_case() -> ListProductsUseCase:
    return ListProductsUseCase(get_product_repository(), get_product_presenter())
