from abc import ABC, abstractmethod

from l1_entities.weather_report import WeatherReport


class IWeatherPresenter(ABC):
    """
    Abstract base class for a weather presenter, defining the interface for presenting weather data.
    """

    @abstractmethod
    def present_weather_data(self, reports: list[WeatherReport]):
        """
        Presents the aggregated weather data.

        Args:
            reports: A list of WeatherReport objects.
        """
        pass

    @abstractmethod
    def present_error(self, message: str):
        """
        Presents an error message.

        Args:
            message: The error message to present.
        """
        pass

    @abstractmethod
    def present_loading_state(self):
        """
        Presents a loading state, indicating that data is being fetched.
        """
        pass
