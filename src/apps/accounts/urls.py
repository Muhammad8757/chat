from django.urls import path

from src.apps.accounts.views.views import RegisterAPIView


urlpatterns = [
    path("register/", RegisterAPIView.as_view({"post": "register"})),
    path("login/", RegisterAPIView.as_view({"post": "login"})),
]
