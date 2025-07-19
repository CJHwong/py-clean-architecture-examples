from l1_entities.calculator_state import CalculatorState
from l2_use_cases.boundaries.i_calculator_presenter import ICalculatorPresenter


class ClearUseCase:
    """
    Use case for handling the 'Clear' (C) operation.
    """

    def __init__(self, state: CalculatorState, presenter: ICalculatorPresenter):
        self._state = state
        self._presenter = presenter

    def execute(self):
        """
        Resets the calculator state and updates the display.
        """
        self._state.reset()
        self._presenter.present_update(self._state.display_value)
