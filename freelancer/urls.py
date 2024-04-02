from django.urls import path, include
from . import views
from Transactions import views as transactions_views

app_name = 'freelancer'

urlpatterns = [
    path('', views.f_home, name='f_home'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/edit-profile/<int:user_id>/', views.edit_profile, name='edit_profile'),
    # path('transactions/', transactions_views.transactions, name='transactions'),
]
