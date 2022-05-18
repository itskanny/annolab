import django.db.utils
from rest_framework import serializers
from annolab.organizations.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'tagline', 'avatar', 'owner']
        read_only_fields = ['created_date', 'updated_date']
        ref_name = 'organizations'

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        try:
            return super(OrganizationSerializer, self).create(validated_data)
        except django.db.utils.IntegrityError:
            raise serializers.ValidationError({"name": ["User already has an organization"]})
