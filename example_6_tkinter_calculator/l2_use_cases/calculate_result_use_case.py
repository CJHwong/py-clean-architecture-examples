from l1_entities.calculator_state import CalculatorState
from l2_use_cases.boundaries.i_calculator_presenter import ICalculatorPresenter


class CalculateResultUseCase:
    """
    Use case for handling the '=' (equals) operation.
    """

    def __init__(self, state: CalculatorState, presenter: ICalculatorPresenter):
        self._state = state
        self._presenter = presenter
        self._operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "x": lambda a, b: a * b,
            "÷": lambda a, b: a / b,
        }

    def execute(self):
        """
        Performs the final calculation and updates the display.
        """
        if not self._state.operator or self._state.first_operand is None:
            return

        try:
            second_operand = float(self._state.display_value)
            operation = self._operations[self._state.operator]
            result = operation(self._state.first_operand, second_operand)

            self._state.display_value = self._format_result(result)
            self._presenter.present_update(self._state.display_value)
            self._state.reset()
            self._state.first_operand = result  # Keep result for chained calculations

        except (ValueError, ZeroDivisionError):
            self._presenter.present_update("Error")
            self._state.reset()

    def _format_result(self, result: float) -> str:
        """Formats the result, removing .0 for integers."""
        if result == int(result):
            return str(int(result))
        return str(result)
