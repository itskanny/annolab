from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser

from .serializer import ProjectsSerializer
from ..models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer
    queryset = Project.objects.all()
    parser_classes = [MultiPartParser, JSONParser]

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.organization.id, int)

        return self.queryset.filter(organization=self.request.organization.id)
