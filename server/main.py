from starlite import Starlite, CORSConfig

from controllers.index import TestController
from controllers.locations import LocationController

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

FRONTEND_URL: str
if os.getenv("ENVIRONMENT") == "development":
    FRONTEND_URL = os.getenv("DEV_FRONTEND_URL")
else:
    FRONTEND_URL = os.getenv("PROD_FRONTEND_URL")

app = Starlite(
    route_handlers=[TestController, LocationController],
    cors_config=CORSConfig(
        allow_origins=[FRONTEND_URL],
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )
)
