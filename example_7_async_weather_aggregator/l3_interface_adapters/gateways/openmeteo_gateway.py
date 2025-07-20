import httpx
from l1_entities.weather_report import WeatherReport
from l2_use_cases.boundaries.i_weather_gateway import IWeatherGateway


class OpenMeteoGateway(IWeatherGateway):
    """
    A gateway to fetch weather data from the Open-Meteo API.
    """

    GEOCODING_API_URL = "https://geocoding-api.open-meteo.com/v1/search"
    WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"

    async def _get_coordinates(self, city: str) -> tuple[float, float]:
        """Fetches latitude and longitude for a given city."""
        params = {"name": city, "count": 1}
        async with httpx.AsyncClient() as client:
            response = await client.get(self.GEOCODING_API_URL, params=params)
            response.raise_for_status()
            data = response.json()
            if not data.get("results"):
                raise ValueError(f"Could not find coordinates for city: {city}")
            location = data["results"][0]
            return location["latitude"], location["longitude"]

    async def fetch_weather(self, city: str) -> WeatherReport:
        """
        Fetches weather data for a given city from Open-Meteo.
        """
        latitude, longitude = await self._get_coordinates(city)

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,weather_code,cloud_cover,rain,showers,snowfall"
                ",apparent_temperature,relative_humidity_2m,is_day,precipitation"
            ),
            "format": "json",
            "timeformat": "unixtime",
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(self.WEATHER_API_URL, params=params)
            response.raise_for_status()
            data = response.json()

            current = data["current"]
            return WeatherReport(
                source="Open-Meteo",
                city=city,
                temperature=current["temperature_2m"],
                conditions=self._map_weather_code_to_conditions(current["weather_code"]),
                humidity=current["relative_humidity_2m"],
                apparent_temperature=current["apparent_temperature"],
                rain=current["rain"],
                snowfall=current["snowfall"],
                cloud_cover=current["cloud_cover"],
                is_day=bool(current["is_day"]),
            )

    def _map_weather_code_to_conditions(self, code: int) -> str:
        """Maps WMO weather codes to human-readable conditions (simplified)."""
        code_map = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            77: "Snow grains",
            95: "Thunderstorm",
        }
        drizzle = {51, 53, 55}
        freezing_drizzle = {56, 57}
        rain = {61, 63, 65}
        freezing_rain = {66, 67}
        snow_fall = {71, 73, 75}
        rain_showers = {80, 81, 82}
        snow_showers = {85, 86}
        thunderstorm_hail = {96, 99}

        if code in code_map:
            return code_map[code]
        if code in drizzle:
            return "Drizzle"
        if code in freezing_drizzle:
            return "Freezing Drizzle"
        if code in rain:
            return "Rain"
        if code in freezing_rain:
            return "Freezing Rain"
        if code in snow_fall:
            return "Snow fall"
        if code in rain_showers:
            return "Rain showers"
        if code in snow_showers:
            return "Snow showers"
        if code in thunderstorm_hail:
            return "Thunderstorm with hail"
        return "Unknown"
