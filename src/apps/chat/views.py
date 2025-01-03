from django.shortcuts import render
from rest_framework.decorators import api_view

@api_view(["GET"])
def index(request):
    return render(request, "chat/index.html")

@api_view(["GET"])
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})