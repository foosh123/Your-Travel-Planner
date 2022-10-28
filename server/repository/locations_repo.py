from repository.base_repo import BaseRepository
from repository.models import Location

from sqlalchemy.orm import Session

class LocationRepository(BaseRepository):

    def __init__(self):
        self.session: Session = BaseRepository.session

    def get_all_locations(self) -> list[Location]:
        """Return all locations from the database"""
        locations = self.session.query(Location).all()
        return locations

    @BaseRepository.commit_after
    def add_location(self, location: Location) -> None:
        """Add a location to the database"""
        self.session.add(location)

    @BaseRepository.commit_after
    def delete_location(self, location_id: int) -> None:
        """Delete a location from the database"""
        self.session.query(Location).filter(Location.id == location_id).delete()

