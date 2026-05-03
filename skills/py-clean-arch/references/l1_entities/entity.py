from dataclasses import dataclass, field


@dataclass
class Entity:
    id: str | None = field(default=None)
