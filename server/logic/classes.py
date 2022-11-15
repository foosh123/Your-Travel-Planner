from pydantic import BaseModel
from typing import Any
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

    def to_json_safe_dict(self) -> dict[str, Any]:
        details: dict[str, Any] = self.dict()

        # convert UUID to string
        details["id"] = str(details["id"])

        # drop password
        details.pop("password")

        return details
