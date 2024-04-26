from rest_framework import serializers

from fundraisings.models import Collect
from payments.serializers import PaymentSerializer
from users.serializers import UserSerializer


class CollectSerializer(serializers.ModelSerializer):
    """Сериализатор доната"""

    author = UserSerializer(read_only=True)
    payments = serializers.SerializerMethodField()

    class Meta:
        model = Collect
        fields = "__all__"
        extra_kwargs = {
            "payments": {
                "read_only": True,
            },
        }
        read_only_fields = ["collected", "users_donated", "collected_on"]

    def get_payments(self, obj):
        donos = obj.donations
        return PaymentSerializer(donos, many=True).data

    def create(self, validated_data):
        collect = Collect.objects.create(
            author=self.context["request"].user, **validated_data
        )
        return collect
