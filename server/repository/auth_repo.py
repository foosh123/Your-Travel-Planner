from logic.classes import User as UserEntity
from repository.base_repo import BaseRepository
from repository.entity_model_mappers import user_entity_to_unconfirmed_user_model, unconfirmed_user_model_to_user_model
from repository.models import User as UserModel, UnconfirmedUser as UnconfirmedUserModel, PasswordResetRequest as PasswordResetRequestModel

from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from uuid import uuid4, UUID

RESET_CODE_EXPIRATION_TIME_IN_MINUTES: int = 30

class AuthRepository(BaseRepository):
    """
    Repository for authentication purposes
    """

    def __init__(self):
        self.session: Session = BaseRepository.session

    @BaseRepository.commit_after
    def add_unconfirmed_user(self, user: UserEntity) -> None:
        """Add a user to the database, but mark it as unconfirmed"""
        user_model: UserModel = user_entity_to_unconfirmed_user_model(user)
        self.session.add(user_model)

    def check_valid_unconfirmed_user(self, user_id: UUID) -> bool:
        """Check if a user is unconfirmed"""
        unconfirmed_user_model: UnconfirmedUserModel | None = self.session.query(UnconfirmedUserModel).filter_by(id=user_id).first()
        return unconfirmed_user_model is not None

    @BaseRepository.commit_after
    def confirm_user(self, user_id: UUID) -> None:
        """Confirm a user"""
        unconfirmed_user_model: UnconfirmedUserModel | None = self.session.query(UnconfirmedUserModel).filter_by(id=user_id).first()
        if unconfirmed_user_model is None:
            return None

        # delete the unconfirmed user
        self.session.delete(unconfirmed_user_model)

        # convert to user model
        user_model: UserModel = unconfirmed_user_model_to_user_model(unconfirmed_user_model)
        self.session.add(user_model)

    @BaseRepository.commit_after
    def add_password_reset_request(self, user_id: UUID) -> UUID:
        """Add a password reset request, returns a unique ID that can be used to associate to this request"""

        # Create a request
        request_id: UUID = uuid4()
        current_time: datetime = datetime.now()
        expiration_time: datetime = current_time + timedelta(minutes=RESET_CODE_EXPIRATION_TIME_IN_MINUTES)
        new_request: PasswordResetRequestModel = PasswordResetRequestModel(
            id=request_id,
            user_id=user_id,
            reset_code_expiration=expiration_time
        )

        # Add the request
        self.session.add(new_request)

        # Return the request ID
        return request_id

    def check_valid_password_reset_request(self, request_id: UUID) -> bool:
        """Check if a password reset request is valid"""

        result: PasswordResetRequestModel | None = self.session.query(PasswordResetRequestModel).filter_by(id=request_id).first()
        if result is None:
            return False

    def get_user_id_from_reset_token(self, request_id: UUID) -> UUID:
        """Get the user ID from a password reset token"""

        result: PasswordResetRequestModel | None = self.session.query(PasswordResetRequestModel).filter_by(id=request_id).first()
        if result is None:
            return None

        return result.user_id


    @BaseRepository.commit_after
    def delete_password_reset_request(self, request_id: UUID) -> None:
        """Delete a password reset request"""

        result: PasswordResetRequestModel | None = self.session.query(PasswordResetRequestModel).filter_by(id=request_id).first()
        if result is None:
            return None

        self.session.delete(result)
