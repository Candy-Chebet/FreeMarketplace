from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('', views.e_home, name='e_home'),
    path('add-job/', views.add_job, name='add_job'),
    # path('edit-job/', views.edit_job, name='edit_job'),  # Uncomment if needed
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/edit-profile/<int:user_id>/', views.edit_profile, name='edit_profile'),
]
