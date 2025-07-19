from l1_entities.calculator_state import CalculatorState
from l2_use_cases.boundaries.i_calculator_presenter import ICalculatorPresenter


class InputDigitUseCase:
    """
    Use case for handling a digit input (0-9).
    """

    def __init__(self, state: CalculatorState, presenter: ICalculatorPresenter):
        self._state = state
        self._presenter = presenter

    def execute(self, digit: str):
        """
        Appends a digit to the current display value.
        """
        if self._state.waiting_for_second_operand:
            self._state.display_value = digit
            self._state.waiting_for_second_operand = False
        else:
            if self._state.display_value == "0":
                self._state.display_value = digit
            else:
                self._state.display_value += digit

        self._presenter.present_update(self._state.display_value)
