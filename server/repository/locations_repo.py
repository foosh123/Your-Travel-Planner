from logic.classes import Location as LocationEntity
from repository.base_repo import BaseRepository
from repository.entity_model_mappers import location_entity_to_model, location_model_to_entity
from repository.models import Location as LocationModel

from sqlalchemy.orm import Session

class LocationRepository(BaseRepository):
    """
    Repository for the Location table
    """

    def __init__(self):
        self.session: Session = BaseRepository.session

    def get_all_locations(self) -> list[LocationEntity]:
        """Return all locations from the database"""
        location_models: list[LocationModel] = self.session.query(LocationModel).all()
        location_entities: list[LocationEntity] = [location_model_to_entity(l) for l in location_models]
        return location_entities

    @BaseRepository.commit_after
    def add_location(self, location: LocationEntity) -> None:
        """Add a location to the database"""
        location_model: LocationModel = location_entity_to_model(location)
        self.session.add(location_model)

    @BaseRepository.commit_after
    def delete_location(self, location_id: int) -> None:
        """Delete a location from the database"""
        self.session.query(LocationModel).filter(LocationModel.id == location_id).delete()
