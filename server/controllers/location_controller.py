from logic.classes import Location
from logic.locations_logic import LocationHandler

from starlite import Controller, get

class LocationController(Controller):
    path = "/locations"

    @get(exclude_from_auth=True)
    async def get_all_locations(self) -> list[Location]:
        return LocationHandler.get_locations()
