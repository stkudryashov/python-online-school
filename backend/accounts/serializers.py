from rest_framework import serializers

from accounts.models import *


class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermission
        fields = ('permission', 'title')


class UserTypeSerializer(serializers.ModelSerializer):
    permissions = UserPermissionSerializer(read_only=True, many=True)

    class Meta:
        model = UserType
        fields = ('id_name', 'title', 'permissions')


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    first_name = serializers.CharField(max_length=48, required=True)
    last_name = serializers.CharField(max_length=48, required=True)

    type = UserTypeSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'type')
        read_only_fields = ('id',)
