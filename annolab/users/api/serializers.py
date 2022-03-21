from django.contrib.auth import get_user_model
# from rest_framework import serializers
from djoser import serializers

User = get_user_model()


class UserSerializer(serializers.UserCreateSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "name", "password", "date_of_birth", "avatar", "id"]
        ref_name = 'annolab_user'

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        return super(UserSerializer, self).create(validated_data)
