from l2_use_cases.calculate_result_use_case import CalculateResultUseCase
from l2_use_cases.clear_use_case import ClearUseCase
from l2_use_cases.input_decimal_use_case import InputDecimalUseCase
from l2_use_cases.input_digit_use_case import InputDigitUseCase
from l2_use_cases.input_operator_use_case import InputOperatorUseCase


class CalculatorController:
    """
    The controller that handles user input from the GUI and invokes the
    appropriate use cases.

    It acts as an adapter between the GUI events and the application's
    core logic.
    """

    def __init__(
        self,
        input_digit_use_case: InputDigitUseCase,
        input_operator_use_case: InputOperatorUseCase,
        input_decimal_use_case: InputDecimalUseCase,
        calculate_result_use_case: CalculateResultUseCase,
        clear_use_case: ClearUseCase,
    ):
        self._input_digit_use_case = input_digit_use_case
        self._input_operator_use_case = input_operator_use_case
        self._input_decimal_use_case = input_decimal_use_case
        self._calculate_result_use_case = calculate_result_use_case
        self._clear_use_case = clear_use_case

    def handle_digit(self, digit: str):
        self._input_digit_use_case.execute(digit)

    def handle_operator(self, operator: str):
        self._input_operator_use_case.execute(operator)

    def handle_decimal(self):
        self._input_decimal_use_case.execute()

    def handle_equals(self):
        self._calculate_result_use_case.execute()

    def handle_clear(self):
        self._clear_use_case.execute()
