from rest_framework import serializers

from ..models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'name', 'created_date', 'updated_date', 'image', 'project', 'is_annotated']
        read_only_fields = ['created_date', 'updated_date', 'is_annotated', 'name']

    def create(self, validated_data):
        validated_data['name'] = validated_data['image']
        print(validated_data)

        return super(ImageSerializer, self).create(validated_data)

