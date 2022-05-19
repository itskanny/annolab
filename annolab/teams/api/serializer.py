from rest_framework import serializers

from ..models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_date', 'updated_date', 'avatar', 'organization']
        read_only_fields = ['created_date', 'updated_date']


class TeamListingSerializer(serializers.ModelSerializer):
    total_members = serializers.IntegerField()


    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_date', 'updated_date', 'avatar', 'organization',
                  'total_members']
        read_only_fields = ['created_date', 'updated_date']
