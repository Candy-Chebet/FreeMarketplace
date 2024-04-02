# chat/views.py
from django.shortcuts import render
import json

def index(request):
    return render(request, 'chat/index.html', {})

def chat_room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })