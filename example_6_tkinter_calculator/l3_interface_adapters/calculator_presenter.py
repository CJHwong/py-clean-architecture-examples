from collections.abc import Callable

from l2_use_cases.boundaries.i_calculator_presenter import ICalculatorPresenter


class CalculatorPresenter(ICalculatorPresenter):
    def __init__(self, update_callback: Callable[[str], None]):
        self._update_callback = update_callback

    def present_update(self, display_value: str):
        self._update_callback(display_value)
