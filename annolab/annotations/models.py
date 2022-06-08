from django.db import models

# Create your models here.
from annolab.images.models import Image

class Annotation(models.Model):
    classification = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    image = models.ForeignKey(Image, related_name='src_image', on_delete=models.CASCADE)
