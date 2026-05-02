import tkinter as tk

from async_tkinter_loop import async_mainloop
from l2_use_cases.get_weather_use_case import GetWeatherUseCase
from l3_interface_adapters.gateways.mock_weather_gateways import MockWeatherGateway
from l3_interface_adapters.gateways.openmeteo_gateway import OpenMeteoGateway
from l3_interface_adapters.weather_controller import WeatherController
from l3_interface_adapters.weather_presenter import WeatherPresenter
from l4_frameworks_and_drivers.gui import WeatherApp


def main():
    # 1. Gateways
    gateways = {
        "Mock Service": MockWeatherGateway(),
        "Open-Meteo": OpenMeteoGateway(),
    }

    # 2. Presenter (callbacks wired after the view exists)
    presenter = WeatherPresenter()

    # 3. Use Case + Controller
    get_weather_use_case = GetWeatherUseCase(gateways, presenter)
    controller = WeatherController(get_weather_use_case)

    # 4. View
    root = tk.Tk()
    app = WeatherApp(root, controller, list(gateways.keys()))

    # 5. Wire presenter to the real GUI methods now that the view exists
    presenter.connect(
        view_update_callback=app.update_display,
        set_loading_callback=app.set_loading_state,
    )

    async_mainloop(root)


if __name__ == "__main__":
    main()
