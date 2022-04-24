import django.core.handlers.wsgi
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

from .serializers import OrganizationSerializer
from ..models import Organization


class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    parser_classes = [MultiPartParser, JSONParser, FormParser]

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)

        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(owner=self.request.user.id)
