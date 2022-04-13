from django.db import models


# Create your models here.
class Group(models.Model):
    avatar = models.ImageField(upload_to='group', blank=True, null=True)
