from rest_framework import serializers

from accounts.models import User, UserInfo, UserType, UserPermission


class UserPermissionSerializer(serializers.ModelSerializer):
    """
    Serializer для прав пользователей
    """

    class Meta:
        model = UserPermission
        fields = ('permission', 'title')


class UserTypeSerializer(serializers.ModelSerializer):
    """
    Serializer для типов пользователей
    """

    permissions = UserPermissionSerializer(read_only=True, many=True)

    class Meta:
        model = UserType
        fields = ('id_name', 'title', 'permissions')


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer для регистрации и получения прав
    """

    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    first_name = serializers.CharField(max_length=48, required=True)
    last_name = serializers.CharField(max_length=48, required=True)

    type = UserTypeSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'type')
        read_only_fields = ('id',)


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer для обновления данных пользователей
    """

    first_name = serializers.CharField(max_length=48, required=True)
    last_name = serializers.CharField(max_length=48, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserInfoSerializer(serializers.ModelSerializer):
    """
    Serializer для контактов пользователей
    """

    user = UserUpdateSerializer(write_only=True)

    class Meta:
        model = UserInfo
        fields = ('user', 'date_of_birth', 'phone_number', 'city', 'about_me')

    # TODO: переписать это говно на нормальный код
    def update(self, instance, validated_data):
        """
        Обновление профиля пользователя
        """

        user_info = validated_data.pop('user')

        instance.user.first_name = user_info.get('first_name')
        instance.user.last_name = user_info.get('last_name')
        instance.user.save()

        instance.date_of_birth = validated_data.get('date_of_birth')
        instance.phone_number = validated_data.get('phone_number')
        instance.city = validated_data.get('city')
        instance.about_me = validated_data.get('about_me')
        instance.save()

        return instance
