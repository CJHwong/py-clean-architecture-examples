# Example 5: Django Project with Multiple Features

This example demonstrates a Django project structured using Clean Architecture principles, where the core logic is organized by feature, suitable for more complex applications with many distinct features.

Each major feature (e.g., Products, Orders, Customers) has its own dedicated set of Clean Architecture layers (`l1_entities`, `l2_use_cases`, `l3_interface_adapters`, `l4_frameworks_and_drivers`) within the `ecommerce_app/core/` directory.

## Project Structure

```plaintext
example_5_django_complex_features/
├── manage.py
├── README.md
├── django_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
└── ecommerce_app/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   └── 0001_initial.py
    ├── core/
    │   ├── products/
    │   │   ├── l1_entities/
    │   │   │   └── product.py
    │   │   ├── l2_use_cases/
    │   │   │   ├── boundaries.py
    │   │   │   ├── create_product_use_case.py
    │   │   │   └── list_products_use_case.py
    │   │   ├── l3_interface_adapters/
    │   │   │   ├── gateways/
    │   │   │   │   └── django_product_repository.py
    │   │   │   └── presenters/
    │   │   │       └── product_list_presenter.py
    │   │   └── l4_frameworks_and_drivers/
    │   │       └── django_dependencies.py
    │   ├── orders/
    │   │   ├── l1_entities/
    │   │   │   └── order.py
    │   │   ├── l2_use_cases/
    │   │   │   ├── boundaries.py
    │   │   │   ├── create_order_use_case.py
    │   │   │   └── list_orders_use_case.py
    │   │   ├── l3_interface_adapters/
    │   │   │   ├── gateways/
    │   │   │   │   └── django_order_repository.py
    │   │   │   └── presenters/
    │   │   │       └── order_list_presenter.py
    │   │   └── l4_frameworks_and_drivers/
    │   │       └── django_dependencies.py
    │   └── customers/
    │       ├── l1_entities/
    │       │   └── customer.py
    │       ├── l2_use_cases/
    │       │   ├── boundaries.py
    │       │   ├── create_customer_use_case.py
    │       │   └── list_customers_use_case.py
    │       ├── l3_interface_adapters/
    │       │   ├── gateways/
    │       │   │   └── django_customer_repository.py
    │       │   └── presenters/
    │       │       └── customer_list_presenter.py
    │       └── l4_frameworks_and_drivers/
    │           └── django_dependencies.py
    └── templates/
        └── ecommerce_app/
            ├── products/
            │   ├── create_product.html
            │   └── product_list.html
            ├── customers/
            │   ├── create_customer.html
            │   └── customer_list.html
            └── orders/
                ├── create_order.html
                └── order_list.html
```

## How to Run

1. **Navigate to the project directory:**

    ```bash
    cd example_5_django_complex_features
    ```

2. **Install dependencies:**

    ```bash
    pip install Django
    ```

3. **Make migrations:**

    ```bash
    python3 manage.py makemigrations ecommerce_app
    ```

4. **Apply migrations:**

    ```bash
    python3 manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python3 manage.py runserver
    ```

6. **Access the application:**
    Open your web browser and go to:
    - Products: `http://127.0.0.1:8000/products/`
    - Create Product: `http://127.0.0.1:8000/products/create/`
    - Customers: `http://127.0.0.1:8000/customers/`
    - Create Customer: `http://127.0.0.1:8000/customers/create/`
    - Orders: `http://127.0.0.1:8000/orders/`
    - Create Order: `http://127.0.0.1:8000/orders/create/`
