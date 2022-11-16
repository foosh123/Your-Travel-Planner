from logic.classes import User
from logic.user_logic import UserHandler

from starlite import Controller, get, delete

class UserController(Controller):
    path = "/users"

    @get(exclude_from_auth=True)
    async def get_all_users(self) -> list[User]:
        all_users: list[User] = UserHandler.get_all_users()
        return [user.to_json_safe_dict() for user in all_users]

    @delete(path="/{user_id: str}", exclude_from_auth=True)
    async def delete_user(self, user_id: str) -> None:
        UserHandler.delete_user(user_id)

    @get(path="/unconfirmed", exclude_from_auth=True)
    async def get_all_unconfirmed_users(self) -> list[User]:
        unconfirmed_users: list[User] = UserHandler.get_all_unconfirmed_users()
        return [user.to_json_safe_dict() for user in unconfirmed_users]

    @delete(path="/unconfirmed/{user_id: str}", exclude_from_auth=True)
    async def delete_unconfirmed_user(self, user_id: str) -> None:
        UserHandler.delete_unconfirmed_user(user_id)
