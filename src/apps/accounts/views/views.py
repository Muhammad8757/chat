from django.shortcuts import render
from rest_framework import viewsets, status
from src.apps.chat.services import send_websocket
from src.apps.accounts.dtos.user_dto import LoginDto, UserDto
from src.apps.accounts.functions import get_token
from src.apps.accounts.models import User
from src.apps.accounts.serializers import auth_serializer
from src.apps.accounts.mapper import UserMapper
from src.apps.accounts.services.auth_service import UserService
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class RegisterAPIView(viewsets.GenericViewSet):
    model = User

    def get_serializer_class(self):
        if self.action == "register":
            return auth_serializer.AuthSerializer
        return auth_serializer.LoginSerializer
    
    def register(self, request, *args, **kwargs):
        data = self.request.data
        serializer = auth_serializer.AuthSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        dto = UserMapper.from_serializer_to_dto(UserDto, serializer, ["username", "email", "phone", "password"])
        if UserService.create_user(self, request, dto):
            return Response({"data": "success"}, status=status.HTTP_200_OK)
        return Response({"data": "Fail"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def login(self, request, *args, **kwargs):
        data = self.request.data
        serializer = auth_serializer.LoginSerializer(data=data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        dto = UserMapper.from_serializer_to_dto(LoginDto, serializer, ["username", "password"])
        user = UserService.login(self, request, dto)
        if user:
            send_websocket(
                group=f"notifications_{user.id}",
                data={"message": "У тебя новое уведомление!"},
            )
            token = get_token(user)
            return Response(token, status=status.HTTP_200_OK)
        return Response({"data": "invalid creditals"}, status=status.HTTP_404_NOT_FOUND)

@permission_classes([IsAuthenticated])
@api_view(["GET"])
def login_html(request):
    return render(request, "accounts/login.html")

@permission_classes([IsAuthenticated])
@api_view(["GET"])
def register_html(request):
    return render(request, "accounts/register.html")