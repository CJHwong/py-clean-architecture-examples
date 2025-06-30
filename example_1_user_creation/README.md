# Clean Architecture Example 1: User Creation

This folder demonstrates the principles of **Clean Architecture** (as described by Robert C. Martin, Uncle Bob) using a simple user creation use case.  
**Note:** This README covers only the `example_1_user_creation` subproject. For an overview of the entire repository and other examples, see the main project README.

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

This example uses a layered folder structure to mirror the Clean Architecture circle:

```plaintext
example_1_user_creation/
├── l1_entities/                # Entities (Enterprise Business Rules)
├── l2_use_cases/               # Use Cases (Application Business Rules)
│   └── boundaries/             # Use Case Boundaries (Interfaces)
├── l3_interface_adapters/      # Interface Adapters (Controllers, Presenters, Gateways)
│   ├── controllers/
│   ├── gateways/
│   └── presenters/
├── l4_frameworks_and_drivers/  # Frameworks & Drivers (UI, DB, External Devices)
│   └── main.py
└── main.py                     # Entry Point
```

### Layer Descriptions

- **Entities (`l1_entities/`)**  
  - Contains core business objects and logic.  
  - Example: `user.py` defines the `User` entity, independent of any frameworks or external systems.

- **Use Cases (`l2_use_cases/`)**  
  - Application-specific business rules.  
  - Example: `create_user_use_case.py` implements the logic for creating a user, using only interfaces for data access and presentation.

- **Boundaries (`l2_use_cases/boundaries/`)**  
  - Abstract interfaces for repositories and presenters.  
  - Example: `i_user_repository.py` defines the contract for user data storage, allowing for different implementations.

- **Interface Adapters (`l3_interface_adapters/`)**  
  - Adapts data and requests between the use cases and the outside world.  
  - Example:  
    - `controllers/user_cli_controller.py` parses CLI input and calls use cases.  
    - `gateways/in_memory_user_repository.py` provides an in-memory implementation of the repository interface.  
    - `presenters/user_cli_presenter.py` formats output for the CLI.

- **Frameworks & Drivers (`l4_frameworks_and_drivers/`)**  
  - Contains code that interacts with external frameworks, databases, or devices.  
  - Example: `main.py` wires up the application, assembling controllers, use cases, and gateways.

## How This Example Binds to Clean Architecture

- **Independence of Frameworks**:  
  The core logic (entities and use cases) does not depend on any external libraries or frameworks. Framework-specific code is isolated in the outermost layer.

- **Testability**:  
  Use cases and entities can be tested in isolation by providing mock implementations of boundaries.

- **Replaceable Details**:  
  You can swap out the in-memory repository for a database-backed one without changing the use case logic.

- **Direction of Dependencies**:  
  All dependencies point inwards, following the Dependency Rule. Outer layers know about inner layers, but not vice versa.

## References

- [Clean Architecture Book](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/)
- [The Clean Architecture Circle Diagram](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)

---

This README should help users understand how your example implements Clean Architecture, and how each part of your codebase maps to the concepts and terminology from the book.
