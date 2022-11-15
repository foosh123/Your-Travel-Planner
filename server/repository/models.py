from sqlalchemy import Column, LargeBinary, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Location(Base):
    __tablename__ = "Location"
    id = Column(UUID(as_uuid=True), primary_key=True)
    country = Column(String)
    city = Column(String)
    location_name = Column(String)
    location_address = Column(String)

class User(Base):
    __tablename__ = "User"
    id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(String)
    password = Column(LargeBinary)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    country_of_residence = Column(String)

class UnconfirmedUser(Base):
    __tablename__ = "UnconfirmedUser"
    id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(String)
    password = Column(LargeBinary)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    country_of_residence = Column(String)
