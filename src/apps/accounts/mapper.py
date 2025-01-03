

from src.apps.accounts.serializers.auth_serializer import AuthSerializer
from src.apps.accounts.dtos.user_dto import UserDto
from src.apps.accounts.models import User
from django.db import models

class UserMapper:
    @staticmethod
    def from_dto_to_model(dto, model: models.Model, fields) -> models.Model:
        data = {field: getattr(dto, field) for field in fields}
        return model(**data)
    

    
    @staticmethod
    def from_model_to_dto(user: User) -> UserDto:
        return UserDto(
            username=user.username,
            phone=user.phone,
            email=user.email
        )
    
    @staticmethod
    def from_serializer_to_dto(dto, serializer, fields) -> UserDto:
        data = {field: serializer.data.get(field) for field in fields}
        return dto(**data)
    
    @staticmethod
    def from_dto_to_serialzier(user_dto: UserDto) -> AuthSerializer:
        return AuthSerializer(
            username=user_dto.username,
            phone=user_dto.phone,
            email=user_dto.email
        )
    