import asyncio
import random

from l1_entities.weather_report import WeatherReport
from l2_use_cases.boundaries.i_weather_gateway import IWeatherGateway


class MockWeatherGateway(IWeatherGateway):
    """
    A mock weather gateway for Source A.
    """

    async def fetch_weather(self, city: str) -> WeatherReport:
        """
        Simulates fetching weather data from Source A.
        """
        # Simulate network latency
        await asyncio.sleep(random.uniform(0.5, 1.5))  # noqa: S311
        return WeatherReport(
            source="Source A",
            city=city,
            temperature=round(random.uniform(15.0, 25.0), 1),  # noqa: S311
            humidity=random.randint(40, 60),  # noqa: S311
            conditions="Sunny",
        )
