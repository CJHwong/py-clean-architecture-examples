import tkinter as tk

from l1_entities.calculator_state import CalculatorState
from l2_use_cases.calculate_result_use_case import CalculateResultUseCase
from l2_use_cases.clear_use_case import ClearUseCase
from l2_use_cases.input_decimal_use_case import InputDecimalUseCase
from l2_use_cases.input_digit_use_case import InputDigitUseCase
from l2_use_cases.input_operator_use_case import InputOperatorUseCase
from l3_interface_adapters.calculator_controller import CalculatorController
from l3_interface_adapters.calculator_presenter import CalculatorPresenter
from l4_frameworks_and_drivers.gui import CalculatorView


def main():
    # 1. Core state entity
    state = CalculatorState()

    # 2. Framework objects (tkinter) created here in the composition root
    window = tk.Tk()
    display_var = tk.StringVar(value="0")

    # 3. Presenter wired to the display callback — no tkinter dependency inside presenter
    presenter = CalculatorPresenter(display_var.set)

    # 4. Use cases
    clear_uc = ClearUseCase(state, presenter)
    input_digit_uc = InputDigitUseCase(state, presenter)
    input_decimal_uc = InputDecimalUseCase(state, presenter)
    input_operator_uc = InputOperatorUseCase(state, presenter)
    calculate_result_uc = CalculateResultUseCase(state, presenter)

    # 5. Controller
    controller = CalculatorController(
        input_digit_use_case=input_digit_uc,
        input_operator_use_case=input_operator_uc,
        input_decimal_use_case=input_decimal_uc,
        calculate_result_use_case=calculate_result_uc,
        clear_use_case=clear_uc,
    )

    # 6. View — fully assembled on construction, no two-phase init needed
    view = CalculatorView(window=window, controller=controller, display_var=display_var)
    view.start()


if __name__ == "__main__":
    main()
