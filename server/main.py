from starlite import Starlite, CORSConfig

from controllers.index import TestController
from controllers.locations import LocationController

app = Starlite(
    route_handlers=[TestController, LocationController],
    cors_config=CORSConfig(
        allow_origins=["https://ytp-frontend.onrender.com/"],  # to abstract out
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )
)
