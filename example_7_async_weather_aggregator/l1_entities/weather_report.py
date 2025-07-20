from dataclasses import dataclass


@dataclass
class WeatherReport:
    """Represents a weather report from a single source."""

    source: str
    city: str
    temperature: float
    conditions: str
    humidity: int | None = None
    apparent_temperature: float | None = None
    rain: float | None = None
    snowfall: float | None = None
    cloud_cover: int | None = None
    is_day: bool | None = None
