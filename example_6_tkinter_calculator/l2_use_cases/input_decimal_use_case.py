from l1_entities.calculator_state import CalculatorState
from l2_use_cases.boundaries.i_calculator_presenter import ICalculatorPresenter


class InputDecimalUseCase:
    """
    Use case for handling the decimal point (.) input.
    """

    def __init__(self, state: CalculatorState, presenter: ICalculatorPresenter):
        self._state = state
        self._presenter = presenter

    def execute(self):
        """
        Adds a decimal point to the display value if one does not already exist.
        """
        if "." not in self._state.display_value:
            self._state.display_value += "."
            self._presenter.present_update(self._state.display_value)
