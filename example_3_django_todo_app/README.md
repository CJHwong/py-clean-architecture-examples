# Clean Architecture Example 3: Django Todo App

This folder demonstrates how to apply **Clean Architecture** principles (as described by Robert C. Martin, Uncle Bob) in a Django-based Todo application.  
**Note:** This README covers only the example_3_django_project subproject. For an overview of the entire repository and other examples, see the main project README.

## Clean Architecture Circle Diagram

```plaintext
+-----------------------------+
|   Frameworks & Drivers      |  (Outer Layer)
+-----------------------------+
|   Interface Adapters        |  (Second Layer)
+-----------------------------+
|   Use Cases                 |  (Third Layer)
+-----------------------------+
|   Entities                  |  (Innermost Layer)
+-----------------------------+
```

- **Dependencies always point inwards**: Outer layers depend on inner layers, never the reverse.

## Project Structure Mapping

This example uses a layered folder structure inside the Django app to mirror the Clean Architecture circle:

```plaintext
example_3_django_project/
├── manage.py
├── db.sqlite3
├── django_project/                  # Django project settings
│   └── ...
└── todo_app/                        # Main Django app
    ├── models.py                    # Django ORM models (for DB)
    ├── views.py                     # Django views (Web controllers)
    ├── urls.py
    ├── templates/
    ├── core/
    │   ├── l1_entities/             # Entities (Enterprise Business Rules)
    │   ├── l2_use_cases/            # Use Cases (Application Business Rules)
    │   ├── l3_interface_adapters/   # Interface Adapters (Controllers, Presenters, Gateways)
    │   └── l4_frameworks_and_drivers/ # Frameworks & Drivers (Django, DB, etc.)
    └── ...
```

### Layer Descriptions

- **Entities (`core/l1_entities/`)**  
  - Contains core business objects and logic, independent of Django or any framework.

- **Use Cases (`core/l2_use_cases/`)**  
  - Application-specific business rules.  
  - Implements the logic for todo operations, using only interfaces for data access and presentation.

- **Interface Adapters (`core/l3_interface_adapters/`)**  
  - Adapts data and requests between the use cases and the outside world.  
  - Example: Adapters for converting Django requests to use case input, and formatting use case output for Django views.

- **Frameworks & Drivers (`core/l4_frameworks_and_drivers/` and Django files)**  
  - Contains code that interacts with Django, the database, and other external systems.  
  - Example: `models.py` (Django ORM), `views.py` (Django views), and the main Django app wiring.

## How This Example Binds to Clean Architecture

- **Framework Independence**:  
  Core logic (entities and use cases) is isolated from Django. Framework-specific code is kept in the outermost layer.

- **Testability**:  
  Use cases and entities can be tested in isolation by providing mock implementations of boundaries.

- **Replaceable Details**:  
  You can swap out the database or web framework with minimal changes to the core logic.

- **Direction of Dependencies**:  
  All dependencies point inwards, following the Dependency Rule. Outer layers know about inner layers, but not vice versa.

## References

- [Clean Architecture Book](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/)
- [The Clean Architecture Circle Diagram](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)

---

This README should help users understand how this Django example implements Clean Architecture, and how each part of the codebase maps to the concepts and terminology from the book.
