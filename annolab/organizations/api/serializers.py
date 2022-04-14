from rest_framework import serializers
from annolab.organizations.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'tagline', 'avatar', 'owner']
        ref_name = 'organizations'
