import tkinter as tk

from async_tkinter_loop import async_mainloop
from l2_use_cases.get_weather_use_case import GetWeatherUseCase
from l3_interface_adapters.gateways.mock_weather_gateways import MockWeatherGateway
from l3_interface_adapters.gateways.openmeteo_gateway import OpenMeteoGateway
from l3_interface_adapters.weather_controller import WeatherController
from l3_interface_adapters.weather_presenter import WeatherPresenter
from l4_frameworks_and_drivers.gui import WeatherApp


def main():
    """
    Main function to set up and run the weather aggregator application.
    """
    # --- Dependency Injection ---

    # 1. Create Gateways
    gateways = {
        "Mock Service": MockWeatherGateway(),
        "Open-Meteo": OpenMeteoGateway(),
    }

    # 2. Create the GUI
    root = tk.Tk()

    # 3. Create Presenter
    def placeholder_update(text):
        print(f"Placeholder update: {text}")

    presenter = WeatherPresenter(placeholder_update)

    # 4. Create Use Case
    get_weather_use_case = GetWeatherUseCase(gateways, presenter)

    # 5. Create Controller
    controller = WeatherController(get_weather_use_case)

    # 6. Create the App, passing in the available services
    app = WeatherApp(root, controller, list(gateways.keys()))

    # 7. Connect the presenter to the actual GUI update method
    presenter._view_update_callback = app.update_display

    # --- Run the application ---
    async_mainloop(root)


if __name__ == "__main__":
    main()
