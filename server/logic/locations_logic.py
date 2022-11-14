from logic.classes import Location as LocationEntity
from repository.locations_repo import LocationRepository
from repository.models import Location as LocationORM


class LocationHandler:
    
    repo = LocationRepository()
    
    # ================== Private Methods ==================


    # ================== Public Methods ==================

    @staticmethod
    def get_locations() -> list[LocationEntity]:
        location_models: list[LocationORM] = LocationHandler.repo.get_all_locations()
        locations_entities: list[LocationEntity] = [LocationHandler._location_orm_to_entity(l) for l in location_models]
        return locations_entities

    @staticmethod
    def add_location(location_obj: LocationEntity) -> None:
        LocationHandler.repo.add_location(location_obj)

    def delete_location(location_id: int) -> None:
        LocationHandler.repo.delete_location(location_id)
