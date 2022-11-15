from datetime import datetime, timedelta
import jwt
from pydantic import BaseModel
import time
from uuid import UUID

from env_vars import SECRET_KEY, DEFAULT_TIME_DELTA
from exceptions.exceptions import InvalidJWTException


# https://auth0.com/blog/how-to-handle-jwt-in-python/

class JWTToken(BaseModel):
    user_id: str

    # time created in epoch time
    time_created: float

    # expiry in epoch time
    expiry: float

    def is_expired(self) -> bool:
        return self.expiry < time.time()

    @staticmethod
    def decode(encoded_jwt_token: str) -> "JWTToken":
        try:
            payload: dict[str, str | datetime] = jwt.decode(encoded_jwt_token, key=SECRET_KEY, algorithms=["HS256"])
            return JWTToken(**payload)
        except jwt.InvalidSignatureError as _:
            return InvalidJWTException("Invalid signature")

    @staticmethod
    def encode(user_id: UUID, duration_to_expiry: timedelta = DEFAULT_TIME_DELTA) -> str:
        current_time: float = time.time()
        expiry: float = current_time + duration_to_expiry.total_seconds()
        payload = {
            "user_id": str(user_id),
            "time_created": current_time,
            "expiry": expiry,
        }
        jwt_token: str = jwt.encode(payload, key=SECRET_KEY)
        return jwt_token
