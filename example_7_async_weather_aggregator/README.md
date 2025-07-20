# Example 7: Async Weather Aggregator

This example demonstrates an asynchronous GUI application for fetching weather data from multiple sources concurrently.

## Core Concepts

- **Asynchronous Operations:** Uses `asyncio` and `httpx` to perform non-blocking I/O for fetching data.
- **GUI:** Built with `tkinter`, Python's standard GUI library.
- **Clean Architecture:** The code is structured into four layers (Entities, Use Cases, Interface Adapters, Frameworks & Drivers) to maintain separation of concerns.
- **Dependency Injection:** The `main.py` script wires together the different components of the application.

## How to Run

1. **Install Dependencies:**
    Navigate to this directory in your terminal and install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Application:**
    Execute the `main.py` script:

    ```bash
    python main.py
    ```

    A `tkinter` window should appear. You can then enter a city name and click "Fetch Weather" to see the (mocked) asynchronous data fetching in action.
