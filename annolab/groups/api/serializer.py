from rest_framework import serializers
from annolab.groups.models import Group


class GroupSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField()

    class Meta:
        model = Group
        fields = ['avatar']
        ref_name = 'groups'
