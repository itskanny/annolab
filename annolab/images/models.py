from django.db import models

from annolab.projects.models import Project


# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=255, blank=True)
    is_annotated = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='project_images')
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
