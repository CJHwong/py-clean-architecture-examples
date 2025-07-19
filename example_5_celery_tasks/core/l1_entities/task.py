from dataclasses import dataclass
from typing import Any


@dataclass
class Task:
    task_id: str
    status: str
    payload: Any
    result: Any | None = None
