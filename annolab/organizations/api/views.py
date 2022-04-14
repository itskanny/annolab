from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser

from .serializers import OrganizationSerializer
from ..models import Organization


class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    parser_classes = [MultiPartParser]
