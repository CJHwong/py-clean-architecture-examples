from django.http import JsonResponse
from django.shortcuts import render
from ecommerce_app.core.customers.l4_frameworks_and_drivers.django_dependencies import (
    get_customer_controller,
)
from ecommerce_app.core.orders.l4_frameworks_and_drivers.django_dependencies import (
    get_order_controller,
)
from ecommerce_app.core.products.l4_frameworks_and_drivers.django_dependencies import (
    get_product_controller,
)


def product_list_view(request):
    products_data = get_product_controller().list_all()
    return render(request, "ecommerce_app/products/product_list.html", products_data)


def create_product_view(request):
    if request.method == "POST":
        response = get_product_controller().create(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            price=float(request.POST.get("price")),
        )
        return JsonResponse({"message": "Product created successfully", "product_id": response.product_id})
    return render(request, "ecommerce_app/products/create_product.html")


def customer_list_view(request):
    customers_data = get_customer_controller().list_all()
    return render(request, "ecommerce_app/customers/customer_list.html", customers_data)


def create_customer_view(request):
    if request.method == "POST":
        response = get_customer_controller().create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
        )
        return JsonResponse({"message": "Customer created successfully", "customer_id": response.customer_id})
    return render(request, "ecommerce_app/customers/create_customer.html")


def order_list_view(request):
    orders_data = get_order_controller().list_all()
    return render(request, "ecommerce_app/orders/order_list.html", orders_data)


def create_order_view(request):
    if request.method == "POST":
        response = get_order_controller().create(
            customer_id=int(request.POST.get("customer_id")),
            product_id=int(request.POST.get("product_id")),
            quantity=int(request.POST.get("quantity")),
        )
        return JsonResponse({"message": "Order created successfully", "order_id": response.order_id})
    return render(request, "ecommerce_app/orders/create_order.html")
