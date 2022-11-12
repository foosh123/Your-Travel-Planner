from starlite import Starlite, get

from controllers.locations import LocationController

app = Starlite(
    route_handlers=[LocationController]
)


# @get("/")
# def index() -> str:
#     return "Hello World!"
# app = Starlite(route_handlers=[index])
