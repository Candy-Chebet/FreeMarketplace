from django.db import models
import os

from django.contrib.auth.models import User
from django.utils import timezone
from employee.models import This_Job



class completedTaskss(models.Model):
    taskName = models.CharField(max_length=120, default='', blank=True, null=True) 
    description = models.TextField(max_length=3000, default='', blank=True, null=True)
    completionDate = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    attachment = models.FileField(upload_to= 'Completed_tasks/', null=True, blank=True)  # This line defines the attachment field

    def __str__(self):
        return self.taskName
   