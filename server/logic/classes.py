from pydantic import BaseModel
from uuid import UUID

class ORMBaseModel(BaseModel):
    class Config:
        orm_mode = True

class Location(ORMBaseModel):
    id: UUID
    country: str
    city: str
    location_name: str
    location_address: str


class User(BaseModel):
    id: UUID
    username: str
    password: bytes  # salted and hashed
    email: str  # pydantic.EmailStr?
    first_name: str
    last_name: str
    country_of_residence: str
