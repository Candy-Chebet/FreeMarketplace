from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'yourDownloads'

urlpatterns = [
    path('checkout/', views.All, name='checkout'),
    path('checkout/<int:completedWork_id>/', views.Checkout, name='checkout-with-title'),
    path('payment-success/<str:completedWork_id>/', views.PaymentSuccessful, name='payment-success'),
    path('payment-failed/<int:completedWork_id>/', views.paymentFailed, name='payment-failed'),
]
