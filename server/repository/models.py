from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class Location(Base):
    __tablename__ = 'Location'
    id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)
    location_name = Column(String)
    location_address = Column(String)
