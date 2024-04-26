from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from payments.api_views import PaymentViewSet

router = DefaultRouter()
router.register(r"payments", PaymentViewSet, basename="payments")

urlpatterns = [
    path(
        f"{settings.API_V1_PREFIX}/",
        include(router.urls),
    ),
]
