from starlite import Starlite
# from starlite.config.cors import CORSConfig

from controllers.index import TestController
from controllers.locations import LocationController

app = Starlite(
    route_handlers=[TestController, LocationController],
    # cors_config=CORSConfig(
    #     allow_origins=["localhost:8080"],  # to abstract out
    # )
)
