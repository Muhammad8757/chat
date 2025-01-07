from django.urls import path

from src.apps.accounts.views.views import RegisterAPIView, login_html, register_html


urlpatterns = [
    path("register/", RegisterAPIView.as_view({"post": "register"})),
    path("login/", RegisterAPIView.as_view({"post": "login"})),
    path("login_html/", login_html, name="test"),
    path("register_html/", register_html, name="register"),
]
