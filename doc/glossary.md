# Clean Architecture Glossary

This glossary provides definitions for the key vocabulary used in Clean Architecture, based on Robert C. Martin's principles. The terms are organized to help developers map the concepts directly to the folder structures in this repository's examples.

---

## Index

### A

- **Actor**
  > A group of users or stakeholders who require changes in the software for the same reasons. The SRP states a module should be responsible to a single actor.

- **Application Business Rules**
  > The layer of rules that are specific to a single application, defining its features and behavior. This is the formal name for the **Use Cases** layer (the red circle).

- **Architecture**
  > The overarching structure of a software system. A good architecture minimizes lifetime maintenance costs and maximizes programmer productivity by keeping options open and separating high-level policy from low-level detail. It should "scream" the system's purpose.

- **Acyclic Dependencies Principle (ADP)**
  > A component coupling principle stating that the dependency graph between components must have no cycles. Cycles create "mega-components" that are difficult to develop, test, and deploy independently.

### B

- **Boundaries**
  > A conceptual line that separates different software elements to prevent changes from propagating across them. Boundaries are implemented by managing source code dependencies, typically using the Dependency Inversion Principle. They are the key to creating a "plugin" architecture.

### C

- **Clean Architecture**
  > An architectural model, famously depicted as concentric circles ("the onion diagram"), that organizes a system into layers, each with a distinct responsibility. Its single most important rule is The Dependency Rule.

- **Common Closure Principle (CCP)**
  > A component cohesion principle that advises gathering classes that change for the same reasons and at the same times into the same component. This is the SRP applied at the component level.

- **Common Reuse Principle (CRP)**
  > A component cohesion principle that advises against forcing users of a component to depend on things they don't need. This is the ISP applied at the component level.

- **Component**
  > The smallest unit of deployment in a system (e.g., a Java `.jar` file, a Python package). Architecture is concerned with how these components are composed and how they relate to one another.

- **Controller**
  > A type of Interface Adapter that handles input from an external source (like a UI or a web request), parses it into a format convenient for a Use Case, and then passes it to the Use Case Input Port.

### D

- **DB (Database)**
  > Part of the Frameworks & Drivers layer. It represents the specific persistence mechanism (e.g., PostgreSQL, MongoDB, a file system) for the application. It is a low-level detail.

- **Dependency Inversion Principle (DIP)**
  > The principle stating that high-level modules should not depend on low-level modules; both should depend on abstractions. Furthermore, abstractions should not depend on details; details should depend on abstractions. This is the primary mechanism for creating boundaries.

- **The Dependency Rule**
  > The single, overarching rule of Clean Architecture: **source code dependencies can only point inwards**. Nothing in an inner circle can know anything at all about something in an outer circle.

- **Devices**
  > Part of the Frameworks & Drivers layer. Refers to the external mechanisms through which a user or other system interacts with the application (e.g., a browser, a mobile device screen, a command line).

### E

- **Enterprise Business Rules**
  > The core, high-level rules and data structures of the business, which are independent of any single application. This is the formal name for the **Entities** layer (the yellow circle).

- **Entities**
  > The innermost circle of the Clean Architecture. Entities encapsulate enterprise-wide, critical business rules and data structures. They are the highest-level policies and are independent of any specific application.

- **External Interfaces**
  > Part of the Frameworks & Drivers layer. This refers to the code that manages communication with other systems, such as third-party APIs or external services.

### F

- **Flow of Control**
  > The path of execution through the system. In Clean Architecture, the flow of control typically starts in a Controller, moves through a Use Case, and ends in a Presenter, while source code dependencies always point in the opposite direction (towards the Use Case).

- **Frameworks and Drivers**
  > The outermost circle of the Clean Architecture (the blue circle). This layer is where all the details go, such as the web framework, database drivers, UI frameworks, and external libraries. These are "plugins" to the core business logic.

### G

- **Gateway**
  > A type of Interface Adapter that provides a bridge to an external system, most commonly a database. Gateways implement interfaces defined by the Use Cases layer, allowing the core application to be ignorant of the persistence specifics. Often called a Repository.

### I

- **Interface Adapters**
  > The third circle of the Clean Architecture (the green circle). This layer's responsibility is to convert data from the format most convenient for the inner circles (Use Cases, Entities) to the format most convenient for the outer circle (Frameworks, Drivers), and vice-versa. This includes Controllers, Presenters, and Gateways.

### P

- **Presenter**
  > A type of Interface Adapter that takes data from the Use Case Output Port, formats it for presentation to the user (e.g., into a View Model), and makes it available to the UI. It is the architectural boundary on the output side of a use case.

### S

- **Screaming Architecture**
  > An architecture that clearly expresses its purpose and domain, rather than the frameworks it uses. The top-level directory structure should reflect the system's use cases (e.g., `orders`, `products`), not technical details (e.g., `controllers`, `models`).

- **Single Responsibility Principle (SRP)**
  > A SOLID principle stating that a module should have one, and only one, reason to change. The "reason to change" is tied to a single **Actor**.

### U

- **UI (User Interface)**
  > Part of the Frameworks & Drivers layer. The specific framework or technology used to render the user interface (e.g., React, HTML/CSS). It is a detail that is kept isolated from the core business logic.

- **Use Case Input Port**
  > An interface implemented by the Use Case Interactor. It defines the method(s) that the Controller will call to execute the use case and specifies the format of the input data.

- **Use Case Interactor**
  > The object that implements a specific use case or application-specific business rule. It orchestrates the flow of data, calls on Entities to perform critical business logic, and directs the output through a Use Case Output Port.

- **Use Case Output Port**
  > An interface implemented by the Presenter. It defines the method(s) that the Use Case Interactor will call to present the results and specifies the format of the output data.

- **Use Cases**
  > The second circle of the Clean Architecture (the red circle). Use Cases are application-specific business rules that orchestrate Entities to achieve a particular user goal. They define and implement the system's operations.

### W

- **Web**
  > Part of the Frameworks & Drivers layer. The specific web framework or server technology used to handle web requests and responses (e.g., Flask, Django, Express). It is a delivery mechanism and a detail.
