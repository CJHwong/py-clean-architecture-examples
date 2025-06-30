from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.product_list_view, name="product_list"),
    path("products/create/", views.create_product_view, name="create_product"),
    path("customers/", views.customer_list_view, name="customer_list"),
    path("customers/create/", views.create_customer_view, name="create_customer"),
    path("orders/", views.order_list_view, name="order_list"),
    path("orders/create/", views.create_order_view, name="create_order"),
]
