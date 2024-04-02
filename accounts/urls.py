from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('employeesignup/', views.SignUpViewE, name="e_reg"),
    path('freelancersignup/', views.SignUpViewF, name="f_reg"),
]
