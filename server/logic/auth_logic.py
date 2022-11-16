from controllers.auth_controller import UserCreatePayload, UserLoginPayload
from exceptions.exceptions import DataAlreadyExistsException, InvalidInputException, NoSuchDataException
from logic.classes import User
from logic.helper_methods import is_valid_email_addr, send_account_creation_confirmation_email, send_password_reset_email
from logic.user_logic import UserHandler
from repository.vars import auth_repo, user_repo

import bcrypt
from uuid import uuid4, UUID

# https://stackabuse.com/hashing-passwords-in-python-with-bcrypt/


class AuthHandler:

    # ================== Private Methods ==================
    @staticmethod
    def _hash_password(password: str) -> bytes:
        byte_password: bytes = password.encode("utf-8")
        hashed_password: bytes = bcrypt.hashpw(byte_password, bcrypt.gensalt())
        return hashed_password

    @staticmethod
    def _user_create_payload_to_entity(user_create_dto: UserCreatePayload) -> User:

        user_entity_id: UUID = uuid4()
        raw_password: str = user_create_dto.password
        hashed_password: bytes = AuthHandler._hash_password(raw_password)

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
        user_model: User | None = user_repo.get_user_by_uuid(user_entity)
        if user_model is None:
            return None
        return user_model.password

    @staticmethod
    def _verify_user_name_does_not_exist(user_name: str) -> None:
        user_model: User | None = user_repo.get_user_by_username(user_name)
        if user_model is not None:
            raise DataAlreadyExistsException("User name already exists")

    @staticmethod
    def _verify_email_does_not_exist(email: str) -> None:
        user_model: User | None = user_repo.get_user_by_email(email)
        if user_model is not None:
            raise DataAlreadyExistsException("Email already exists")

    # ================== Public Methods ==================

    @staticmethod
    def add_unconfirmed_user(user_create_dto: UserCreatePayload) -> None:
        user_model: User = AuthHandler._user_create_payload_to_entity(user_create_dto)

        user_name_to_add: str = user_model.username
        email_to_add: str = user_model.email
        AuthHandler._verify_user_name_does_not_exist(user_name_to_add)
        AuthHandler._verify_email_does_not_exist(email_to_add)

        auth_repo.add_unconfirmed_user(user_model)
        id_for_confirmation: str = str(user_model.id)
        send_account_creation_confirmation_email(email_to_add, id_for_confirmation)

    @staticmethod
    def confirm_user(user_id: str) -> None:
        try:
            user_uuid: UUID = UUID(user_id)
        except ValueError:
            raise InvalidInputException("Invalid confirmation code")
        else:
            has_unconfirmed_user: bool = auth_repo.check_valid_unconfirmed_user(user_uuid)
            if has_unconfirmed_user is False:
                raise NoSuchDataException("User does not exist")
            auth_repo.confirm_user(user_uuid)

    @staticmethod
    def get_user_by_credentials(user_login_dto: UserLoginPayload) -> User:

        username_or_email: str = user_login_dto.username_or_email
        raw_password_query: str = user_login_dto.password

        # Check if user exists
        db_user: User | None
        if is_valid_email_addr(username_or_email):
            db_user = UserHandler.get_user_by_email(username_or_email)
        else:
            db_user = UserHandler.get_user_by_username(username_or_email)

        if db_user is None:
            raise InvalidInputException("Invalid username / password")

        # If username exists, check password
        relevant_password: bytes = db_user.password

        # If password is correct, return user
        byte_password_query: bytes = raw_password_query.encode("utf-8")
        is_password_correct: bool = bcrypt.checkpw(byte_password_query, relevant_password)

        if is_password_correct is False:
            raise InvalidInputException("Invalid username / password")

        return db_user

    @staticmethod
    def send_password_reset_email(email: str) -> None:
        user_model: User | None = user_repo.get_user_by_email(email)
        if user_model is None:

            # For security purposes, we don't want to tell the user if the email is not registered
            # raise NoSuchDataException("User does not exist")
            return
        
        user_id: UUID = user_model.id
        unique_reset_id: UUID = auth_repo.add_password_reset_request(user_id)
        unique_reset_id_str: str = str(unique_reset_id)
        send_password_reset_email(email, unique_reset_id_str)

    @staticmethod
    def verify_reset_token(reset_token: str) -> None:
        try:
            reset_token_uuid: UUID = UUID(reset_token)
        except ValueError:
            raise InvalidInputException("Invalid reset token")
        else:
            is_valid_token: bool = auth_repo.check_valid_password_reset_request(reset_token_uuid)
            if is_valid_token is False:
                raise InvalidInputException("Invalid reset token")

    @staticmethod
    def reset_password(reset_token: str, new_password: str) -> None:
        try:
            reset_token_uuid: UUID = UUID(reset_token)
        except ValueError:
            raise InvalidInputException("Invalid reset token")
        else:
            is_valid_token: bool = auth_repo.check_valid_password_reset_request(reset_token_uuid)
            if is_valid_token is False:
                raise InvalidInputException("Invalid reset token")

        # Get user from reset token
        user_id: UUID = auth_repo.get_user_id_from_reset_token(reset_token_uuid)
        user_entity: User = user_repo.get_user_by_uuid(user_id)

        # Update user
        new_password: bytes = AuthHandler._hash_password(new_password)
        user_entity.password = new_password

        # Delete reset token
        auth_repo.delete_password_reset_request(reset_token_uuid)

        # Update user in database
        user_repo.update_user(user_entity)
