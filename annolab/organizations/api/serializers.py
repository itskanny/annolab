import django.db.utils
from rest_framework import serializers
from annolab.organizations.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'tagline', 'avatar', 'owner', 'created_date', 'updated_date', ]
        read_only_fields = ['created_date', 'updated_date']
        ref_name = 'organizations'

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        try:
            return super(OrganizationSerializer, self).create(validated_data)
        except django.db.utils.IntegrityError:
            raise serializers.ValidationError({"name": ["User already has an organization"]})


class OrganizationListingSerializer(serializers.ModelSerializer):
    total_projects = serializers.IntegerField()
    total_teams = serializers.IntegerField()

    class Meta:
        model = Organization
        fields = ['id', 'name', 'tagline', 'avatar', 'owner', 'created_date', 'updated_date',
                  'total_projects', 'total_teams']
        read_only_fields = ['created_date', 'updated_date']
