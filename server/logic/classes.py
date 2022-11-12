from pydantic import BaseModel

class Location(BaseModel):
    id: int
    country: str
    city: str
    location_name: str
    location_address: str
    # class Config:
    #     orm_mode = True

