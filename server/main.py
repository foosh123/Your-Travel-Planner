from starlite import Starlite, CORSConfig
from starlite.middleware.base import DefineMiddleware

from controllers.auth_controller import AuthController, JWTAuthenticationMiddleWare
from controllers.index import TestController
from controllers.location_controller import LocationController
from exceptions.starlite_exception_handlers import exception_handler_map

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

FRONTEND_URL: str
if os.getenv("ENVIRONMENT") == "development":
    FRONTEND_URL = os.getenv("DEV_FRONTEND_URL")
else:
    FRONTEND_URL = os.getenv("PROD_FRONTEND_URL")



# Can optionally exclude certain paths from authentication.
# the following excludes all routes mounted at or under `/schema*`
auth_middleware = DefineMiddleware(JWTAuthenticationMiddleWare, exclude="schema")


app = Starlite(
    route_handlers=[AuthController, TestController, LocationController],
    exception_handlers=exception_handler_map,
    cors_config=CORSConfig(
        allow_origins=["*"],  # temp fix
        # allow_origins=[FRONTEND_URL],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    ),
    middleware=[auth_middleware],
)
