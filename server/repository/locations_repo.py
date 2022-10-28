from dotenv import load_dotenv, find_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from repository.models import Location


load_dotenv(find_dotenv())
POSTGRES_USER: str = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
POSTGRES_CONTAINER_PORT: int = int(os.getenv("POSTGRES_CONTAINER_PORT"))
DB_NAME: str = os.getenv("DB_NAME")
DATABASE_URI: str = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:{POSTGRES_CONTAINER_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


class LocationRepository:

    def get_all_locations(self) -> list[Location]:
        """Return all locations from the database"""
        session = Session()
        locations = session.query(Location).all()
        session.close()
        return locations

    def add_location(self, location: Location) -> None:
        """Add a location to the database"""
        session = Session()
        session.add(location)
        session.commit()
        session.close()
