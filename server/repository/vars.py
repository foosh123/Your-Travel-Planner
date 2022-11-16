from repository.auth_repo import AuthRepository
from repository.locations_repo import LocationRepository
from repository.user_repo import UserRepository


# Variables available for higher layers
# TODO: give this file a better name
auth_repo: AuthRepository = AuthRepository()
user_repo: UserRepository = UserRepository()
location_repo: LocationRepository = LocationRepository()
