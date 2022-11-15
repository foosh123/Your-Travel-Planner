from controllers.auth_controller import UserCreatePayload, UserLoginPayload
from exceptions.exceptions import DataAlreadyExistsException, InvalidCredentialsException, NoSuchDataException
from logic.classes import User
from logic.helper_methods import send_account_creation_confirmation_email
from repository.auth_repo import AuthRepository

import bcrypt
from uuid import uuid4, UUID

# https://stackabuse.com/hashing-passwords-in-python-with-bcrypt/


class AuthHandler:

    repo = AuthRepository()

    # ================== Private Methods ==================
    @staticmethod
    def _user_create_payload_to_entity(user_create_dto: UserCreatePayload) -> User:

        user_entity_id: UUID = uuid4()
        raw_password: str = user_create_dto.password
        byte_password: bytes = raw_password.encode("utf-8")
        hashed_password: bytes = bcrypt.hashpw(byte_password, bcrypt.gensalt())

        return User(
            id=user_entity_id,
            username=user_create_dto.username,
            password=hashed_password,
            email=user_create_dto.email,
            first_name=user_create_dto.first_name,
            last_name=user_create_dto.last_name,
            country_of_residence=user_create_dto.country_of_residence
        )

    @staticmethod
    def _get_password_of_user(user_entity: User) -> bytes | None:
        user_model: User | None = AuthHandler._get_user_by_uuid(user_entity)
        if user_model is None:
            return None
        return user_model.password

    @staticmethod
    def _is_email_address(input_string: str) -> bool:
        return "@" in input_string  # TODO: improve this

    @staticmethod
    def _get_user_by_uuid(user_id: UUID) -> User | None:
        db_user: User | None = AuthHandler.repo.get_user_by_uuid(user_id)
        return db_user

    @staticmethod
    def _get_user_by_username(username: str) -> User | None:
        db_user: User | None = AuthHandler.repo.get_user_by_username(username)
        return db_user

    @staticmethod
    def _get_user_by_email(email: str) -> User | None:
        db_user: User | None = AuthHandler.repo.get_user_by_email(email)
        return db_user

    # ================== Public Methods ==================

    @staticmethod
    def add_unconfirmed_user(user_create_dto: UserCreatePayload) -> None:
        user_model: User = AuthHandler._user_create_payload_to_entity(user_create_dto)
        try:
            AuthHandler.repo.add_unconfirmed_user(user_model)
        except Exception as e:  # TODO: check for right exception
            print(str(e))
            raise DataAlreadyExistsException("User already exists")
        else:
            id_for_confirmation: str = str(user_model.id)
            email_for_confirmation: str = user_model.email
            send_account_creation_confirmation_email(email_for_confirmation, id_for_confirmation)

    @staticmethod
    def confirm_user(user_id: str) -> None:
        try:
            user_uuid = UUID(user_id)
        except ValueError:
            raise InvalidCredentialsException("Invalid confirmation code")
        else:
            has_unconfirmed_user: bool = AuthHandler.repo.check_valid_unconfirmed_user(user_uuid)
            if has_unconfirmed_user is False:
                raise NoSuchDataException("User does not exist")
            AuthHandler.repo.confirm_user(user_uuid)

    @staticmethod
    def get_user_by_credentials(user_login_dto: UserLoginPayload) -> User:

        username_or_email: str = user_login_dto.username_or_email
        raw_password_query: str = user_login_dto.password

        # Check if user exists
        db_user: User | None
        if AuthHandler._is_email_address(username_or_email):
            db_user = AuthHandler._get_user_by_email(username_or_email)
        else:
            db_user = AuthHandler._get_user_by_username(username_or_email)

        if db_user is None:
            raise InvalidCredentialsException("Invalid username / password")

        # If username exists, check password
        relevant_password: bytes = db_user.password

        # If password is correct, return user
        byte_password_query: bytes = raw_password_query.encode("utf-8")
        is_password_correct: bool = bcrypt.checkpw(byte_password_query, relevant_password)

        if is_password_correct is False:
            raise InvalidCredentialsException("Invalid username / password")

        return db_user
