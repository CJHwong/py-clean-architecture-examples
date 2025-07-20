import asyncio

from l2_use_cases.boundaries.i_weather_gateway import IWeatherGateway
from l2_use_cases.boundaries.i_weather_presenter import IWeatherPresenter


class GetWeatherUseCase:
    """
    Use case for fetching and aggregating weather data from multiple sources.
    """

    def __init__(self, gateways: dict[str, IWeatherGateway], presenter: IWeatherPresenter):
        self._gateways = gateways
        self._presenter = presenter

    async def execute(self, city: str, service_names: list[str]):
        """
        Executes the use case to fetch weather data for a given city from the selected services.

        Args:
            city: The name of the city.
            service_names: A list of names of the services to use.
        """
        self._presenter.present_loading_state()

        gateways_to_use = [self._gateways[name] for name in service_names if name in self._gateways]

        if not gateways_to_use:
            self._presenter.present_error("No valid weather service selected.")
            return

        try:
            tasks = [gateway.fetch_weather(city) for gateway in gateways_to_use]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            successful_reports = [res for res in results if not isinstance(res, Exception)]

            if successful_reports:
                self._presenter.present_weather_data(successful_reports)
            else:
                # You might want to log the actual exceptions in a real application
                self._presenter.present_error("Failed to fetch weather data from the selected source(s).")

        except Exception as e:
            self._presenter.present_error(f"An unexpected error occurred: {e}")
