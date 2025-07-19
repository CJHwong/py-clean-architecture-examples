# Example 6: Tkinter GUI Calculator

This example demonstrates the Clean Architecture pattern in a simple, reactive GUI application using Python's built-in Tkinter library.

The goal is to show how the core application logic can be completely decoupled from the UI, allowing for a reactive data flow where the UI updates in response to changes in the application's state, without the core logic knowing anything about the UI framework.

## Architecture

The application is structured into the four standard layers:

- **`l1_entities`**: Contains the `CalculatorState` data class, which represents the core state of the application.
- **`l2_use_cases`**: Holds all the business logic for calculator operations (`InputDigitUseCase`, `CalculateResultUseCase`, etc.). It also defines the `ICalculatorPresenter` boundary interface for sending data outwards.
- **`l3_interface_adapters`**: Includes the `CalculatorController` to handle GUI events and the `CalculatorPresenter` which implements the output boundary to update the display.
- **`l4_frameworks_and_drivers`**: Contains the `gui.py` file with all the Tkinter-specific code for building and rendering the user interface.

## How to Run

To run the calculator application, execute the following command from the root directory of the repository:

```bash
python main.py
```

This will launch the graphical calculator window.
