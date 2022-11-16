from exceptions.exceptions import InvalidInputException
from logic.helper_methods import is_valid_email_addr

from pydantic import BaseModel, validator

class UserCreatePayload(BaseModel):
    username: str
    email: str
    password: str
    password_confirm: str
    first_name: str
    last_name: str
    country_of_residence: str

    @validator("email")
    def must_be_valid_email(cls, v):
        if not is_valid_email_addr(v):
            raise InvalidInputException("Email address is invalid")
        return v

    @validator("password_confirm")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise InvalidInputException("Passwords do not match")
        return v

    @validator("*")
    def fields_not_empty(cls, v):
        if not v:
            raise InvalidInputException(f"Field cannot be empty")
        return v
    
class UserLoginPayload(BaseModel):
    username_or_email: str
    password: str
