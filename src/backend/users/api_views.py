from http import HTTPMethod, HTTPStatus

from django.contrib.auth import update_session_auth_hash
from rest_framework import mixins, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from users.models import User
from users.serializers import (
    ChangePasswordSerializer,
    UserSerializer,
    UserSignUpSerializer,
)


class UserSingUpViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Миксин вью-сет для регистрации.
    """

    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer
    permission_classes = (permissions.AllowAny,)


class UserViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Миксин вью-сет для объектов 'User'.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view([HTTPMethod.POST])
@permission_classes([permissions.IsAuthenticated])
def change_password(request):
    """Смена пароля."""

    serializer = ChangePasswordSerializer(
        data=request.data, context={"request": request}
    )
    if serializer.is_valid(raise_exception=True):
        request.user.set_password(serializer.validated_data["new_password"])
        request.user.save()
        update_session_auth_hash(request, request.user)
        return Response(
            {"message": "Пароль изменен успешно!"},
            HTTPStatus.OK,
        )
    return Response(serializer.errors, HTTPStatus.BAD_REQUEST)
