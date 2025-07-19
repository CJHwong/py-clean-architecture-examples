[繁體中文版](./principles.zh-TW.md)

---

# Core Principles of Clean Architecture

This document provides a concise summary of the fundamental principles that underpin Clean Architecture. These principles guide the design of systems that are independent, testable, and easy to maintain.

## 1. The Dependency Rule

This is the most important rule in Clean Architecture. It dictates that **source code dependencies can only point inwards**.

- The concentric circles of the architecture diagram represent different levels of software, from high-level policies (Entities) in the center to low-level details (Frameworks & Drivers) on the outside.
- Nothing in an inner circle can know anything at all about something in an outer circle. Specifically, code in an inner circle cannot refer to any name (class, function, variable) declared in an outer circle.
- This ensures that the core business logic is completely decoupled from external concerns.

## 2. Independence

A key goal of the architecture is to create a system that is independent of external agencies.

- **Independent of Frameworks:** The core business logic does not depend on any specific library or framework (e.g., Django, FastAPI). The framework is a tool to be used, not a structure to conform to. It's a low-level detail.
- **Independent of the UI:** The UI can be replaced (e.g., from a web app to a console app) without any change to the underlying business rules.
- **Independent of the Database:** The core logic is not tied to a specific database vendor. You can swap PostgreSQL for MongoDB without changing the Entities or Use Cases.
- **Independent of Anything External:** The business rules should not know anything about the outside world.

## 3. Boundaries and Plugins

The architecture is built by establishing clear **boundaries** between layers.

- These boundaries are enforced by the Dependency Rule.
- The primary mechanism for creating these boundaries is the **Dependency Inversion Principle (DIP)**, where inner layers define interfaces (abstractions) that outer layers must implement.
- This turns the entire system into a "plugin" architecture. The UI, database, web framework, and other external services are all "plugins" to the central core of business rules.

## 4. Testability

A direct benefit of this separation is high testability.

- The **Enterprise Business Rules (Entities)** can be tested in complete isolation, as they have no external dependencies.
- The **Application Business Rules (Use Cases)** can also be tested without needing the UI, database, or web server. You can use simple test doubles (mocks or stubs) to stand in for the outer layers.
- This makes tests fast, reliable, and easy to write.

## 5. A "Screaming" Architecture

The top-level structure of the project should immediately communicate its purpose and domain, not the technology it uses.

- Instead of seeing `models`, `views`, `controllers` at the top level, you should see directories that reflect the system's use cases, such as `order_management`, `customer_accounts`, or `inventory_tracking`.
- The architecture should "scream" about the business domain, not about the frameworks.