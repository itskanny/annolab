from django.db import models

from annolab.organizations.models import Organization

from django.contrib.auth import get_user_model

# Create your models here.
from annolab.teams.managers import TeamListingManager


class Team(models.Model):
    name = models.CharField(verbose_name='team name', max_length=255, unique=True)
    description = models.TextField(verbose_name='team description', )
    avatar = models.ImageField(upload_to='team_avatar', blank=True, null=True)
    organization = models.ForeignKey(Organization, related_name='teams', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(get_user_model(), related_name='teams')

    objects = TeamListingManager()
