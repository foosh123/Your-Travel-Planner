
from repository.models import Location as LocationORM, User as UserORM, UnconfirmedUser as UnconfirmedUserORM
from logic.classes import Location as LocationEntity, User as UserEntity

def model_to_dict(model_obj):
    model_dict = model_obj.__dict__
    model_dict.pop('_sa_instance_state')
    return model_dict

# ================== Location ==================

def location_model_to_entity(location_orm_obj: LocationORM) -> LocationEntity:
    return LocationEntity.from_orm(location_orm_obj)
    # return LocationEntity(
    #     id=location_orm_obj.id,
    #     country=location_orm_obj.country,
    #     city=location_orm_obj.city,
    #     location_name=location_orm_obj.location_name,
    #     location_address=location_orm_obj.location_address
    # )

def location_entity_to_model(location_model_obj: LocationEntity) -> LocationORM:
    return LocationORM(**location_model_obj.dict())

# ================== Auth ==================

def user_model_to_entity(user_orm_obj: UserORM) -> UserEntity:
    user_entity_details: dict = model_to_dict(user_orm_obj)
    return UserEntity(**user_entity_details)

def user_entity_to_user_model(user_model_obj: UserEntity) -> UserORM:
    return UserORM(**user_model_obj.dict())

def user_entity_to_unconfirmed_user_model(user_model_obj: UserEntity) -> UnconfirmedUserORM:
    return UnconfirmedUserORM(**user_model_obj.dict())

def unconfirmed_user_model_to_user_model(unconfirmed_user_model_obj: UnconfirmedUserORM) -> UserORM:
    unconfirmed_user_entity_details: dict = model_to_dict(unconfirmed_user_model_obj)
    return UserORM(**unconfirmed_user_entity_details)
