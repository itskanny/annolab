from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Organization(models.Model):
    name = models.CharField(verbose_name='organization name', max_length=255, unique=True)
    tagline = models.TextField(verbose_name='organization tagline')
    avatar = models.ImageField(blank=True, null=True, upload_to='organization_avatars')
    owner = models.OneToOneField(get_user_model(), related_name='organization', on_delete=models.CASCADE)
