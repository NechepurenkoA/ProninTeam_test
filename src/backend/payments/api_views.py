from rest_framework import mixins, viewsets

from payments.models import Payment
from payments.serializers import PaymentSerializer


class PaymentViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Миксин вью-сет для объектов 'Payment'.
    """

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
