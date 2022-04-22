from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser

from .serializer import ProjectsSerializer
from ..models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer
    queryset = Project.objects.all()
    parser_classes = [MultiPartParser]
