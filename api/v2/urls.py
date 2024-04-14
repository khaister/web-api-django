from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v2.widget_view import WidgetViewSet

router = DefaultRouter()
router.register(r"widgets", WidgetViewSet, basename="async-widget")

urlpatterns = [
    path("api/v2/", include(router.urls)),
]
