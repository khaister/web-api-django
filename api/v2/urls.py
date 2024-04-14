from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v2.widget_view import WidgetViewSet
from api.v2.tv_show_view import TvShowViewSet

router = DefaultRouter()
router.register(r"widgets", WidgetViewSet, basename="async-widget")
router.register(r"tv-shows", TvShowViewSet, basename="async-tv-show")

urlpatterns = [
    path("api/v2/", include(router.urls)),
]
