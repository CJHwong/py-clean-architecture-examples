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
    """
    The Composition Root.

    This is where the application is assembled. It instantiates all the
    necessary objects and injects the dependencies.
    """
    # 1. Create the core state entity
    state = CalculatorState()

    # 2. Create the GUI View and its display variable
    # The view is created first to get the tk.StringVar
    # which the presenter needs.
    # Note: We pass a dummy controller for now.
    view = CalculatorView(controller=None)
    display_var = view.display_var

    # 3. Create the Presenter (Interface Adapter)
    presenter = CalculatorPresenter(display_var)

    # 4. Create Use Cases (Application Logic)
    # Inject the state and the presenter into each use case
    clear_uc = ClearUseCase(state, presenter)
    input_digit_uc = InputDigitUseCase(state, presenter)
    input_decimal_uc = InputDecimalUseCase(state, presenter)
    input_operator_uc = InputOperatorUseCase(state, presenter)
    calculate_result_uc = CalculateResultUseCase(state, presenter)

    # 5. Create the Controller (Interface Adapter)
    # Inject all the use cases into the controller
    controller = CalculatorController(
        input_digit_use_case=input_digit_uc,
        input_operator_use_case=input_operator_uc,
        input_decimal_use_case=input_decimal_uc,
        calculate_result_use_case=calculate_result_uc,
        clear_use_case=clear_uc,
    )

    # 6. Assign the fully-configured controller to the view
    view._controller = controller

    # 7. Start the application
    view.start()


if __name__ == "__main__":
    main()
