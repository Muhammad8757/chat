from src.apps.accounts.dtos.user_dto import LoginDto, UserDto
from src.apps.accounts.mapper import UserMapper
from src.apps.accounts.models import User
from src.apps.accounts.repositories.auth_repository import UserRespository
from django.contrib.auth import authenticate
from django.db import models


class UserService:
    def create_user(self, request, user_dto: UserDto) -> User:
        try:
            UserRespository.create_user(user_dto)
            return True
        except Exception as e:
            print(f"Ошибка при создании пользователя: {e}")
            return False
    
    def login(self, request, user_dto: LoginDto) -> User:
        user: User = UserMapper.from_dto_to_model(user_dto, User, ["username", "password"])
        authenticated_user = UserRespository.login(user=user)
        if authenticated_user:
            return authenticated_user
        return None