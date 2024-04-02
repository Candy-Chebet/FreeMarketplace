from django.db import models

# Create your models here.


import os

from django.contrib.auth.models import User
from django.utils import timezone
from employee.models import This_Job



class completedWork(models.Model):
    completedWork_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    short_text = models.TextField()
    Amount = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
   

    def __str__(self):
         return self.title