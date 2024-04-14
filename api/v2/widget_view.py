from adrf.viewsets import ViewSet
from asgiref.sync import sync_to_async
from rest_framework.response import Response

from api.auth import AsyncAuthentication
from api.v1.widget_view import WidgetSerializer
from core.models import Widget


class WidgetViewSet(ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    authentication_classes = [AsyncAuthentication]

    @sync_to_async
    def list(self, request):
        widgets = Widget.objects.filter(active=True).order_by("-created_on")
        return Response(data=WidgetSerializer(widgets, many=True).data)

    async def retrieve(self, request, pk):
        widget = await Widget.objects.aget(pk=pk)
        return Response(data=WidgetSerializer(widget).data)
