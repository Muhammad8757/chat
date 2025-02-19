from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    path('ws/notifications/', consumers.NotificationConsumer.as_asgi()),

]