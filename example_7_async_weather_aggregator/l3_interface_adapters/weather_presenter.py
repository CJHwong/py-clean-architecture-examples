from collections.abc import Callable

from l1_entities.weather_report import WeatherReport
from l2_use_cases.boundaries.i_weather_presenter import IWeatherPresenter


class WeatherPresenter(IWeatherPresenter):
    """
    Presents weather data to the GUI via injected callbacks.

    Call connect() after the view is created to wire the real GUI methods.
    """

    def __init__(self):
        self._view_update_callback: Callable[[str], None] = lambda text: None
        self._set_loading_callback: Callable[[bool], None] = lambda is_loading: None

    def connect(
        self,
        view_update_callback: Callable[[str], None],
        set_loading_callback: Callable[[bool], None],
    ) -> None:
        self._view_update_callback = view_update_callback
        self._set_loading_callback = set_loading_callback

    def present_weather_data(self, reports: list[WeatherReport]) -> None:
        self._set_loading_callback(False)
        if not reports:
            self.present_error("No weather data available.")
            return

        lines = []
        for report in reports:
            lines.append(f"Source: {report.source}")
            lines.append(f"  City: {report.city}")
            lines.append(f"  Conditions: {report.conditions}")
            lines.append(f"  Temperature: {report.temperature}°C")
            if report.apparent_temperature is not None:
                lines.append(f"  Apparent Temperature: {report.apparent_temperature}°C")
            if report.humidity is not None:
                lines.append(f"  Humidity: {report.humidity}%")
            if report.cloud_cover is not None:
                lines.append(f"  Cloud Cover: {report.cloud_cover}%")
            if report.rain is not None:
                lines.append(f"  Rain: {report.rain}mm")
            if report.snowfall is not None:
                lines.append(f"  Snowfall: {report.snowfall}cm")
            if report.is_day is not None:
                lines.append(f"  Time of Day: {'Day' if report.is_day else 'Night'}")
            lines.append("")

        self._view_update_callback("\n".join(lines))

    def present_error(self, message: str) -> None:
        self._set_loading_callback(False)
        self._view_update_callback(f"Error: {message}")

    def present_loading_state(self) -> None:
        self._set_loading_callback(True)
