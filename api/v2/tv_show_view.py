from adrf.viewsets import ViewSet
from rest_framework.response import Response

from api.auth import AsyncAuthentication
from core.services import tv_show_service


class TvShowViewSet(ViewSet):
    authentication_classes = [AsyncAuthentication]

    async def list(self, request):
        shows = await tv_show_service.get_shows_async()
        return Response(shows.model_dump())
