from exceptions.exceptions import InvalidInputException
from logic.helper_methods import is_valid_email_addr

from pydantic import BaseModel, validator
from zxcvbn import zxcvbn


MIN_PASSWORD_STRENGTH_SCORE = 2  # TODO: bring these out into a config file?
MIN_PASSWORD_LENGTH = 8

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


    @validator("password")
    def password_is_strong_enough(cls, v):
        password_strength = zxcvbn(v)
        if not password_strength["score"] >= MIN_PASSWORD_STRENGTH_SCORE:
            raise InvalidInputException("Password is not strong enough")
        return v

    @validator("password")
    def password_is_long_enough(cls, v):
        if len(v) < MIN_PASSWORD_LENGTH:
            raise InvalidInputException(f"Password is not long enough, must be at least {MIN_PASSWORD_LENGTH} characters")
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

class PasswordForgetPayload(BaseModel):
    email: str

class ResetPasswordPayload(BaseModel):
    request_id: str
    password: str
    password_confirm: str

    @validator("password_confirm")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise InvalidInputException("Passwords do not match")
        return v
