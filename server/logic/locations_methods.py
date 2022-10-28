from repository.locations_repo import LocationRepository
from repository.models import Location as LocationORM
from logic.classes import Location as LocationModel


def get_locations() -> list[LocationModel]:
    locations: list[LocationORM] = LocationRepository().get_all_locations()
    locations_models: list[LocationModel] = [LocationModel.from_orm(location) for location in locations]
    return locations_models


def add_single_location(location_model_obj: LocationModel) -> None:

    location_orm_obj: LocationORM = LocationORM(**location_model_obj.dict())
    LocationRepository().add_location(location_orm_obj)

