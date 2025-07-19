from dataclasses import dataclass


@dataclass
class CalculatorState:
    """
    An entity representing the complete state of the calculator.

    This is a pure data class with no logic other than representing
    the current state. It lives in the innermost layer of the architecture
    and has no dependencies on any other layer.
    """

    display_value: str = "0"
    first_operand: float | None = None
    operator: str | None = None
    waiting_for_second_operand: bool = False

    def reset(self):
        """Resets the calculator to its initial state."""
        self.display_value = "0"
        self.first_operand = None
        self.operator = None
        self.waiting_for_second_operand = False
