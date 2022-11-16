from starlite import Controller, Request, get, post
from starlite import AbstractAuthenticationMiddleware, AuthenticationResult, ASGIConnection
from typing import Any
from uuid import UUID

from controllers.jwt import JWTToken
from controllers.payloads import PasswordForgetPayload, ResetPasswordPayload, UserCreatePayload, UserLoginPayload
from env_vars import AUTHORIZATION_HEADER
from exceptions.exceptions import InvalidJWTException
from logic.auth_logic import AuthHandler
from logic.user_logic import UserHandler
from logic.classes import User


# ================= Auth logic =================

# https://starlite-api.github.io/starlite/usage/8-authentication/1-abstract-authentication-middleware/
class JWTAuthenticationMiddleWare(AbstractAuthenticationMiddleware):

    # AuthenticationResult: Pydantic model that has
    # 1) user: non-optional object representing the user, typed as Any
    # 2) auth: optional object representing the authentication, defaults to None
    async def authenticate_request(self, connection: ASGIConnection) -> AuthenticationResult:
        """
        Given request, parse JWT stored in header, retrieve user
        """

        # retrieve jwt token
        jwt_token_str: str = connection.headers.get(AUTHORIZATION_HEADER)
        if not jwt_token_str:
            return AuthenticationResult(user=None, auth=None)  # TODO: or throw exception?

        # decode token
        try:
            token: JWTToken = JWTToken.decode(jwt_token_str)
        except InvalidJWTException as _:
            return AuthenticationResult(user=None, auth=None)
        else:
            if token.is_expired():
                return AuthenticationResult(user=None, auth=None)

            # retrieve user
            user_id: UUID = token.user_id
            user: User | None = UserHandler.get_user_by_uuid(UUID(user_id))
            if user is None:
                return AuthenticationResult(user=None, auth=None)

            return AuthenticationResult(user=user, auth=token)


class AuthController(Controller):
    path = "/auth"

    @post(path="/register", exclude_from_auth=True)
    async def create_user(self, data: UserCreatePayload) -> None:
        AuthHandler.add_unconfirmed_user(data)

    @get(path="/confirm-register/{user_uuid: str}", exclude_from_auth=True)
    async def confirm_user(self, user_uuid: str) -> None:
        AuthHandler.confirm_user(user_uuid)

    @post(path="/login", exclude_from_auth=True)
    async def login(self, data: UserLoginPayload) -> dict[str, str]:
        user: User = AuthHandler.get_user_by_credentials(data)
        return {"jwt": JWTToken.encode(user.id)}

    @post(path="/forgot-password", exclude_from_auth=True)
    async def forgot_password(self, data: PasswordForgetPayload) -> None:
        AuthHandler.send_password_reset_email(data.email)

    @get(path="/verify-reset-token/{request_uuid: str}", exclude_from_auth=True)
    async def verify_reset_token(self, request_uuid: str) -> None:
        AuthHandler.verify_reset_token(request_uuid)

    @post(path="/reset-password", exclude_from_auth=True)
    async def reset_password(self, data: ResetPasswordPayload) -> None:
        AuthHandler.reset_password(data.request_id, data.password)

    @get(path="/check-authenticated")
    async def check_authenticated(self, request: Request[User, JWTToken]) -> dict[str, Any]:
        result: dict[str, Any] = {
            "is_authenticated": request.auth is not None,
            "user": {} if request.auth is None else request.user.to_json_safe_dict(),
        }
        return result

    @get(path="/check-authenticated-2")
    async def check_authenticated_2(self, request: Request[User, JWTToken]) -> bool:
        return True
