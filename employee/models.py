from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# import os

# # Create your models here.
# def generate_attachment_path(instance, filename):
#     # Get the filename and extension
#     base_filename, extension = os.path.splitext(filename)
#     # Generate a new filename
#     new_filename = f"{instance.taskName}_{instance.id}{extension}"
#     # Return the path where the file will be uploaded
#     return os.path.join('attachments', new_filename)

class This_Job(models.Model):
    user = models.CharField(max_length=120, default='', blank=True, null=True) 
    title = models.CharField(max_length=500)
    short_text = models.TextField()
    time = models.CharField(max_length=50)
    skill = models.CharField(max_length=100)
    budget = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
