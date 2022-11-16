from logic.classes import User as UserEntity
from repository.base_repo import BaseRepository
from repository.entity_model_mappers import unconfirmed_user_model_to_user_model, user_entity_to_user_model, user_model_to_entity
from repository.models import User as UserModel, UnconfirmedUser as UnconfirmedUserModel

from sqlalchemy.orm import Session
from uuid import UUID

class UserRepository(BaseRepository):
    """
    Repository to handle users (both confirmed and unconfirmed)
    """

    def __init__(self):
        self.session: Session = BaseRepository.session

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

    def get_all_users(self) -> list[UserEntity]:
        """Get all users"""
        user_models: list[UserModel] = self.session.query(UserModel).all()
        user_entities: list[UserEntity] = [user_model_to_entity(user_model) for user_model in user_models]
        return user_entities

    @BaseRepository.commit_after
    def delete_user(self, user_uuid: UUID) -> None:
        """Delete a user"""
        user_model: UserModel | None = self.session.query(UserModel).filter_by(id=user_uuid).first()
        if user_model is not None:
            self.session.delete(user_model)

    def get_all_unconfirmed_users(self) -> list[UserEntity]:
        """Get all unconfirmed users"""
        unconfirmed_user_models: list[UnconfirmedUserModel] = self.session.query(UnconfirmedUserModel).all()
        user_models: list[UserModel] = [unconfirmed_user_model_to_user_model(uu_model) for uu_model in unconfirmed_user_models]
        user_entities: list[UserEntity] = [user_model_to_entity(user_model) for user_model in user_models]
        return user_entities

    @BaseRepository.commit_after
    def delete_unconfirmed_user(self, user_uuid: UUID) -> None:
        """Delete an unconfirmed user"""
        uu_model: UnconfirmedUserModel | None = self.session.query(UnconfirmedUserModel).filter_by(id=user_uuid).first()
        if uu_model is not None:
            self.session.delete(uu_model)

    @BaseRepository.commit_after
    def update_user(self, user_entity: UserEntity) -> None:

        old_user_data: UserModel = self.session.query(UserModel).filter_by(id=user_entity.id).first()
        self.session.delete(old_user_data)

        new_user_data: UserModel = user_entity_to_user_model(user_entity)
        self.session.add(new_user_data)
