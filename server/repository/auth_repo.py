from logic.classes import User as UserEntity
from repository.base_repo import BaseRepository
from repository.entity_model_mappers import user_entity_to_model, user_model_to_entity
from repository.models import User as UserModel

from sqlalchemy.orm import Session
from uuid import UUID

class AuthRepository(BaseRepository):
    """
    Repository for authentication purposes
    """

    def __init__(self):
        self.session: Session = BaseRepository.session

    @BaseRepository.commit_after
    def add_user(self, user: UserEntity) -> None:
        """Add a user to the database"""
        user_model: UserModel = user_entity_to_model(user)
        self.session.add(user_model)

    def get_user_by_uuid(self, user_id: UUID) -> UserEntity | None:
        """Get a user by its UUID"""
        user_model: UserModel | None = self.session.query(UserModel).filter_by(id=user_id).first()
        if user_model is None:
            return None

        user_entity: UserEntity = user_model_to_entity(user_model)
        return user_entity

    def get_user_by_username(self, username: str) -> UserEntity | None:
        """Get a user by its username"""
        user_model: UserModel | None = self.session.query(UserModel).filter_by(username=username).first()
        if user_model is None:
            return None

        user_entity: UserEntity = user_model_to_entity(user_model)
        return user_entity

    def get_user_by_email(self, email: str) -> UserEntity | None:
        """Get a user by its email"""
        user_model: UserModel | None = self.session.query(UserModel).filter_by(email=email).first()
        if user_model is None:
            return None

        user_entity: UserEntity = user_model_to_entity(user_model)
        return user_entity
