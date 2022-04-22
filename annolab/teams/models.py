from django.db import models

from annolab.organizations.models import Organization


# Create your models here.

class Team(models.Model):
    name = models.CharField(verbose_name='Team Name', max_length=255, unique=True)
    description = models.TextField(verbose_name='Team Description', )
    avatar = models.ImageField(upload_to='team_avatar', blank=True, null=True)
    organization = models.ForeignKey(Organization, related_name='teams', on_delete=models.CASCADE)
