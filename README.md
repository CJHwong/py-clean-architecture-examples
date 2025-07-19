# Clean Architecture Examples

This repository demonstrates the Clean Architecture pattern in Python through several practical examples, each organized in its own directory. The goal is to illustrate how Clean Architecture principles can be applied to different types of applications, from simple CLI tools to web applications using FastAPI, Django, and background task queues with Celery.

A key ambition of this repository is to make the code structure **faithfully and transparently reflect the Clean Architecture circle diagram** (see below). Each example is carefully organized so that every folder and layer in the codebase directly maps to a corresponding ring in the diagram. This approach is intended to make the separation of concerns, direction of dependencies, and the role of each layer as clear and explicit as possible.

![Clean Architecture Diagram](https://blog.cleancoder.com/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg)

> **Note:** The folder names and their contents are chosen to match the terminology and boundaries of the Clean Architecture model: Entities, Use Cases, Interface Adapters, and Frameworks & Drivers. This structure is consistent across all examples, regardless of the underlying framework or application type.

## Table of Contents

- [Clean Architecture Examples](#clean-architecture-examples)
  - [Table of Contents](#table-of-contents)
  - [Import Linter](#import-linter)
  - [Example 1: User Creation CLI](#example-1-user-creation-cli)
  - [Example 2: FastAPI Todo App](#example-2-fastapi-todo-app)
  - [Example 3: Django Todo App](#example-3-django-todo-app)
  - [Example 4: Django Ecommerce App](#example-4-django-ecommerce-app)
  - [Example 5: Celery Task Queue](#example-5-celery-task-queue)
  - [Example 6: Tkinter GUI Calculator](#example-6-tkinter-gui-calculator)
  - [References](#references)
  - [TODO](#todo)

---

## Import Linter

This repository uses [Import Linter](https://github.com/seddonym/import-linter) via pre-commit to help enforce architectural boundaries between layers. The configuration is managed in `.pre-commit-config.yaml` and ensures that imports between Clean Architecture layers follow the intended dependency direction (e.g., inner layers should not import from outer layers).

To run the import linter manually:

```bash
pre-commit run pre-commit-import-linter --all-files
```

This will check for any import violations according to the rules defined in the configuration. The linter is also run automatically on every commit if you have pre-commit installed.

---

## Example 1: User Creation CLI

**Path:** `example_1_user_creation/`

A simple command-line application for user creation, structured according to Clean Architecture layers:

- **l1_entities:** Core business entities (e.g., `user.py`).
- **l2_use_cases:** Application use cases and boundaries (e.g., `create_user_use_case.py`).
- **l3_interface_adapters:** Controllers, presenters, and gateways for CLI interaction.
- **l4_frameworks_and_drivers:** Entry point and framework-specific code (e.g., `main.py`).

## Example 2: FastAPI Todo App

**Path:** `example_2_fastapi_todo_app/`

A web application using FastAPI, organized into Clean Architecture layers under `todo_app/core/`:

- **l1_entities:** Domain models for todos.
- **l2_use_cases:** Business logic for todo management.
- **l3_interface_adapters:** Adapters for API and persistence.
- **l4_frameworks_and_drivers:** FastAPI app entry point and configuration.

## Example 3: Django Todo App

**Path:** `example_3_django_todo_app/`

A Django-based todo application, with Clean Architecture layers inside `todo_app/core/`:

- **l1_entities:** Domain entities.
- **l2_use_cases:** Use case logic.
- **l3_interface_adapters:** Adapters for Django views and models.
- **l4_frameworks_and_drivers:** Django project and app setup.

## Example 4: Django Ecommerce App

**Path:** `example_4_django_ecommerce_app/`

A more complex Django application for ecommerce, where the core logic is organized by feature (Customers, Orders, Products). Each feature has its own set of Clean Architecture layers, demonstrating how the pattern scales.

## Example 5: Celery Task Queue

**Path:** `example_5_celery_tasks/`

Demonstrates how to integrate a background task queue (Celery) with a Flask web application while maintaining clean architecture. The `core` module is completely decoupled from the frameworks. The Flask app and Celery workers are external entry points that use factories from Layer 4 to build and execute use cases.

## Example 6: Tkinter GUI Calculator

**Path:** `example_6_tkinter_calculator/`

A reactive GUI application using Python's built-in `Tkinter` library. This example clearly demonstrates how the UI can be a simple "plugin" to the core business logic and how a reactive data flow can be achieved while respecting the Dependency Rule.

---

## References

- [Clean Architecture by Robert C. Martin](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Celery Documentation](https://docs.celeryq.dev/)

---

Each example is self-contained and includes a `README.md` with setup and usage instructions. Explore the directories for more details on each implementation.

---

## TODO

- [x] Add a glossary of allowed Clean Architecture vocabulary terms and their definitions. See [Glossary](./doc/glossary.md).
- [x] Write a concise summary of Clean Architecture principles for the introduction. See [Core Principles](./doc/principles.md).
- [x] Provide an example of a simple GUI application using Clean Architecture.
- [ ] Add more advanced examples (e.g., microservices, event-driven, or async patterns).
