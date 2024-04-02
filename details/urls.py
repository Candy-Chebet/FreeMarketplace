from django.urls import path, re_path
from . import views

app_name = 'details'

urlpatterns = [
    re_path(r'^job-details/(?P<job_id>[0-9]+)/$', views.job_details, name='job_details'),
    re_path(r'^job-details/edit-job/(?P<job_id>[0-9]+)/$', views.edit_job, name='edit_job'),
    re_path(r'^job-details/edit-bid/(?P<bid_id>[0-9]+)/$', views.edit_bid, name='edit_bid'),
]
