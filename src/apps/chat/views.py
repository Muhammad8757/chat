from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated])
@api_view(["GET"])
def index(request):
    return render(request, "chat/index.html")


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})