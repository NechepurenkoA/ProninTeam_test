from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователей."""

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_password(self, data):
        password_validation.validate_password(data)
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class ChangePasswordSerializer(serializers.Serializer):
    """
    Сериализатор смены пароля.
    """

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, data):
        request = self.context["request"]
        if request.user.check_password(data):
            return data
        raise ValidationError("Старый пароль не совпадает!")
