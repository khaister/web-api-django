from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.tv_show_view import TvShowViewSet
from api.v1.widget_view import WidgetViewSet

router = DefaultRouter()
router.register(r"widgets", WidgetViewSet)
router.register(r"tv-shows", TvShowViewSet, basename="tv-shows")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
