import tkinter as tk

from l2_use_cases.boundaries.i_calculator_presenter import ICalculatorPresenter


class CalculatorPresenter(ICalculatorPresenter):
    """
    A concrete implementation of the presenter boundary for a Tkinter GUI.

    This class adapts the data from the use cases for display in the UI.
    It depends on the ICalculatorPresenter interface from the use cases layer,
    adhering to the Dependency Rule.
    """

    def __init__(self, display_var: tk.StringVar):
        self._display_var = display_var

    def present_update(self, display_value: str):
        """
        Updates the Tkinter display variable with the new value.
        """
        self._display_var.set(display_value)
