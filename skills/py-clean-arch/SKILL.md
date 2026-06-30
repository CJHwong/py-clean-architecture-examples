---
name: py-clean-arch
description: Use this skill when the user asks about Clean Architecture in Python — not generic theory, but the specific layer conventions (l1_entities, l2_use_cases, l3_interface_adapters, l4_frameworks_and_drivers), folder patterns, boundary interfaces, and .importlinter.ini contracts from CJHwong/py-clean-architecture-examples. Fetches live code from that repo as the authoritative reference. Also use when the user wants to scaffold a Python CLI, FastAPI, Django, or Celery project with CA layers.
---

# py-clean-arch

Two modes:

**Scaffold** — create project files by fetching the matching example from GitHub and adapting it.
**Explain** — answer CA questions using this repo's docs, not generic Uncle Bob recaps.

---

## Reference structure

`references/` is a runnable minimal CA project — actual `.py` files, not docs.

| File | Role |
|------|------|
| `l1_entities/entity.py` | Domain entity (pure dataclass, no dependencies) |
| `l2_use_cases/boundaries/i_entity_repository.py` | Abstract repository port |
| `l2_use_cases/boundaries/i_entity_presenter.py` | Abstract presenter port |
| `l2_use_cases/action_entity_use_case.py` | Use case with DI via constructor |
| `l3_interface_adapters/controllers/entity_controller.py` | Converts input to use case invocation |
| `l3_interface_adapters/gateways/in_memory_entity_repository.py` | Repository implementation |
| `l3_interface_adapters/presenters/entity_presenter.py` | Presenter implementation |
| `l4_frameworks_and_drivers/main.py` | Composition root — DI factory (`create_controller()`) |
| `main.py` | Entry point — imports factory, creates controller, calls `handle()` |
| `.importlinter.ini` | Layer dependency contracts (5 rules) |

Key patterns:
- **Dependency inversion**: inner layers define interfaces (`boundaries/`), outer layers implement them
- **l4 as factory**: `l4_frameworks_and_drivers/main.py` exports a `create_controller()` factory — no side effects
- **Entry point is thin**: root `main.py` just imports the factory, wires, and invokes
- **boundaries/ per interface**: each boundary gets its own file (one class per file)

---

## Repo docs

Fetch on demand. These are the authoritative source for *why* the repo is structured the way it is.

| Doc | Raw URL | Fetch when |
|-----|---------|------------|
| Core Principles | `https://raw.githubusercontent.com/CJHwong/py-clean-architecture-examples/main/doc/principles.md` | User asks about layers, dependency rule, boundaries, testability, screaming architecture |
| Glossary | `https://raw.githubusercontent.com/CJHwong/py-clean-architecture-examples/main/doc/glossary.md` | User asks what a term means (entity, gateway, presenter, boundary, controller, etc.) |

---

## Scaffold mode

### Step 1 — Interview

One message, ask only for what's missing:

1. **Project name** — snake_case (e.g., `order_service`)
2. **Type** — `cli` | `fastapi` | `django` | `celery`
3. **Entity** — PascalCase domain object (e.g., `Order`). Multiple OK.
4. **Action** — use case verb (e.g., `create`, `submit`)

### Step 2 — Read the reference files

Read every `.py` file in `references/` before fetching anything. These are the canonical CA patterns: entity dataclass, boundary interfaces, use case DI, controller, gateway, presenter, and l4 factory. Internalize the structure — all substitutions will map onto these patterns.

### Step 3 — Fetch the example from GitHub

| Type | Example directory |
|------|-------------------|
| `cli` | `example_1_user_creation` |
| `fastapi` | `example_2_fastapi_todo_app` |
| `django` | `example_3_django_todo_app` |
| `celery` | `example_5_celery_tasks` |

Get the file tree:
```
https://api.github.com/repos/CJHwong/py-clean-architecture-examples/git/trees/main?recursive=1
```
Filter to paths under the example directory, skip `__pycache__` and `.pyc`. Fetch raw content for each file:
```
https://raw.githubusercontent.com/CJHwong/py-clean-architecture-examples/main/<path>
```

At minimum fetch: `.importlinter.ini`, one entity, one use case, all boundary files, one gateway, one presenter, one controller (if present), the l4 entry point.

### Step 4 — Adapt the example

Create the project directory and write every file from the fetched example with these substitutions:

| Replace | With |
|---------|------|
| Example package root (e.g., `example_1_user_creation`) | `<project_name>` |
| Example entity name (e.g., `User`, `TodoItem`) | User's entity |
| Example action (e.g., `create`, `process`) | User's action |

Also replace all import paths, class names, and file names throughout. End with the run hint for the type (`python main.py`, `uvicorn main:app --reload`, `python manage.py runserver`, etc.).

### Gotchas

Things an agent gets wrong without being told:

**`.importlinter.ini` root_package is always `<project_name>`** — the project folder is the Python package. Layer paths nest under it:
- `cli`: `<project>.l4_frameworks_and_drivers` — flat, no sub-app
- `fastapi`: `<project>.<app>_app.core.l4_frameworks_and_drivers`
- `django`: `<project>.<app>_app.core.l4_frameworks_and_drivers`
- `celery`: `<project>.core.l4_frameworks_and_drivers`

**`boundaries/` vs `boundaries.py` varies by example.** `cli` and `celery` use a `boundaries/` subdirectory with one file per interface. `fastapi` and `django` use a single `boundaries.py`. Match whatever the fetched example uses — don't standardize.

**Celery's boundary interface is a queue, not a presenter.** `l2_use_cases/boundaries/` contains `i_<entity>_queue.py` (with `enqueue()`), not an `i_<entity>_presenter.py`. The celery gateway in l3 implements the queue interface. Presenters still exist in l3 but are called from the Flask trigger (`app.py`), not from use cases.

**Django ORM models live outside `core/`.** `<app>/models.py` is in the Django app layer, not inside `l3_interface_adapters/`. The Django gateway in `core/l3_interface_adapters/gateways/` imports from `models.py`. Don't move models into core.

**At scale, all inbound ports are gateways.** The `i_*_repository` / `i_*_presenter` split in `references/` is the textbook form. Production adoptions collapse every L2 port to one term — `<role>_gateway.py` with class `<Role>Gateway(ABC)`, no `i_` prefix — even when it's conceptually a repository. L3 impls are named by their backing provider, and one port commonly has several (`django_*`, `fms_*`, `aws_*`, `composite_*`). Don't force the repository/presenter naming on a real service.

**Presenters drop out of L2 once there's an HTTP API.** The injected-presenter output port (use case calls `presenter.present()`) is for CLI/template UIs. With a JSON API, the use case returns a plain DTO and the presenter lives in L3, called by the controller (router/view), not the use case. Don't add an `i_*_presenter` boundary to a FastAPI/Ninja service.

**Scope the no-frameworks-in-core contract to I/O SDKs.** The `references/` contract bans a long list (django, fastapi, pydantic, sqlalchemy...). Real adoptions keep only true I/O SDKs out of L1/L2 — `requests`, `boto3`, `botocore` — and let the layers contract handle the framework boundary. Banning pydantic or dataclasses-adjacent libs in core is more than production keeps.
