from rest_framework import serializers

from payments.models import Payment
from users.serializers import UserSerializer


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор доната"""

    user = UserSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"

    def create(self, validated_data):
        payment = Payment.objects.create(
            user=self.context["request"].user, **validated_data
        )
        return payment
