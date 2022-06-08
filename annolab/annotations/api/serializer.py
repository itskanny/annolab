from rest_framework import serializers

from ..models import Annotation
from annolab.images.models import Image

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ['id', 'classification', 'created_date', 'updated_date', 'image', 'x', 'y', 'width', 'height']
        read_only_fields = ['created_date', 'updated_date']

    def create(self, validated_data):
        validated_data['image'].is_annotated = True
        validated_data['image'].save()
        return super(AnnotationSerializer, self).create(validated_data)
