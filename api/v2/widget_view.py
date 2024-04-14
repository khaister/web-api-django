from adrf.viewsets import ViewSet
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.response import Response

from api.v1.widget_view import WidgetSerializer
from core.models import Widget


class AsyncAuthentication(BaseAuthentication):
    async def authenticate(self, request) -> tuple[User, None]:
        return super().authenticate(request)


class AsyncPermission:
    async def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser


class WidgetViewSet(ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = WidgetSerializer

    @sync_to_async
    def list(self, request):
        widgets = Widget.objects.filter(active=True).order_by("-created_on")
        return Response(data=WidgetSerializer(widgets, many=True).data)

    async def retrieve(self, request, pk):
        widget = await Widget.objects.aget(pk=pk)
        return Response(data=WidgetSerializer(widget).data)
