from l1_entities.calculator_state import CalculatorState
from l2_use_cases.boundaries.i_calculator_presenter import ICalculatorPresenter


class InputOperatorUseCase:
    """
    Use case for handling an operator input (+, -, x, ÷).
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

    def execute(self, operator: str):
        """
        Handles the logic for when an operator is pressed.
        """
        try:
            input_value = float(self._state.display_value)
        except ValueError:
            self._presenter.present_update("Error")
            self._state.reset()
            return

        # If an operator is already pending, calculate the result first
        if self._state.operator and self._state.waiting_for_second_operand:
            self._state.operator = operator
            return

        if self._state.first_operand is None:
            self._state.first_operand = input_value
        elif self._state.operator:
            result = self._calculate()
            self._state.display_value = self._format_result(result)
            self._state.first_operand = result
            self._presenter.present_update(self._state.display_value)

        self._state.operator = operator
        self._state.waiting_for_second_operand = True

    def _calculate(self) -> float:
        """Performs the calculation."""
        if self._state.operator not in self._operations:
            return float(self._state.display_value)

        operation = self._operations[self._state.operator]
        second_operand = float(self._state.display_value)

        try:
            result = operation(self._state.first_operand, second_operand)
        except ZeroDivisionError:
            self._presenter.present_update("Error")
            self._state.reset()
            return 0.0

        return result

    def _format_result(self, result: float) -> str:
        """Formats the result, removing .0 for integers."""
        if result == int(result):
            return str(int(result))
        return str(result)
