from django.contrib.auth import get_user_model
from rest_framework import serializers
from djoser import serializers as djoser_serializers

User = get_user_model()


class UserCreateSerializer(djoser_serializers.UserCreateSerializer):

    class Meta:
        model = User
        fields = ["email", "username", "name", "password", "date_of_birth", "avatar", "id"]
        ref_name = 'annolab_create_user'

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        return super(UserCreateSerializer, self).create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ["email", "username", "name", "date_of_birth", "avatar", "id"]
        ref_name = 'annolab_user'
