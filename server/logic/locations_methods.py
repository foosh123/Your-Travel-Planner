from repository.locations_repo import LocationRepository
from repository.models import Location as LocationORM
from logic.classes import Location as LocationEntity

# ================= Repository =================

repo = LocationRepository()

# ================== Mappers ==================

def location_orm_to_entity(location_orm_obj: LocationORM) -> LocationEntity:
    return LocationEntity.from_orm(location_orm_obj)

def location_entity_to_orm(location_model_obj: LocationEntity) -> LocationORM:
    return LocationORM(**location_model_obj.dict())

# ================== Methods ==================

def get_locations() -> list[LocationEntity]:
    location_models: list[LocationORM] = repo.get_all_locations()
    locations_entities: list[LocationEntity] = [location_orm_to_entity(l) for l in location_models]
    return locations_entities

def add_location(location_obj: LocationEntity) -> None:
    location_model: LocationORM = location_entity_to_orm(location_obj)
    repo.add_location(location_model)

def delete_location(location_id: int) -> None:
    repo.delete_location(location_id)
