from django.db import models

from annolab.organizations.models import Organization


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Project Name')
    description = models.TextField(verbose_name='Project Description')
    avatar = models.ImageField(upload_to='project_avatars', blank=True, null=True)
    organization = models.ForeignKey(Organization, related_name='projects', on_delete=models.CASCADE)

