from exceptions.exceptions import InvalidInputException
from logic.classes import User
from repository.vars import user_repo

from uuid import UUID

# https://stackabuse.com/hashing-passwords-in-python-with-bcrypt/


class UserHandler:

    # ================== Public Methods ==================

    @staticmethod
    def get_password_of_user(user_entity: User) -> bytes | None:
        user_model: User | None = user_repo.get_user_by_uuid(user_entity)
        if user_model is None:
            return None
        return user_model.password

    @staticmethod
    def is_email_address(input_string: str) -> bool:
        return "@" in input_string  # TODO: improve this

    @staticmethod
    def get_user_by_uuid(user_id: UUID) -> User | None:
        db_user: User | None = user_repo.get_user_by_uuid(user_id)
        return db_user

    @staticmethod
    def get_user_by_username(username: str) -> User | None:
        db_user: User | None = user_repo.get_user_by_username(username)
        return db_user

    @staticmethod
    def get_user_by_email(email: str) -> User | None:
        db_user: User | None = user_repo.get_user_by_email(email)
        return db_user

    @staticmethod
    def get_all_users() -> list[User]:
        db_users: list[User] = user_repo.get_all_users()
        return db_users

    @staticmethod
    def delete_user(user_id: str) -> None:
        try:
            user_uuid = UUID(user_id)
        except ValueError:
            raise InvalidInputException("Invalid User ID to delete")
        else:
            user_repo.delete_user(user_uuid)

    @staticmethod
    def get_all_unconfirmed_users() -> list[User]:
        db_users: list[User] = user_repo.get_all_unconfirmed_users()
        return db_users

    @staticmethod
    def delete_unconfirmed_user(user_id: str) -> None:
        try:
            user_uuid = UUID(user_id)
        except ValueError:
            raise InvalidInputException("Invalid User ID to delete")
        else:
            user_repo.delete_unconfirmed_user(user_uuid)
