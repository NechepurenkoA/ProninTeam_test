from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from fundraisings.api_views import CollectViewSet

router = DefaultRouter()
router.register(r"collections", CollectViewSet, basename="collections")

urlpatterns = [
    path(
        f"{settings.API_V1_PREFIX}/",
        include(router.urls),
    ),
]
