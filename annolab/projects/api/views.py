from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.serializers import ValidationError

from .serializer import ProjectSerializer, ProjectListSerializer
from ..models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.with_details()
    parser_classes = [MultiPartParser, JSONParser]

    def get_queryset(self, *args, **kwargs):
        if not self.request.organization:
            raise ValidationError({'non_field_errors': ['Organization with id does not exist']})
        assert isinstance(self.request.organization.id, int)
        return self.queryset.filter(organization=self.request.organization.id)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectSerializer

