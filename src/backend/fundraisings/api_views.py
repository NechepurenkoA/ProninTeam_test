from rest_framework import mixins, permissions, viewsets

from fundraisings.models import Collect
from fundraisings.serializers import CollectSerializer


class CollectViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Миксин вью-сет для объектов 'Collect'.
    """

    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer
