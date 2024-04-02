from django.urls import path, re_path
from . import views


urlpatterns = [
  
    path('chat/', views.index, name='chat'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    
    
]
