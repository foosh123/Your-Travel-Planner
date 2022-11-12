from logic.classes import Location
from logic.locations_methods import get_locations

from starlite import Controller, get

class LocationController(Controller):
    path = "/locations"

    @get()
    async def list_locations(self) -> list[Location]:
        return get_locations()
