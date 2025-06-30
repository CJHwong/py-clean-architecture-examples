import re
from dataclasses import dataclass


@dataclass
class User:
    """Entity:
    - This is the core enterprise business rule.
    - It is a pure Python object, independent of any framework or external library.
    - Encapsulates the most critical data and validation logic.
    """

    username: str
    password: str

    def __post_init__(self):
        """Validate immediately after object creation."""
        self._validate()

    def _validate(self):
        """Internal validation rules for the entity. This is the highest-level policy."""
        if not re.match("^[a-zA-Z0-9_]+$", self.username):
            raise ValueError("Username must be alphanumeric with underscores.")
        if len(self.password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

    # In a real application, the password should be hashed. Omitted here for simplicity.
    # def set_password(self, raw_password):
    #     self.password = hash(raw_password)
