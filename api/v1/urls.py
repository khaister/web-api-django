from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.widget_view import WidgetViewSet

router = DefaultRouter()
router.register(r"widgets", WidgetViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
