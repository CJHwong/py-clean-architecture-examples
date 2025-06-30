from django.http import JsonResponse
from django.shortcuts import render
from ecommerce_app.core.customers.l2_use_cases.create_customer_use_case import (
    CreateCustomerRequest,
)
from ecommerce_app.core.customers.l4_frameworks_and_drivers.django_dependencies import (
    get_create_customer_use_case,
    get_list_customers_use_case,
)
from ecommerce_app.core.orders.l2_use_cases.create_order_use_case import (
    CreateOrderRequest,
)
from ecommerce_app.core.orders.l4_frameworks_and_drivers.django_dependencies import (
    get_create_order_use_case,
    get_list_orders_use_case,
)
from ecommerce_app.core.products.l2_use_cases.create_product_use_case import (
    CreateProductRequest,
)
from ecommerce_app.core.products.l4_frameworks_and_drivers.django_dependencies import (
    get_create_product_use_case,
    get_list_products_use_case,
)


def product_list_view(request):
    list_products_use_case = get_list_products_use_case()
    products_data = list_products_use_case.execute()
    return render(request, "ecommerce_app/products/product_list.html", products_data)


def create_product_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = float(request.POST.get("price"))

        create_product_use_case = get_create_product_use_case()
        request_model = CreateProductRequest(name=name, description=description, price=price)
        response = create_product_use_case.execute(request_model)
        return JsonResponse(
            {
                "message": "Product created successfully",
                "product_id": response.product_id,
            },
        )
    return render(request, "ecommerce_app/products/create_product.html")


def customer_list_view(request):
    list_customers_use_case = get_list_customers_use_case()
    customers_data = list_customers_use_case.execute()
    return render(request, "ecommerce_app/customers/customer_list.html", customers_data)


def create_customer_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        create_customer_use_case = get_create_customer_use_case()
        request_model = CreateCustomerRequest(name=name, email=email)
        response = create_customer_use_case.execute(request_model)
        return JsonResponse(
            {
                "message": "Customer created successfully",
                "customer_id": response.customer_id,
            },
        )
    return render(request, "ecommerce_app/customers/create_customer.html")


def order_list_view(request):
    list_orders_use_case = get_list_orders_use_case()
    orders_data = list_orders_use_case.execute()
    return render(request, "ecommerce_app/orders/order_list.html", orders_data)


def create_order_view(request):
    if request.method == "POST":
        customer_id = int(request.POST.get("customer_id"))
        product_id = int(request.POST.get("product_id"))
        quantity = int(request.POST.get("quantity"))

        create_order_use_case = get_create_order_use_case()
        request_model = CreateOrderRequest(customer_id=customer_id, product_id=product_id, quantity=quantity)
        response = create_order_use_case.execute(request_model)
        return JsonResponse({"message": "Order created successfully", "order_id": response.order_id})
    return render(request, "ecommerce_app/orders/create_order.html")
