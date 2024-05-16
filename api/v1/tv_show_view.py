from rest_framework import permissions, viewsets
from rest_framework.response import Response

from core.services import tv_show_service


class TvShowViewSet(viewsets.ViewSet):
    queryset = None
    serializer_class = None
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        shows = tv_show_service.get_shows()
        return Response(shows.model_dump())
