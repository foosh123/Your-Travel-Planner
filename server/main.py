from starlite import Starlite, CORSConfig
from starlite.middleware.base import DefineMiddleware

from controllers.auth_controller import AuthController, JWTAuthenticationMiddleWare
from controllers.index import TestController
from controllers.location_controller import LocationController
from controllers.user_controller import UserController
from exceptions.starlite_exception_handlers import exception_handler_map
from env_vars import FRONTEND_URL


# Can optionally exclude certain paths from authentication.
# the following excludes all routes mounted at or under `/schema*`
auth_middleware = DefineMiddleware(JWTAuthenticationMiddleWare, exclude="schema")


app = Starlite(
    route_handlers=[AuthController, LocationController, TestController, UserController],
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
