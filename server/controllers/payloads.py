from pydantic import BaseModel

class UserCreatePayload(BaseModel):
    username: str
    email: str
    password: str
    password_confirm: str
    first_name: str
    last_name: str
    country_of_residence: str

class UserLoginPayload(BaseModel):
    username_or_email: str
    password: str
