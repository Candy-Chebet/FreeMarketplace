from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    # path('download/<int:task_id>/', download_attachment, name='download_attachment'),
    path('uploads/', views.upload_task, name='upload'),
    path('list/', views.listTasks, name='list'),
    path('update_task/<str:pk>/', views.update_task, name='update'),
]
