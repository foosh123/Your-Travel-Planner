from logic.classes import User as UserEntity
from repository.base_repo import BaseRepository
from repository.entity_model_mappers import user_entity_to_unconfirmed_user_model, unconfirmed_user_model_to_user_model
from repository.models import User as UserModel, UnconfirmedUser as UnconfirmedUserModel

from sqlalchemy.orm import Session
from uuid import UUID

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
