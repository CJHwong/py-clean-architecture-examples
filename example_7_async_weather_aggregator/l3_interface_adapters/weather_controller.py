import asyncio

from l2_use_cases.get_weather_use_case import GetWeatherUseCase


class WeatherController:
    """
    Controller to link the GUI with the weather fetching use case.
    """

    def __init__(self, get_weather_use_case: GetWeatherUseCase):
        self._get_weather_use_case = get_weather_use_case
        self._background_tasks = set()

    def get_weather(self, city: str, service_names: list[str]):
        """
        Initiates the weather fetching process for the selected services.

        This method creates an asyncio task to run the use case, allowing the GUI
        to remain responsive.

        Args:
            city: The name of the city.
            service_names: A list of names of the services to use.
        """
        task = asyncio.create_task(self._get_weather_use_case.execute(city, service_names))
        self._background_tasks.add(task)
        task.add_done_callback(self._background_tasks.discard)
