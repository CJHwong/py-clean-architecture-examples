from abc import ABC, abstractmethod

from l1_entities.weather_report import WeatherReport


class IWeatherGateway(ABC):
    """
    Abstract base class for a weather gateway, defining the interface for fetching weather data.
    """

    @abstractmethod
    async def fetch_weather(self, city: str) -> WeatherReport:
        """
        Fetches weather data for a given city.

        Args:
            city: The name of the city.

        Returns:
            A WeatherReport object containing the weather data.
        """
        pass
