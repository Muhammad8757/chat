from django.urls import path
from src.apps.chat.views import room, index

urlpatterns = [
    path("<str:room_name>/", room, name="room"),
    path("", index, name="index"),
]
