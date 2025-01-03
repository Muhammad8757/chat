from src.apps.accounts.dtos.user_dto import UserDto
from ..models import User
from django.contrib.auth import authenticate

class UserRespository:
    @staticmethod
    def create_user(user_dto: UserDto):
        user: User = User.objects.create(
            username=user_dto.username,
            email=user_dto.email,
            phone=user_dto.phone,
        )
        user.set_password(user_dto.password)
        user.save()
        return user

    
    @staticmethod
    def login(user: User):
        authenticated_user = authenticate(username=user.username, password=user.password)
        if authenticated_user is None:
            return False
        return authenticated_user
