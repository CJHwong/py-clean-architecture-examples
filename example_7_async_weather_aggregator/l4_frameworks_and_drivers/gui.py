import tkinter as tk
from tkinter import ttk

from l3_interface_adapters.weather_controller import WeatherController


class WeatherApp:
    """
    The main GUI for the Weather Aggregator application.
    """

    def __init__(self, root: tk.Tk, controller: WeatherController, available_services: list[str]):
        self._root = root
        self._controller = controller
        self._available_services = available_services
        self._root.title("Async Weather Aggregator")

        self._create_widgets()

    def _create_widgets(self):
        """Creates and places the widgets in the main window."""
        main_frame = ttk.Frame(self._root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # --- Input Widgets ---
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E))

        ttk.Label(input_frame, text="City:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self._city_entry = ttk.Entry(input_frame, width=20)
        self._city_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
        self._city_entry.insert(0, "New York")

        ttk.Label(input_frame, text="Service:").grid(row=0, column=2, sticky=tk.W, padx=(10, 5))
        self._service_selection = ttk.Combobox(input_frame, values=self._available_services, width=15)
        self._service_selection.grid(row=0, column=3, sticky=tk.W)
        if self._available_services:
            self._service_selection.current(0)

        self._fetch_button = ttk.Button(input_frame, text="Fetch Weather", command=self._fetch_weather)
        self._fetch_button.grid(row=0, column=4, sticky=tk.E, padx=(10, 0))

        # --- Results Display ---
        self._results_text = tk.Text(main_frame, wrap=tk.WORD, height=15, width=70)
        self._results_text.grid(row=1, column=0, columnspan=5, pady=(10, 0))
        self._results_text.config(state=tk.DISABLED)

    def _fetch_weather(self):
        """
        Handles the button click to fetch weather data.
        """
        city = self._city_entry.get()
        service = self._service_selection.get()
        if city and service:
            self._controller.get_weather(city, [service])

    def update_display(self, text: str):
        """
        Updates the results display with the given text.
        This method is intended to be called by the presenter.
        """
        self._results_text.config(state=tk.NORMAL)
        self._results_text.delete("1.0", tk.END)
        self._results_text.insert(tk.END, text)
        self._results_text.config(state=tk.DISABLED)

    def set_loading_state(self, is_loading: bool):
        """
        Enables or disables the fetch button to indicate loading status.
        """
        if is_loading:
            self._fetch_button.config(state=tk.DISABLED)
            self.update_display("Loading weather data...")
        else:
            self._fetch_button.config(state=tk.NORMAL)
