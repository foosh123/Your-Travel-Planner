from dotenv import load_dotenv, find_dotenv
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date


load_dotenv(find_dotenv())
POSTGRES_USER: str = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
POSTGRES_CONTAINER_PORT: int = int(os.getenv("POSTGRES_CONTAINER_PORT"))
DB_NAME: str = os.getenv("DB_NAME")
DATABASE_URI: str = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:{POSTGRES_CONTAINER_PORT}/{DB_NAME}"

Base = declarative_base()


class Locations(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)
    location_name = Column(String)
    location_address = Column(String)


if __name__ == '__main__':
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)
