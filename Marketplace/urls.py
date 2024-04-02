"""Marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from Transactions.views import transactions, add_invoice
from mpesa.urls import mpesa_urls

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appMarketplace.urls')),
    path('', include('paypal.standard.ipn.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('freelancer/', include('freelancer.urls')),
    path('employee/', include('employee.urls')),
    path('details/', include('details.urls')),
    path('chats/', include(('chats.urls', 'chats'), namespace='chats')),
    path('completedtasks/', include(('Finished_Tasks.urls', 'uploads'), namespace='completedtasks')),
    path('mpesa/', include(mpesa_urls)),
    # path('message/', include('Comms.urls', namespace='my_app_messages')),
    path('transactions/', include('Transactions.urls', namespace='Transactions')),
    path('checkout/', include('yourDownloads.urls', namespace='checkouts')),
    
    # path('addInvoice/', include('Transactions.urls', namespace='addInvoice')),
]
