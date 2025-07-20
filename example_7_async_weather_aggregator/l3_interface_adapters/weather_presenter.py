from collections.abc import Callable

from l1_entities.weather_report import WeatherReport
from l2_use_cases.boundaries.i_weather_presenter import IWeatherPresenter


class WeatherPresenter(IWeatherPresenter):
    """
    Presents weather data to the GUI by invoking a callback function.
    """

    def __init__(self, view_update_callback: Callable[[str], None]):
        self._view_update_callback = view_update_callback

    def present_weather_data(self, reports: list[WeatherReport]):
        """
        Formats and presents the aggregated weather data.
        """
        if not reports:
            self.present_error("No weather data available.")
            return

        formatted_string = ""
        for report in reports:
            formatted_string += f"Source: {report.source}\n"
            formatted_string += f"  City: {report.city}\n"
            formatted_string += f"  Conditions: {report.conditions}\n"
            formatted_string += f"  Temperature: {report.temperature}°C\n"
            if report.apparent_temperature is not None:
                formatted_string += f"  Apparent Temperature: {report.apparent_temperature}°C\n"
            if report.humidity is not None:
                formatted_string += f"  Humidity: {report.humidity}%\n"
            if report.cloud_cover is not None:
                formatted_string += f"  Cloud Cover: {report.cloud_cover}%\n"
            if report.rain is not None:
                formatted_string += f"  Rain: {report.rain}mm\n"
            if report.snowfall is not None:
                formatted_string += f"  Snowfall: {report.snowfall}cm\n"
            if report.is_day is not None:
                day_or_night = "Day" if report.is_day else "Night"
                formatted_string += f"  Time of Day: {day_or_night}\n"
            formatted_string += "\n"

        self._view_update_callback(formatted_string)

    def present_error(self, message: str):
        """
        Presents an error message.
        """
        self._view_update_callback(f"Error: {message}")

    def present_loading_state(self):
        """
        Presents a loading state.
        """
        self._view_update_callback("Loading weather data...")
