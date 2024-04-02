from django.urls import path
from . import views

app_name = 'appMarketplace'

urlpatterns = [
    path('', views.index, name='index'),  # Removed the '$' character
    path('about/', views.about, name='about'),
    path('contact/', views.contact_us, name='contact_us'),
]
