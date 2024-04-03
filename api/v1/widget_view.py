from rest_framework import serializers, permissions, viewsets

from core.models import Widget


class WidgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Widget
        fields = ["name", "description", "quantity", "active"]


class WidgetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Widget.objects.all().order_by("-created_on")
    serializer_class = WidgetSerializer
    permission_classes = [permissions.IsAuthenticated]
