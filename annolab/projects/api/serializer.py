from rest_framework import serializers

from ..models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'avatar', 'organization']
        read_only_fields = ['created_date', 'updated_date']


class ProjectListSerializer(serializers.ModelSerializer):
    total_images = serializers.IntegerField()
    annotated_images = serializers.IntegerField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'avatar', 'organization', 'total_images', 'annotated_images']
        read_only_fields = ['created_date', 'updated_date']
